"""
@author: liucong
@contact: logcongcong@gmail.com
@time: 2020/7/29 11:25
"""
import json
import random


# 判断句子中是否包含敏感词
def remove_dirty_sentence(dirty_obj, sentence):
    if len(dirty_obj.match(sentence)) == 0:
        return False
    else:
        return True


# 判断字符串中是否包含汉字
def is_chinese_char(text):
    for c in text:
        cp = ord(c)
        if ((cp >= 0x4E00 and cp <= 0x9FFF) or (cp >= 0x3400 and cp <= 0x4DBF) or (cp >= 0x20000 and cp <= 0x2A6DF)
                or (cp >= 0x2A700 and cp <= 0x2B73F) or (cp >= 0x2B740 and cp <= 0x2B81F) or (cp >= 0x2B820 and cp <= 0x2CEAF)
                or (cp >= 0xF900 and cp <= 0xFAFF) or (cp >= 0x2F800 and cp <= 0x2FA1F)):
            return True
    return False


# 将对话预料构建成unilm所需要得数据格式，并过滤无效数据
def build_data_for_train(path, save_path):
    sample_list = []
    with open(path, "r", encoding="utf-8") as fh:
        data_dict = json.load(fh)
        for key in data_dict.keys():
            if len(key) > 64:
                continue
            vaule = data_dict[key]
            if len(vaule) > 10:
                random.shuffle(vaule)
                for j in range(10):
                    if not is_chinese_char(vaule[j]):
                        continue
                    if len(vaule[j]) > 64:
                        continue
                    sample_list.append({"src_text": key, "tgt_text": vaule[j]})
            else:
                for vaule_ in vaule:
                    if not is_chinese_char(vaule_):
                        continue
                    if len(vaule_) > 64:
                        continue
                    sample_list.append({"src_text": key, "tgt_text": vaule_})
    random.shuffle(sample_list)
    fin = open(save_path, "w", encoding="utf-8")
    for sample in sample_list:
        fin.write(str(sample) + "\n")


if __name__ == "__main__":
    douban_path = "data/douban.json"
    kuakua_save_path = "data/merge_data.json"
    build_data_for_train(douban_path, kuakua_save_path)

