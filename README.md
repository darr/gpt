# gpt

#### Description
implement OpenAI gpt

## How To Run?

```shell
bash run.sh
```

Yes, just run the shell, it can work.
run.sh will create a virtual env that needed by gpt, and install all  
software that needed by gpt.  

And how about the pretrained model ,config and dataset that we need  
for finetune?  

All of them will be download and cached after we run the shell run.sh  

In a word, just run the shell:  
```shell
bash run.sh
```
Then you get a result.  

And if you need,read the code.  

## papers

[Gaussian Error Linear Units](https://arxiv.org/pdf/1606.08415.pdf)  
[translate to chinese](./papers/GAUSSIAN_ERROR_LINEAR_UNITS1606.08415.md)  

[Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)  
[translate to chinese](./papers/Attention_Is_All_You_Need1706.03762.md)  

[Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)  
[translate to chinese](./papers/Improving_Language_Understanding_by_Generative_Pre-Training.md)  

[Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)  
[translate to chinese](./papers/Language_Models_are_Unsupervised_Multitask_Learners.md)  

## Dataset

use the dataset ROCStories

## output

### my device
```shell
31.4 GiB
Intel® Core™ i7-8700K CPU @ 3.70GHz × 12 
GeForce GTX 1080 Ti/PCIe/SSE2
64-bit
```

### run three epochs

with 40 seconds an epoch for train and 23 seconds an epoch for eval,  
so we need less than 3 minutes to get the results below.  

```shell
show.py line:42 ***** Eval results *****
show.py line:44 eval_accuracy = 0.874933190807055
show.py line:44 eval_loss = 0.432198545569156
show.py line:44 train_loss = 2.201771383611565
```

### run one epoch

with 40 seconds an epoch for train and 23 seconds an epoch for eval,  
so we need about 1 minutes to get the results below.  

```shell
show.py line:42 ***** Eval results *****
show.py line:44 eval_accuracy = 0.863174772848744
show.py line:44 eval_loss = 0.31887995107815814
show.py line:44 train_loss = 3.087455103540013
```

### run 10 epochs

with 40 seconds an epoch for train and 23 seconds an epoch for eval,  
so we need about 7 minutes to get the results below.  

```shell
show.py line:42 ***** Eval results *****
show.py line:44 eval_accuracy = 0.8786745056119722
show.py line:44 eval_loss = 0.5693538990389142
show.py line:44 train_loss = 1.2477980831749418
```

### run 30 epochs

with 40 seconds an epoch for train and 23 seconds an epoch for eval,  
so we need about 21 minutes to get the results below.  

```shell
show.py line:42 ***** Eval results *****
show.py line:44 eval_accuracy = 0.8727952966328166
show.py line:44 eval_loss = 0.6764590177271101
show.py line:44 train_loss = 0.23714334345780885
```

### run directly
with 23 seconds an epoch for eval,  
so we need about half a minutes to get the results below.  

```shell
show.py line:42 ***** Eval results *****
show.py line:44 eval_accuracy = 0.5611972207375735
show.py line:44 eval_loss = 0.6895335352318919
show.py line:44 train_loss = 0.0
```
