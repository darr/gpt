#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : gpt_cache.py
# Create date : 2019-03-17 17:50
# Modified date : 2019-03-20 17:02
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import shutil
import tempfile
import sys
from io import open

import tarfile
import requests
from tqdm import tqdm

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from pybase import pylog

def _split_path(url):
    parsed = urlparse(url)
    if not parsed.netloc or not parsed.path:
        raise ValueError("bad s3 path {}".format(url))
    bucket_name = parsed.netloc
    file_path = parsed.path
    if file_path.startswith("/"):
        file_path = file_path[1:]
    return bucket_name, file_path

def _get_file_name_from_path(file_path):
    lt = file_path.split('/')
    return lt[-1]

def _get_file_name(url):
    bucket_name, file_path = _split_path(url)
    file_name = _get_file_name_from_path(file_path)
    return file_name

def _http_get(url, temp_file):
    req = requests.get(url, stream=True)
    content_length = req.headers.get('Content-Length')
    total = int(content_length) if content_length is not None else None
    progress = tqdm(unit="B", total=total)
    for chunk in req.iter_content(chunk_size=1024):
        if chunk:
            progress.update(len(chunk))
            temp_file.write(chunk)
    progress.close()

def _create_model_dir(cache_dir):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

def _write_temp_file(url, cache_path):
    with tempfile.NamedTemporaryFile() as temp_file:
        pylog.info("tempfile: %s" %  (temp_file.name))
        _http_get(url, temp_file)
        temp_file.flush()
        temp_file.seek(0)
        pylog.info("copying %s to cache at %s" % (temp_file.name, cache_path))
        with open(cache_path, 'wb') as cache_file:
            shutil.copyfileobj(temp_file, cache_file)

def _download_file_from_web(url, cache_dir):
    _create_model_dir(cache_dir)
    filename = _get_file_name(url)
    cache_path = os.path.join(cache_dir, filename)

    if not _check_is_cached_the_file(url, cache_path):
        _write_temp_file(url, cache_path)
        return False, cache_path
    return True, cache_path

def _check_is_cached_the_file(url, cache_path):
    if not os.path.exists(cache_path):
        pylog.info("not found %s, downloading %s to tempfile" %  (cache_path, url))
        return False
    else:
        pylog.debug("do not need download, exists %s" % cache_path)
        return True

def _check_and_decompression(filename, cache_dir):
    _check_and_untar(filename, cache_dir)

def _check_and_untar(filename, cache_dir):
    name_lt = filename.split('.')
    if name_lt[-1] == "gz" and name_lt[-2] == 'tar':
        cache_path = os.path.join(cache_dir, filename)
        _untar(cache_path, cache_dir)

def _untar(filename, dirs):
    t = tarfile.open(filename)
    pylog.info("decompression %s" % filename)
    t.extractall(path=dirs)

def _install_spacy(cache_path):
    pylog.info(cache_path)
    cmd_str = "pip install %s" % cache_path
    pylog.info(cmd_str)
    os.system(cmd_str)

def _get_spacy_en_install_path(config):
    spacy_dict = config["pretrained_model_dict"]["spacy"]
    env_path = os.path.dirname(os.__file__)
    install_path = "%s/site-packages/%s/%s" % (env_path, spacy_dict["name"], spacy_dict["name_ver"])
    pylog.info(install_path)
    return install_path

def get_spacy(url, cache_dir="./spacy"):
    is_cached, cache_path = _download_file_from_web(url, cache_dir)
    if not is_cached:
        _install_spacy(cache_path)
    return cache_path

def get_dataset(url, cache_dir="./data"):
    is_cached, cache_path = _download_file_from_web(url, cache_dir)
    if not is_cached:
        filename = _get_file_name(url)
        _check_and_decompression(filename, cache_dir)
    return cache_path

def get_dataset_path(config):
    data_dict = config["pretrained_model_dict"]["data"]
    cache_dir = config["dataset_dir"]
    url = data_dict["url"]
    file_path = get_dataset(url, cache_dir)
    return file_path

def get_pretrained_model(url, cache_dir="./cache_model"):
    is_cached, cache_path = _download_file_from_web(url, cache_dir)
    if not is_cached:
        pass
    return cache_path

def get_model_file_path(name,config):
    pretrained_model_dict = config["pretrained_model_dict"]
    dic = pretrained_model_dict[name]
    url = dic["url"]
    cache_dir = config["model_dir"]
    file_path = get_pretrained_model(url, cache_dir)
    return file_path

def get_spacy_file_path(config):
    pretrained_model_dict = config["pretrained_model_dict"]
    dic = pretrained_model_dict["spacy"]
    url = dic["url"]
    cache_dir = config["spacy_dir"]
    file_path = get_spacy(url, cache_dir)
    install_path = _get_spacy_en_install_path(config)

    return install_path
