#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-03-16 12:23
# Modified date : 2019-03-20 16:04
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from pybase import pylog
from etc import config
import show
import train_graph
import eval_graph

def run_directly(config):
    train_loss, model_config = train_graph.direct_save(config)
    eval_loss, eval_accuracy = eval_graph.do_eval(model_config, config)
    show.show_result_detail(eval_loss, eval_accuracy, train_loss, config)

def run_finetuned(config):
    train_loss, model_config = train_graph.do_train(config)
    eval_loss, eval_accuracy = eval_graph.do_eval(model_config, config)
    show.show_result_detail(eval_loss, eval_accuracy, train_loss, config)

def run(config):
    show.show_devices(config)
#    run_directly(config)
    run_finetuned(config)

run(config)
