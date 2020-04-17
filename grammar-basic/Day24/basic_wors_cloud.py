"""
基础词云

"""
import wordcloud
import random
# 创建词韵
w = wordcloud.WordCloud()
# 生成字符串生成词云
w.generate(' Donnot forget, you are stars. When the stars exploded  in the universe hundreds of millions of years ago,everything in this world formed. Everything we know is stardust')
# 生成本地图片
w.to_file('./res/img/output1.png')


# 创建词云对象，设置次云照片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='#eeeeee', font_path='./res/fonts/SimHei.ttf')
w.generate('别忘了, 你们是星星。当群星几亿年前在宇宙间爆炸时, 形成了这世界上的一切。我们所知道的一切都是星尘。')
w.to_file('./res/img/output2.png')
