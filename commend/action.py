#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui, time
from default import color_check, write_log
from check import home_close


# 蹭铃铛
# wc: 共斗次数
# args['clock_x']，args['clock_y']: 铃铛位置
# args['clock_color_nomal']：铃铛正常颜色
# args['clock_color_action_l']，args['clock_color_action_h']：有铃铛时颜色，范围值
# args['join_x']，args['join_y']: e: 参加按钮
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
        g_cd = color_check(args['cancel_x'], args['cancel_y'])
        # print("g 位颜色：", g_cd)
        write_log(content="g 位颜色,x={}, y={} ：{}".format(
            args['cancel_x'], args['cancel_y'], g_cd))
        if g_cd == args["cancel_color_0"] or g_cd == args["cancel_color_0"]:
            pyautogui.press('g')
            print("发现 g 位颜色异常，不进入游戏~,x={}, y={}".format(
                args['cancel_x'], args['cancel_y']))
            write_log(content="发现 g 位颜色异常，不进入游戏~,x={}, y={}".format(
                args['cancel_x'], args['cancel_y']))
            # 点击 e 进入正常状态
            pyautogui.click(args['join_x'], args['join_y'], 2, 1.5)
            time.sleep(5)
        else:
            time.sleep(3)
            # 判断 e 点击参加，是否误操作，将自动铃铛关闭了
            e_cd = color_check(args['join_x'], args['join_y'])
            write_log(content='e 位置颜色为：{}'.format(e_cd))
            if e_cd == args['join_color_0'] or e_cd == args['join_color_1']:
                print("{}: e 位置异常，可能铃铛关闭，进行修复，{}, {} 位置颜色为：{}".format(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    args['join_x'], args['join_y'], e_cd))
                write_log(content="e 位置异常，可能铃铛关闭，进行修复，{}, {} 位置颜色为：{}".format(
                    args['join_x'], args['join_y'], e_cd))
                # 再点击 e ，开启铃铛
                pyautogui.click(args['join_x'], args['join_y'], 1)
                # 点击空白进入游戏
                pyautogui.click(args['click_none_x'], args['click_none_x'])
            time.sleep(1)
            # 准备队伍
            pyautogui.click(args['prepare_start_x'], args['prepare_start_y'])
            # 等待房间内刷完
            home_close(**args)
            # 点击继续，进入下一步，退出房间
            pyautogui.click(args['quit_x'], args['quit_x'], 8, 1)
            time.sleep(1)
            # 次数统计
            wc += 1
            print("auto game: {} 次成功".format(wc))
    elif a_cd == 222:
        write_log(content="没有铃铛,已经刷了 {} 次".format(wc))
    else:
        print("{} 铃铛异常，准备修复~".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        write_log(content="铃铛异常，准备修复~")
        Handling_exceptions(**args)

    return wc


# 异常处理
def Handling_exceptions(**args):
    # pyautogui.click(x=1371, y=22)
    time.sleep(1)
    # 点击主目录 尝试恢复
    pyautogui.click(args['main_x'], args['main_y'])
    # 点击 g, c 尝试恢复
    time.sleep(2)
    pyautogui.click(args['cancel_x'], args['cancel_y'])
    time.sleep(2)
    pyautogui.click(args['quit_x'], args['quit_y'])
    time.sleep(2)
    # 点击两次 f
    pyautogui.click(args['pl_x'], args['pl_y'], 2, 1.5)
    # 点击主目录 尝试恢复
    time.sleep(2)
    pyautogui.click(args['main_x'], args['main_y'])
    # 点击空白 尝试恢复 click_none_x
    pyautogui.click(args['click_none_x'], args['click_none_y'])
    pyautogui.click(args['quit_x'], args['quit_y'], 2, 1.5)

    content = "异常处理完成"

    return content
    