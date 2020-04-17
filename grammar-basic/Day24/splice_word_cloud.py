"""
导入词云制作库wordcloud和中文分词jieba
"""
import jieba
import wordcloud
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='#eeeeee', font_path='./res/fonts/SimHei.ttf')


# 调用jieba的cut()方法对原始文本进行中文分词，得到string
txt = 'Python是一种广泛使用的解释型、高级编程、通用型编程语言，由吉多·范罗苏姆创造，第一版发布于1991年。可以视之为一种改良的LISP。Python的设计哲学强调代码的可读性和简洁的语法。相比于C++或Java，Python让开发者能够用更少的代码表达想法。不管是小型还是大型程序，该语言都试图让程序的结构清晰明了'
txtlist = jieba.lcut(txt)
string = "".join(txtlist)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('./res/img/output3.png')
