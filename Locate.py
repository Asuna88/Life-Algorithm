#!/usr/bin/env python
# coding=utf-8
"""
进入序号Value目录
"""
import os
import Arg

path = ""
shell = ""
key = ""


# 定位序号
def locate_key(root):
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配每个文件夹
        match = Arg.match_key(each)
        while match:
            folder = Arg.get_key()
            if not folder == "":
                step_in_key(root, folder)
                match = match - 1
            # print(os.getcwd())


# 访问
def step_in(root, target):
    step_in_key(root, target)


# 访问key
def step_in_key(root, target):
    os.chdir(root)
    os.chdir(target)
    step_in_value(root + "/" + target)


# 访问value
def step_in_value(root):
    files = os.listdir(root)
    for each in files:
        if os.path.isdir(each):
            os.chdir(each)
            # 目录切换成功
            # print(os.getcwd())


def init():
    array = Arg.get_agr()
    print(array)
    if len(array) == 0:
        print(os.getcwd())
        return
    if not len(array) == 0:
        locate_key(os.getcwd())


#
if __name__ == "__main__":
    # 切换
    init()
