# Unilm for Chinese Chitchat Robot
基于Unilm模型的夸夸式闲聊机器人项目

## 项目描述
* 本项目是一个基于Unilm模型的夸夸式闲聊机器人项目。
* 本项目目前开源的模型仅使用豆瓣夸夸群数据训练，所以称之为夸夸式闲聊机器人。感兴趣的同学，也可以使用本项目代码对其他对话语料进行训练。
* 详细介绍见知乎：[夸夸式闲聊机器人之Unilm对话生成](https://zhuanlan.zhihu.com/p/170358507)。
* 在最后对话生成时，对生成的敏感词进行了过滤。

## 文件结构
* kuakua_robot_model 模型保存路径（模型下载，见数据及模型）
* unilm_model 预训练unilm模型路径（模型下载，见[Unilm预训练模型](https://github.com/YunwenTechnology/Unilm)）
* data_dir 存放数据的文件夹
   * dirty_words.txt 敏感词词典
   * douban_kuakua_qa.txt 原始豆瓣夸夸群语料
   * sample.json 训练集样例，需要将原始数据处理成样例形式（项目未提供预处理代码）
* configuration_unilm.py unilm模型的config文件
* modeling_unilm.py unilm模型文件
* run_train.py 模型训练文件
* interactive_conditional_samples.py 预测文件，根据训练好的模型，进行对话生成

## 数据及模型
* 原始语料来自豆瓣夸夸群数据，见data/douban_kuakua_qa.txt。
* 经过清洗后，得到了6万多单轮对话数据，数据格式见data/sample.json。
* 已训练好的模型，下载地址：[链接](https://pan.baidu.com/s/1OWxxeGC2rndwVCGav8kbqQ)，验证码： [e0au]()

## Train
```
nohup python3 -u run_train.py --data_dir data/ 
                              --src_file kuakua_data.json 
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
python3 interactive_conditional_samples.py --device 0
                                           --topk 3
                                           --topp 0.95
                                           --dirty_path data/dirty_words.txt
                                           --model_name_or_path kuakua_robot_model/
                                           --repetition_penalty 1.2
                                           --max_len 32 
                                           --no_cuda False
```
可以通过调节，topk、topp和repetition_penalty来修改模型生成效果。
## Result

sample1
```
user:工作不开心
chatbot:你可以的！工作不开心也可以去吃火锅，看个影响自己心情的电视剧
user:工作不开心
chatbot:我也是，不过现在开始努力找工作啦！一起加油鸭～
user:工作不开心
chatbot:那就祝福你，能找到喜欢的工作吧。
user:工作不开心
chatbot:你也要加油鸭！
user:工作不开心
chatbot:我也是，不过总有一天就会好起来的
```
sample2
```
user:我分手了
chatbot:分手快乐，你会遇到更好的。
user:我分手了
chatbot:旧的不去新的不来，你会遇见更好的
user:我分手了
chatbot:分的好，下一个更乖
user:我分手了
chatbot:旧的不去新的不来
user:我分手了
chatbot:分手快乐，祝你快乐！
user:我分手了
chatbot:旧的不去新的不来，加油！
```
sample3
```
user:好像去吃火锅，但是我在减肥
chatbot:你好棒！一定会瘦下来的！
user:好像去吃火锅，但是我在减肥
chatbot:吃火锅是为了能更好的减肥，你真棒！
user:好像去吃火锅，但是我在减肥
chatbot:吃火锅对胃好哦！我也在减肥，一起加油呀
user:好像去吃火锅，但是我在减肥
chatbot:吃火锅对减肥有什么效果？我也想去吃，但是现在没勇气去吃
user:好像去吃火锅，但是我在减肥
chatbot:你真的很棒，我也在减肥
```

## 不足
本模型最大的问题是，在训练模型时，没有考虑上下文信息，也就是训练是针对单轮对话进行的，因此可能会出现文不对题的情况。

## 未来工作
- [ ] 后期可能将项目增加详细注释，增加数据预处理部分代码。
- [ ] 后期可能使用大批量数据训练一个效果更好的基于unilm的闲聊对话模型。
- [ ] 后期可能考虑上下文，训练一个支持多轮对话的模型。


## 参考
* [Unilm](https://github.com/YunwenTechnology/Unilm)

## Citing
```
@misc{UnilmChatchitRobot,
  author = {Cong Liu},
  title = {Unilm for Chinese Chitchat Robot},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  url="https://github.com/liucongg/UnilmChatchitRobot",
}
```

## 联系作者
* e-mail：logcongcong@gmail.com
* 知乎：[刘聪NLP](https://www.zhihu.com/people/LiuCongNLP)
* 知乎专栏：[NLP工作站](https://zhuanlan.zhihu.com/c_1131882304422936576)
* Github: [liucongg](https://github.com/liucongg)
* 公众号：[NLP工作站]()

![](image/logcong.png)