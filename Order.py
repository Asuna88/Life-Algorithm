#!/usr/bin/env python
# coding=utf-8
import os
import re
import Key
import Locate

path = ""
shell = ""
key = ""


# 根据文件路径计算序号
def get_sequence(root):
    global key
    levels = root.split("/")
    for each in levels:
        match = re.compile(r'^[0-9]&').match(each)
        if not match:
            continue
        if key == "":
            key = each
            continue
        if not key == "":
            key = key + "." + each
            continue
    return key


# 生成别名
def get_alias(root):
    global path
    global shell
    path = root
    name = os.path.basename(root)
    shell = "ln -s " + path + " " + key + "_" + name
    print(shell)
    # print_list(path)


# 打印所有子目录
def print_list(root):
    # dirs 文件夹
    # files 文件
    for root, dirs, files in os.walk(root):
        for each in dirs:
            # 匹配每个文件夹
            match = Key.match_pattern(each)
            if match:
                Locate.step_in(root, each)
                # print(os.getcwd())
                os.chdir(root)


#
if __name__ == "__main__":
    # 切换
    Locate.init()
    # print(os.getcwd())
    # 所有
    print_list(os.getcwd())
