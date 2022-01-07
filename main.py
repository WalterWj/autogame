#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import argparse
import os
# import pyautogui
import sys
from configparser import ConfigParser

# cfg = ConfigParser()
# cfg.read('config.ini')
# # 获取 string 类型
# clock = cfg.get('main', 'clock')
# print(clock)
# # 获取 int 类型
# clock = cfg.getint('main', 'clock_color')
# print(clock)

def main():
    args = parse_args()
    # 游戏模式
    mode = args.mode
    # 配置项
    cfg = ConfigParser()
    cfg.read(args.config)
        

def parse_args():
    # Incoming parameters
    parser = argparse.ArgumentParser(description="autogame for World Flipper")
    parser.add_argument("--config",
                        dest="config",
                        help="Play game's config",
                        default="config.ini")
    parser.add_argument("-m",
                        dest="mode",
                        help="Play game's mode",
                        default="pl")

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()