#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui
import os
import time


# 获取颜色
def color_check(x, y):
    # 获取颜色
    x, y = int(x), int(y)
    pix = pyautogui.pixel(x, y)
    _pix = pix[0]
    # ' Color: ' + str(pix[0])

    # 需要返回一个 string 类型，进行比较
    return str(_pix)


# 写日志
def write_log(path="log", file="main.log", content="", mod='a+'):
    file = os.path.join(path, file)
    # 添加时间
    content = time.strftime("%Y-%m-%d %H:%M:%S",
                            time.localtime()) + ": " + content + "\n"
    # 添加日志，做分析使用
    with open(file, mod, encoding='utf-8') as f:
        f.write(content)

    content = "Write file {}, Contennt: {}".format(file, content)

    return content
