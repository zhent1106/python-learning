"""
按行读取文件
@Date 2020.05.08
"""
from collections import defaultdict
import re

# 正则，匹配单词
rec = re.compile(r'\s+')
# 统计单词出现的频次
dd = defaultdict(int)
# 读取文件 a.txt，r+表示读写默写
with open('./res/txt/test.txt', 'r+') as f:
    # 每次读取一行
    for line in f:
        clean_line = line.strip()
        if clean_line:
            # 正则分词
            words = rec.split(clean_line)
            # 遍历，统计
            for word in words:
                dd[word] += 1
# 按照频次降序排列
dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
print('---输出结果---')
print(dd)
