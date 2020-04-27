"""
Myqr制作二维码
    """
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont


def img_code():
    myqr.run(words='https://niit-student.oss-cn-beijing.aliyuncs.com/markdown/lALPGojJ7-6xtcvNAS7NAXw_380_302.png',
             version=1,
             level='H',
             picture='./res/img/bluetian.jpg',
             colorized=True,
             contrast=1.0,
             brightness=1.0,
             save_name='code2.png',
             save_dir=os.getcwd() + '/res/img/')


def draw():
    img = Image.open('./res/img/code2.png')
    w, h = img.size
    txt = '想看会儿海'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/fonts/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/img/code3.png')


if __name__ == '__main__':
    img_code()
    draw()
