"""
跑马灯文字
"""

import os
import time


def main():
    content = '你眸海温涟，藏山高水远，我的人间。'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:]+content[0]


if __name__ == '__main__':
    main()
