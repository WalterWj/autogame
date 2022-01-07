#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui, time
from default import *
from check import home_close

# 异常处理


# 蹭铃铛
# wc: 共斗次数
def Bells_fighting(wc, **args):
    # 铃铛颜色
    a_cd = color_check(x=args['clock_x'], y=args['clock_y'])
    # print("铃铛颜色:{}".format(a_cd))
    write_log(content="铃铛颜色:{}".format(a_cd))
    if a_cd != args['clock_color_nomal'] and args[
            'clock_color_action_l'] <= a_cd <= args['clock_color_action_h']:
        # 点击铃铛进入房间
        pyautogui.click(x=args['clock_x'], y=args['clock_y'])
        # pyautogui.press('a')
        print("开始第 {} 次游戏！".format(wc + 1))
        write_log(content="开始第 {} 次游戏！".format(wc + 1))
        time.sleep(1)
        # 点击参加 -- e
        # pyautogui.press('e')
        pyautogui.click(x=args['join_x'], y=args['join_y'])
        time.sleep(2)
        # 查看 g 点位置，判断是否异常
        # 如果判断 g 位置异常，认为进入游戏失败，退出循环，开始下一局
        g_cd = color_check(x=1602, y=682)
        # print("g 位颜色：", g_cd)
        write_log(content="g 位颜色,x=1602, y=682：{}".format(g_cd))
        if g_cd == 24 or g_cd == 41:
            pyautogui.press('g')
            print("发现 g 位颜色异常，不进入游戏~,x=1602, y=682")
            write_log(content="发现 g 位颜色异常，不进入游戏~,x=1602, y=682")
            # 点击 e 进入正常状态
            time.sleep(1)
            pyautogui.press('e')
            time.sleep(2)
            pyautogui.press('e')
            time.sleep(10)
        else:
            # time.sleep(1)
            # 点击参加 -- e
            # pyautogui.press('e')
            # 点击空白处 防止意外
            # pyautogui.click(1878, y=822)
            time.sleep(2)
            # 避免进入房间查看奖励，点击 f 关闭
            # pyautogui.press('f')
            # time.sleep(1)
            # 判断 e 点击参加，是否误操作，将自动铃铛关闭了
            e_cd = color_check(1725, 889)
            write_log(content='e 位置颜色为：{}'.format(e_cd))
            if e_cd == 74 or e_cd == 66:
                print("{}: e 位置异常，可能铃铛关闭，进行修复，1725, 889 位置颜色为：{}".format(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    e_cd))
                write_log(content="e 位置异常，可能铃铛关闭，进行修复，1725, 889 位置颜色为：{}".
                          format(e_cd))
                # 再点击 e ，开启铃铛
                pyautogui.press('e')
                # 点击空白进入游戏
                pyautogui.click(x=1878, y=822)
            time.sleep(1)
            # 准备队伍
            pyautogui.press('d')
            # 等待房间内刷完
            home_close(x=1542, y=957)
            # 切换到模拟器
            pyautogui.click(x=1371, y=22)
            # 点击继续，进入下一步
            _nc = 0
            while _nc <= 8:
                pyautogui.press('c')
                time.sleep(1)
                _nc += 1
            # pyautogui.press('c')
            # time.sleep(2)
            # pyautogui.press('c')
            # # 过 7s 动画 -- c （异常下点击 g）
            # time.sleep(7)
            # pyautogui.press('c')
            # 如果异常下点击 g
            # 查看 g 点位置，判断是否异常
            # 如果判断 g 位置异常，认为进入游戏失败，退出循环，开始下一局
            time.sleep(1)
            g_cd = color_check(x=1602, y=682)
            write_log(content="g 位颜色：{}".format(g_cd))
            if 410 <= g_cd <= 420:
                time.sleep(3)
                pyautogui.press('g')
                print("g 位颜色：{}, 发现异常，点击 g".format(g_cd))
                write_log(content="g 位颜色：{}, 发现异常，点击 g".format(g_cd))
            # 离开房间 -- c
            time.sleep(4)
            wc += 1
            pyautogui.press('c')
            time.sleep(1.5)
            pyautogui.press('c')
            print("auto game: {} 次成功".format(wc))
    elif a_cd == 222:
        # print("没有铃铛,已经刷了 {} 次".format(wc))
        write_log(content="没有铃铛,已经刷了 {} 次".format(wc))
    else:
        print("{} 铃铛异常，准备修复~".format(local_time))
        write_log(content="铃铛异常，准备修复~")
        pyautogui.click(x=1371, y=22)
        time.sleep(1)
        # 点击主目录 尝试恢复
        pyautogui.click(x=1466, y=978)
        # 点击 g, c 尝试恢复
        time.sleep(2)
        pyautogui.press('g')
        time.sleep(2)
        pyautogui.press('c')
        time.sleep(2)
        pyautogui.press('f')
        pyautogui.press('f')
        # 点击主目录 尝试恢复
        time.sleep(2)
        pyautogui.click(x=1466, y=978)
        # 点击空白 尝试恢复
        pyautogui.click(x=1835, y=822)
        pyautogui.press('c')
        pyautogui.press('c')

    return wc
