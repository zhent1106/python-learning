"""
中文文本情感分析
"""
from snownlp import SnowNLP

text = '人们日常所犯的最大错误是对陌生人太客气，对亲密的人太苛刻，要努力改变这个习惯！'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表实正面情绪。越接近0表示负面情绪
text1 = '这部电影是真心棒'
text2 = '这部电影剧情烂透了'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
print(text1, s1.sentiments)
print(text2, s2.sentiments)

# 关键字抽取
text3 = '请允许我尘埃落定，用沉默埋葬过去，满身风雨我从海上来，才隐居到这沙漠，该隐瞒的事总是清晰，千言万语只能无语，爱是天时地利人和的迷信，原来你也在这里'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
print(s3.summary(limit=4))
