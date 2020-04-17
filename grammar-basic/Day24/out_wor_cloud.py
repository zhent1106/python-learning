"""
外部文本词云
"""
import wordcloud
import random

f = open('./res/txt/想看会儿海.txt', encoding='utf-8')
txt = f.read()

# 更换背景颜色和整体风格
w = wordcloud.WordCloud(scale=2, max_font_size=100,
                        background_color='#383838', colormap='PuRd', font_path='./res/fonts/SimHei.ttf')

# 将txt变量传入

w.generate(txt)
w.to_file('./res/img/output4.png')
