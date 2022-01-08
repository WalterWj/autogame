#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import pyautogui

# 实时捕获鼠标位置和对应点的颜色

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        # 获取像素
        pix = pyautogui.pixel(int(str(x).rjust(4)), int(str(y).rjust(4)))
        # 获取位置
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' Color: ' + str(pix[0])
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

