# Unilm for Chinese Chitchat Robot

## 描述
* 本项目使用[unilm模型](https://github.com/YunwenTechnology/Unilm)训练了一个夸夸式的闲聊机器人。
* 详细介绍见知乎：[夸夸式闲聊机器人之Unilm对话生成]()


## 数据及模型
* 原始语料来自豆瓣夸夸群数据，见data/douban_kuakua_qa.txt。
* 经过清洗后，得到了6万多单轮对话数据，见data/kuakua_data.json。
* 已训练好的模型，下载地址：[链接]()，验证码： [3333]()


## Train

```
nohup python3 -u run_train.py --data_dir data/ 
                              --src_file merge_data.json 
                              --model_type unilm 
                              --model_name_or_path unilm_model/ 
                              --output_dir kuakua_robot_model/ 
                              --max_seq_length 128 
                              --max_position_embeddings 512 
                              --do_train 
                              --do_lower_case 
                              --train_batch_size 32 
                              --learning_rate 2e-5 
                              --logging_steps 100 
                              --num_train_epochs 10 > log.log 2>&1 &
```
训练机器2060s，batch_size为32，训练了10个epoch。
Loss如下：
![avatar](image/tensorboard.png)
通过loss曲线来看，其实模型并没有完全收敛，loss还有很大的下降幅度，可以继续进行训练，效果应该会更好。

## Test
```
python3 interactive_conditional_samples.py
```