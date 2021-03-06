#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui
import os
import time
from configparser import ConfigParser

# 获取颜色
def color_check(x, y):
    # 获取颜色
    pix = pyautogui.pixel(x, y)
    _pix = pix[0]
    # ' Color: ' + str(pix[0])

    # 需要返回一个 string 类型，进行比较
    return _pix


# 写日志
def write_log(content="", mod='a+', **args):
    file = os.path.join(args['logpath'], args['logfile'])
    # 添加时间
    content = time.strftime("%Y-%m-%d %H:%M:%S",
                            time.localtime()) + ": " + content + "\n"
    # 添加日志，做分析使用
    with open(file, mod, encoding='utf-8') as f:
        f.write(content)

    content = "Write file {}, Contennt: {}".format(args['logfile'], content)

    return content

# 初始化配置文件内容
def config_set(config, distance=0):
    for key in config:
        try:
            # key 以 _x 结尾需要处理
            if key.endswith('_x'):
                config[key] = int(config[key]) - int(distance) * 593
            else:
                config[key] = int(config[key])
        except ValueError:
            config[key] = eval(config[key])

    return config

# 循环点击一个位置
def click_num(x, y, num=8, duration=1):
    _num = 0
    while _num < num:
        pyautogui.click(x, y)
        time.sleep(duration)
        _num += 1

    content = "执行成功:{},{} {} 次".format(x, y, num)

    return content

# 初始化参数
def parser_set(config_file="config.ini", distance=0):
    cfg = ConfigParser()
    cfg.read(config_file, encoding='utf-8')
    main_config = dict(cfg.items("main"))
    main_config = config_set(main_config, distance)
    log_config = config_set(dict(cfg.items("log")))
    # 配置日志名
    log_config["logfile"] = "{}{}".format(log_config["logfile"], distance)
    config = {**main_config, **log_config}

    return main_config, log_config, config
