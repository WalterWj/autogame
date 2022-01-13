#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 将 commend 加入
import os
import sys
currrent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(currrent_dir, "commend"))

# 加载自定义函数
from commend.action import Bells_fighting, Fight_together, Clean_pl
from commend.default import write_log, parser_set

import argparse
import time


def main():
    args = parse_args()
    # 游戏模式
    mode = args.mode
    # 循环次数
    wc = 0
    # 配置项初始化
    main_config, log_config, config = parser_set(args.config, args.distance)

    # 清理日志
    write_log(content="清空日志", mod='w+', **log_config)
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Wait 1s start!")
    time.sleep(1)
    print("Ctrl + c 可以退出脚本~")
    print("{}: 开始游戏".format(local_time))
    write_log(content="=======================开始游戏=======================", **log_config)

    while True:
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if mode == "main":
            print("{} 开始摇铃铛~".format(local_time), end='')
            print('\b' * len("{} 开始摇铃铛~".format(local_time)) * 2, end='', flush=True)
            wc = Bells_fighting(wc, **config)
        elif mode == "gd":
            print("开始共斗~", end='')
            print('\b' * len("开始共斗~") * 2, end='', flush=True)
            wc, result = Fight_together(wc, **config)
            if result:
                pass
            else:
                mode = "main"
        elif mode == "pl":
            print("开始清理疲劳~", end='')
            print('\b' * len("开始清理疲劳~") * 2, end='', flush=True)
            wc, result = Clean_pl(wc, **config)
            if result:
                pass
            else:
                mode = "main"
        else:
            print("请输入 [''/gd/pl]~ ")
            break

        # 6s 循环检查铃铛变化
        time.sleep(4)


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
    parser.add_argument("-d",
                        dest="distance",
                        help="Play game's num",
                        default=0)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
