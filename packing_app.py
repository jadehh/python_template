#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : packing_app.py.py
# @Author   : jade
# @Date     : 2021/11/27 14:25
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from jade import *

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    if getOperationSystem() == "Windows":
        parser.add_argument('--extra_sys_str', type=str,
                            default="")  ## 添加环境变量
        parser.add_argument('--extra_path_list', type=list,
                            default="")  ## 添加到exec打包路径
    else:
        parser.add_argument('--extra_sys_str', type=str,
                            default="")       ## 添加环境变量
        parser.add_argument('--extra_path_list', type=list,
                            default="")  ## 添加到exec打包路径
    parser.add_argument("--head_str",type=str,default="")
    parser.add_argument('--full', type=str,
                        default="True")  ## 打包成一个完成的包
    parser.add_argument("--use_jade_log",type=str,default="True")
    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效
    parser.add_argument('--app_version', type=str,
                        default=get_app_version())  ##需要打包的文件名称
    parser.add_argument('--app_name', type=str,
                        default="conta_service")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="箱号服务")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="False")  ## 是否打包成AppImage
    parser.add_argument('--is_qt', type=str, default="False")  ## 是否为Qt
    parser.add_argument("--specify_files",type=str,default="")
    parser.add_argument('--lib_path', type=str, default="conta_service_lib64")  ## 是否lib包分开打包

    args = parser.parse_args()
    # writePy(args)
    build(args)
    packAPP(args)
    zip_lib_package(args)


