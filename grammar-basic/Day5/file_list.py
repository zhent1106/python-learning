"""
判断一组文件中图片的个数
"""


def count_image(file_list):
    """
    判断一组文件中图片的个数
    ：param file_list：文件列表
    ：return ：图片文件数量
    """
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') or \
                file.endswith('webp') or file.endswith('bmp'):
            count = count+1
    return count

# 调用函数


img_list = ['1.png', '2.jpg', '3.gif', '4.webp', '5.bmp', '6.mp4']
result = count_image(img_list)
print('一共有', result, '个图片格式文件')
