# -*- coding: utf-8 -*-
import os
from PIL import Image
import xlrd


def ResizeImage(filein, fileout, width, height, filetype):
    """
    filein: 输入图片
    fileout: 输出图片
    width: 输出图片宽度
    height:输出图片高度
    type:输出图片类型（png, gif, jpeg...）
    """
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(fileout, filetype)


def fuzhi文件夹(path1, path2):
    path_1 = os.listdir(path1)
    for i in path_1:
        i_patn = os.path.join(path1, i)
        if os.path.isdir(i_patn):
            path2.append()


def 读取文件(photo_path, all_file, all_file_name):
    '''
    :param photo_path: 文件路径
    :param all_file: 输出文件list
    :return: 遍历递归
    '''
    photo_list = os.listdir(photo_path)
    for photofile in photo_list:
        photo_ = os.path.join(photo_path, photofile)
        if os.path.isdir(photo_):
            读取文件(photo_, all_file, all_file_name)
        elif photo_[-4:] == '.jpg':
            all_file.append(photo_)
            all_file_name.append(photofile)
    return all_file, all_file_name


def ptu(img1path, img2path, outpath):
    '''
    :param img1path: 原图
    :param img2path: 覆盖在上面的图片
    :param outpath: 保存位置，需要建立子文件夹目录
    :return:改动之后，直接替换原文件
    兜兜转转，覆盖在原图上的图片有两张，路径都被写死了，本来想写成活动路径
    目前原图有不同的尺寸，先将尺寸统一
    '''
    outfile_dir, outfile_name = os.path.split(img1path)
    img1_1 = Image.open(img1path)
    img1 = img1_1.resize((1653, 2597), Image.ANTIALIAS)  # 重写图片尺寸
    img2 = Image.open(img2path)
    img2_2 = Image.open(r'D:/test/抠2.png')
    # newpath = outpath + '/' + outfile_dir[8:]
    newpath = outpath
    if os.path.isdir(newpath):
        print("路径存在")
        img1.paste(img2, (0, 1860))
        img1.paste(img2_2, (144, 2298))
        img1.save(newpath)
    else:
        # os.makedirs(newpath)
        print("路径不存在")
        img1.paste(img2, (0, 1860))
        img1.paste(img2_2, (144, 2298))
        img1.save(newpath)
        print(newpath)
        # 貌似是save方法会自动创建文件路径


if __name__ == '__main__':
    path1 = input()
    path = path1.replace('\\', '/')
    copyfile = r'D:/test/抠1.png'
    outpath = r'd:/test'
    xls_path = r'd:/test/文件名.xls'
    file_list, file_list_name = 读取文件(path, [], [])
    print(file_list)
    xlsfile = xlrd.open_workbook(xls_path)
    sheet = xlsfile.sheet_by_index(0)
    xls_list = []
    # 通过单元格获取数据
    xls_list = sheet.col_values(0, 0, sheet.nrows + 1)
    # 通过表格获取数据
    cell_value = sheet.cell_value(0, 0)

    for i in range(0, len(file_list_name), 1):
        if file_list_name[i] in xls_list:
            print('>>>>>>>>>>>>>')
            ptu(file_list[i], copyfile, file_list[i])
