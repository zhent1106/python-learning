"""
使用Pillow生成海报
"""

from PIL import Image, ImageDraw, ImageFont
import time


header = '001'
title = '想看会儿海'
books = ['中国史纲五十讲', '再见拖延症', '心流']
writes = ['日思录第001篇', 'python给图片加文字']
summary = '今晚晚风独美'
n = 18
summary_list = [summary[i:i + n] for i in range(0, len(summary), n)]

# 背景图
img = './res/img/zhent.jpg'
# 生成的图片
new_img = './res/img/pillowWall.jpg'
# 压缩后的图片
compress_img = './res/pillowWallCompress.jpg'

# 设置字体样式
font_type = './res/fonts/SimHei.ttf'
font_medium_type = './res/fonts/SimHei.ttf'
header_font = ImageFont.truetype(
    './res/fonts/SimHei.ttf', 80, encoding='utf-8')
title_font = ImageFont.truetype(
    './res/fonts/SimHei.ttf', 60, encoding='utf-8')
font = ImageFont.truetype(font_type, 60)
color = '#000000'

# 打开图片
image = Image.open(img)
draw = ImageDraw.Draw(image)
width, height = image.size

# header 头
header_x = 100
header_y = 1300
draw.text((header_x, height - header_y), u'%s' % header, color, header_font)

# 标题
title_x = header_x
title_y = header_y - 100
draw.text((title_x, height - title_y), u'%s' % title, color, title_font)

# 当前时间
cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
cur_time_x = 900
cur_time_y = title_y - 5
cur_time_font = ImageFont.truetype(font_type, 70)
draw.text((cur_time_x, height - cur_time_y), u'%s' %
          cur_time, color, cur_time_font)

# 阅读
book_x = title_x + 10
book_start_y = title_y - 200
book_y = 0
book_line = 100
for num, book in enumerate(books):
    y = book_start_y - num * book_line
    book_num = num + 1
    draw.text((book_x, height - y), u'%s. %s' % (book_num, book), color, font)

# 写作
write_x = book_x
write_y = title_y - 600
write_line = 80

for num, write in enumerate(writes):
    write_num = num + 1
    y = write_y - num * write_line
    draw.text((write_x, height - y), u'%s. %s' %
              (write_num, write), color, font)

# 哲思
summary_x = book_x + 800
summary_y = book_start_y
summary_line = 80
for num, summary in enumerate(summary_list):
    y = summary_y - num * summary_line
    draw.text((summary_x, height - y), u'%s' % summary, color, font)

# 生成图片
image.save(new_img, 'png')

# 压缩图片
sImg = Image.open(new_img)
w, h = sImg.size
width = int(w / 2)
height = int(h / 2)
dImg = sImg.resize((width, height), Image.ANTIALIAS)
dImg.save(compress_img)
