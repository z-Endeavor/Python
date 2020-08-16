"""
在屏幕上显示跑马灯文字
"""

import os
import time


def main():
    content = 'Python真好玩！！'
    while True:
        # 清理屏幕的输出
        os.system('cls')
        print(content)
        # 休眠200ms
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
