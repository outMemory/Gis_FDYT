# -*- coding: utf-8 -*-
import os, shutil, sys

if __name__ == '__main__':
    print("输入文件所在位置")
    path_wenjian = input().replace('\\', '/') or 'D:/test/0-9/新建文件夹'
    print("输入文件夹所在位置")
    path_wenjianjia = input().replace('\\', '/') or 'D:/test/0-9/新建文件夹 (2)'
    wenjianweizhi = os.listdir(path_wenjian)

    for ii in wenjianweizhi:
        name_ii = ii.split('_')[0]
        if os.path.isdir(path_wenjianjia + '/' + name_ii):
            shutil.copy(path_wenjian + '/' + ii, path_wenjianjia + '/' + name_ii + '/不动产单元图')
            print("正在复制", ii)
        else:
            print(path_wenjianjia + '/' + name_ii + '/不动产单元图')
            input('找不到对应文件夹，回车退出')
            sys.exit(0)
