#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : etc.py
# Create date : 2019-01-30 15:17
# Modified date : 2019-03-20 16:41
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import torch
from etc_model_dict import pretrained_model_dict

config = {}

config["use_spacy"] = True
#config["use_spacy"] = False

config["device"] = torch.device("cuda" if torch.cuda.is_available() else "cpu")
config["trian_batch_size"] = 16
config["special_tokens_lt"] = ['_start_', '_delimiter_', '_classify_']

config["model_name"] = "./openai_gpt_model"
config["do_train"] = True
config["do_eval"] = True
config["output_dir"] = "../log"
config["seed"] = 42
config["num_train_epochs"] = 1
config["train_batch_size"] = 16
config["eval_batch_size"] = 16
config["max_grad_norm"] = 1
config["learning_rate"] = 6.25e-5
config["warmup_proportion"] = 0.002
#config["lr_schedule"] = "warmup_linear"
config["weight_decay"] = 0.01
config["lm_coef"] = 0.9
config["n_valid"] = 374
config["data_dir"] = "./data"
config["model_dir"] = "%s/cache_model" % config["data_dir"]
config["spacy_dir"] = "%s/spacy" % config["data_dir"]
config["dataset_dir"] = "%s/dataset" % config["data_dir"]
config["dataset"] = "%s/ROCStories" % config["dataset_dir"]
config["train_dataset"] = "%s/cloze_test_val__spring2016 - cloze_test_ALL_val.csv" % config["dataset"]
config["eval_dataset"] = "%s/cloze_test_test__spring2016 - cloze_test_ALL_test.csv" % config["dataset"]
config["pretrained_model_dict"] = pretrained_model_dict
