#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui, os, time


# 获取颜色
def color_check(x, y):
    # 获取颜色
    pix = pyautogui.pixel(x, y)
    _pix = pix[0]
    # ' Color: ' + str(pix[0])

    return _pix


# 写日志
def write_log(file="main.log", content="", mod='a+'):
    file = os.path.join("log", file)
    # 添加时间
    content = time.strftime("%Y-%m-%d %H:%M:%S",
                            time.localtime()) + ": " + content + "\n"
    # 添加日志，做分析使用
    with open(file, mod, encoding='utf-8') as f:
        f.write(content)

    content = "Write file {}, Contennt: {}".format(file, content)

    return content


def ConOrQuit(click_x, click_y, while_num=8):
    numc = 0
    while numc <= while_num:
        numc += 1
        time.sleep(1.5)
        pyautogui.click(x=click_x, y=click_y)

    content = "点击 x:{},y:{} {} 次, 耗时 {}s".format(click_x, click_y, while_num,
                                                 while_num * 1.5)

    return content

