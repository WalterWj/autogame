#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyautogui
import time
from default import color_check, write_log, click_num
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
    # 铃铛下面的颜色
    a_cd_below = color_check(args['clock_below_x'], args['clock_below_y'])
    # print("铃铛颜色:{}".format(a_cd))
    write_log(content="铃铛颜色:{}".format(a_cd), **args)
    # if a_cd != args['clock_color_nomal'] and args[
    #         'clock_color_action_l'] <= a_cd <= args['clock_color_action_h']:
    if a_cd != args['clock_color_nomal'] and a_cd_below == args[
            'clock_below_color_nomal']:
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 点击铃铛进入房间
        pyautogui.click(x=args['clock_x'], y=args['clock_y'])
        # pyautogui.press('a')
        print("{} 开始第 {} 次游戏！".format(local_time, wc + 1))
        write_log(content="开始第 {} 次游戏！".format(wc + 1), **args)
        time.sleep(1)
        # 点击参加 -- e
        # pyautogui.press('e')
        pyautogui.click(x=args['join_x'], y=args['join_y'])
        time.sleep(3)
        # 查看 g 点位置，判断是否异常
        # 如果判断 g 位置异常，认为进入游戏失败，退出循环，开始下一局
        g_cd = color_check(args['cancel_x'], args['cancel_y'])
        # print("g 位颜色：", g_cd)
        write_log(content="g 位颜色,x={}, y={} ：{}".format(
            args['cancel_x'], args['cancel_y'], g_cd),
                  **args)
        if g_cd == args["cancel_color_0"] or g_cd == args[
                "cancel_color_1"] or g_cd == args["cancel_color_2"]:
            pyautogui.click(args['cancel_x'], args['cancel_y'])
            print("发现 g 位颜色异常，不进入游戏~,x={}, y={}".format(
                args['cancel_x'], args['cancel_y']))
            write_log(content="发现 g 位颜色异常，不进入游戏~,x={}, y={}".format(
                args['cancel_x'], args['cancel_y']),
                      **args)
            # 点击 e 进入正常状态
            click_num(args['join_x'], args['join_y'], 1)
            time.sleep(5)
        else:
            time.sleep(3)
            # 判断 e 点击参加，是否误操作，将自动铃铛关闭了
            e_cd = color_check(args['join_x'], args['join_y'])
            write_log(content='e 位置颜色为：{}'.format(e_cd), **args)
            if e_cd == args['join_color_0'] or e_cd == args['join_color_1']:
                print("{}: e 位置异常，可能铃铛关闭，进行修复，{}, {} 位置颜色为：{}".format(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    args['join_x'], args['join_y'], e_cd))
                write_log(content="e 位置异常，可能铃铛关闭，进行修复，{}, {} 位置颜色为：{}".format(
                    args['join_x'], args['join_y'], e_cd),
                          **args)
                # 再点击 e ，开启铃铛
                pyautogui.click(args['join_x'], args['join_y'])
                time.sleep(1)
                # 点击空白进入游戏
                pyautogui.click(args['click_none_x'], args['click_none_y'])
            time.sleep(1)
            # 准备队伍
            pyautogui.click(args['prepare_start_x'], args['prepare_start_y'])
            # 等待房间内刷完
            _time = home_close(**args)
            print("刷图耗时: {}s~".format(_time))
            time.sleep(3)
            # 点击 8 次退出，退出房间
            click_num(args['quit_x'], args['quit_y'], 8)
            time.sleep(1)
            # 点击一次主目录
            click_num(args['main_x'], args['main_y'], 1)
            # 次数统计
            wc += 1
            print("auto game: {} 次成功".format(wc))
    elif a_cd == args['clock_color_nomal']:
        write_log(content="没有铃铛,已经刷了 {} 次".format(wc), **args)
    elif a_cd == args['clock_color_action_l'] and a_cd_below != args[
            'clock_below_color_nomal']:
        pass
        # pyautogui.click(args['continue_x'], args['continue_y'])
    else:
        print("{} 铃铛异常，准备修复~".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        write_log(content="铃铛异常，准备修复~", **args)
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
    # pyautogui.click(args['pl_x'], args['pl_y'], 2, 2)
    # 点击主目录 尝试恢复
    time.sleep(2)
    pyautogui.click(args['main_x'], args['main_y'])
    # 点击空白 尝试恢复 click_none_x
    pyautogui.click(args['click_none_x'], args['click_none_y'])
    click_num(args['quit_x'], args['quit_y'], 2, 2)
    # 点击退出或者主目录
    click_num(args['exit_x'], args['exit_y'], 2, 2)

    content = "异常处理完成"

    return content


# 共斗


def Fight_together(wc, **args):
    # 控制循环次数，如果一直没有成功，则退出
    _nc = 0
    # 如果铃铛为 222，说明在房间内
    bill_color = color_check(args['clock_x'], args['clock_y'])
    write_log(content="第 {} 次捕获铃铛颜色: {},{}: {}".format(_nc, args['clock_x'],
                                                       args['clock_y'],
                                                       bill_color),
              **args)
    # 铃铛下面位置颜色
    bill_below_color = color_check(args['clock_below_x'],
                                   args['clock_below_y'])
    write_log(content="第 {} 次捕获铃铛颜下面色: {},{}: {}".format(
        _nc, args['clock_below_x'], args['clock_below_y'], bill_below_color),
              **args)
    # 初始化 result 结果
    result = True
    if bill_color != args['clock_color_nomal'] and bill_below_color == args[
            'clock_below_color_nomal']:
        result = False
    else:
        while bill_color == args['clock_color_nomal']:
            # 循环点击 b, d，开始共斗
            pyautogui.click(args['prepare_start_x'], args['prepare_start_y'])
            time.sleep(1)
            pyautogui.click(args['continue_x'], args['continue_y'])
            if _nc <= 20:
                result = True
            else:
                result = False
                break
            # 重新获取铃铛颜色
            time.sleep(3)
            bill_color = color_check(args['clock_x'], args['clock_y'])
            _nc += 1
            write_log(content="第 {} 次捕获铃铛颜色: {},{}: {}".format(
                _nc, args['clock_x'], args['clock_y'], bill_color),
                      **args)

    # 当正常进入房间后，开始共斗
    if result:
        _time = home_close(**args)
        print("刷图耗时：{}~".format(_time))

        # 刷完之后，点击 b 返回房间
        b_d_nc = 0
        while b_d_nc < 8:
            pyautogui.click(args['continue_x'], args['continue_y'])
            time.sleep(2)
            pyautogui.click(args['prepare_start_x'], args['prepare_start_y'])
            b_d_nc += 1

        wc += 1

    return wc, result


def Clean_pl(wc, **args):
    _bool = True
    # 清理体力，循环共斗
    # 1. 点击 F 开始刷图
    print("开始第 {} 次刷图,清理 Pl~".format(wc + 1))
    write_log(content="开始第 {} 次刷图,清理 Pl~".format(wc + 1), **args)
    pyautogui.click(args['pl_x'], args['pl_y'])
    time.sleep(3)
    f_cd = color_check(args['pl_x'], args['pl_y'])
    # print("f {},{} 位置颜色为：{}".format(args['pl_x'], args['pl_y'], f_cd))
    write_log(content="f {},{} 位置颜色为：{}".format(args['pl_x'], args['pl_y'],
                                                f_cd),
              **args)
    if f_cd == args['pl_color_red']:
        print("疲劳已经刷完, 开始摇铃铛~")
        # 取消刷房间，点f
        pyautogui.click(args['pl_x'], args['pl_y'])
        time.sleep(1)
        # 退出房间
        pyautogui.click(args['exit_x'], args['exit_y'])
        time.sleep(2)
        # 返回主界面 quit_x
        pyautogui.click(args['quit_x'], args['quit_y'])
        # 返回 False 值，如果是，则使用
        _bool = False
    else:
        # 2. 判断如果刷完，点击 b 进行重新刷图，跳回 1
        # 切换到模拟器
        time.sleep(2)
        # 等待房间内刷完
        home_close(**args)
        time.sleep(5)
        # 点击 b 重复, 重新进入房间
        click_num(args['continue_x'], args['continue_y'], 5, 2)
        wc += 1
        print("已经刷了 {} 次！".format(wc))

    return wc, _bool
