#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import pyautogui
from default import color_check, write_log


# 房间检查
# con_x,con_y,con_c: 继续位置 x,y 坐标和颜色，如果多次 41，说明已经刷完
# bell_nomal: 没有铃铛的颜色，默认 222
# bell_un_0:铃铛异常状态 --> 有阴影，默认为：239
# bell_un_1:铃铛异常状态 --> 有阴影，默认为：231
# bell_x, bell_y:铃铛位置
def home_close(con_x,
               con_y,
               con_c,
               bell_x,
               bell_y,
               bell_nomal=222,
               bell_un_0=239,
               bell_un_1=231):
    # 游戏时间
    start_time = time.time()
    # 等待房间刷完
    print("进入房间开始游戏！")
    wc = 0
    # 控制检测次数
    nc = 0
    while True:
        # 3s 检查一次
        time.sleep(3)
        # 控制时间，如果超过一定时间也会 break
        c_d = color_check(con_x, con_y)
        # print("捕获继续位置颜色：{},{},{}".format(x, y, c_d))
        write_log(content="捕获继续位置颜色：{},{},{}".format(con_x, con_y, c_d))
        # 控制 41 像素连续
        if c_d == con_c:
            nc += 1
        else:
            nc = 0
        # 连续检测次数 3 次
        if nc >= 3:
            # print(c_d, "完成刷图~")
            write_log(content="{} 完成刷图~".format(c_d))
            break
        else:
            # print(c_d, "继续检查")
            write_log(content="继续检查".format(c_d))
        wc += 1
        # 过了 8min，还没有退出
        if wc >= 160:
            write_log(content="Game abnormal~")
            break
        else:
            pass
        # 60s 后检查如果铃铛正常，也退出
        # 铃铛颜色
        if wc >= 20:
            time.sleep(1)
            a_cd = color_check(x=bell_x, y=bell_y)
            # print("铃铛颜色:{}".format(a_cd))
            write_log(content="铃铛颜色:{}".format(a_cd))
            # 如果 2min 后，发现铃铛灰色，说明异常，退出房间。
            if a_cd == bell_nomal:
                break
            # 如果房间解散，直接点击 g 返回界面
            if a_cd == bell_un_0 or a_cd == bell_un_1:
                pyautogui.press('g')

        numb = "已经游戏 {} s".format(3 * wc)
        print(numb, end='')
        print('\b' * len(numb) * 2, end='', flush=True)

    print("完成刷图")
    write_log(content="完成刷图")
    print("--- cost {} seconds ---".format((time.time() - start_time)))
    write_log(content="--- cost {} seconds ---".format((time.time() -
                                                        start_time)))

