'''
Author: jerrery.li
Date: 2024-02-19 11:34:24
LastEditors: jerrery.li
LastEditTime: 2024-02-19 16:05:39
FilePath: /图解GPT/1.1 N-gram/Bigram.py
Description: 
'''
from collections import defaultdict,Counter

corpus = ["我喜欢吃苹果",
          "我喜欢吃香蕉",
          "她喜欢吃葡萄",
          "他不喜欢吃香蕉",
          "他喜欢吃苹果",
          "她喜欢吃草莓"]

#把句子分为N个 Gram
def tokenize(text):
    return [char for char in text]

#计算每个Bigram出现的次数
def count_ngrams(coupus,n):
    ngrams_count = defaultdict(Counter) #创建一个字典，存储N-gram计数
    for text in corpus: 
        tokens = tokenize(text) #对文本进行分词
        for i in range(len(tokens)-n +1): #遍历分词结果，生成N-Gram
            ngram = tuple(tokens[i:i+n]) #创建一个N-Gram元组
            prefix = ngram[:-1] # 获取N-Gram的前缀
            token = ngram[-1]   # 获取N-Gram的目标单字
            ngrams_count[prefix][token] += 1 #更新N-Gram计算
    return ngrams_count

bigram_counts = count_ngrams(corpus,3) #计算词频
print("Bigram 词频：")
for prefix,counts in bigram_counts.items():
    print("{}:{}".format("".join(prefix),dict(counts)))

# 计算每个Bigram的出现频率
def ngram_probabilities(ngram_counts):
    ngram_probs = defaultdict(Counter)
    for prefix,tokens_count in bigram_counts.items(): #遍历N-Gram前缀
        total_count = sum(tokens_count.values())
        for token, count in tokens_count.items():
            ngram_probs[prefix][token] = count/total_count
    return ngram_probs

bigram_probs = ngram_probabilities(bigram_counts)
print("\n bigram出现的概率：")
for prefix,probs in bigram_probs.items():
    print("{}:{}".format("".join(prefix),dict(probs)))


#根据Bigram出现的频率，定义下一个词的函数
def generate_next_token(prefix, ngram_probs):
    if prefix not in ngram_probs:
        return None
    next_token_probs = ngram_probs[prefix]
    next_token = max(next_token_probs, key=next_token_probs.get)
    return next_token

#生成连续文本
def generate_text(prefix, ngram_probs,n,length=6):
    tokens = list(prefix) #将前缀转换为字符串列表
    for _ in range(length - len(prefix)): #根据指定长度生成文本
        # next_token = generate_next_token(prefix,ngram_probs)
        next_token = generate_next_token(tuple(tokens[-(n-1):]), ngram_probs) 
        if not next_token:
            break
        tokens.append(next_token)
    return "".join(tokens)

generated_text = generate_text("我喜",bigram_probs,3)
print("生成的文本：{}".format(generated_text))

