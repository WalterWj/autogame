#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import argparse
from configparser import ConfigParser
# 加载自定义函数
from commend.default import write_log
from commend.action import Bells_fighting


def main():
    args = parse_args()
    # 清理日志
    write_log(content="清空日志", mod='w+')
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Wait 1s start!")
    time.sleep(1)
    print("Ctrl + c 可以退出脚本~")
    print("{}: 开始游戏".format(local_time))
    write_log(content="=======================开始游戏=======================")
    # 游戏模式
    mode = args.mode
    # 循环次数
    wc = 0
    # 配置项
    cfg = ConfigParser()
    cfg.read(args.config)
    main_config = dict(cfg.items("main"))
    while True:
        if mode == "main":
            wc = Bells_fighting(wc,**main_config)
        else:
            print("请输入 [''/pl/gd]~ ")
            break

        # 6s 循环检查铃铛变化
        time.sleep(6)

        

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
                        default="main")

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()