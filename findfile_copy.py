# -*- coding: utf-8 -*-
import os, sys, xlrd, shutil


def filereader_list(photo_path, all_file, all_file_name):
    '''
    :param all_file_name: 输出文件名字的列表
    :param photo_path: 文件路径
    :param all_file: 输出文件路径的列表
    :return: 遍历递归
    '''
    photo_list = os.listdir(photo_path)
    for photofile in photo_list:
        photo_ = os.path.join(photo_path, photofile)
        if os.path.isdir(photo_):
            filereader_list(photo_, all_file, all_file_name)
        elif photo_[-4:] == '.jpg':
            all_file.append(photo_)
            all_file_name.append(photofile)
    return all_file, all_file_name


def xlsreader(path_xls):
    xlsfile = xlrd.open_workbook(path_xls)
    sheet = xlsfile.sheet_by_index(0)
    xls_list = sheet.col_values(0, 0, sheet.nrows + 1)
    if not sheet.cell_type(0, 0) == 1:
        print('请将单元格格式改为文本')
    return xls_list


if __name__ == '__main__':
    xls = input('输入excel文件位置').replace('\\', '/') or 'D:/test/xlsx模板/1.xls'
    filepath = input('查找文件的范围').replace('\\', '/') or 'D:/test/wenjian'
    outfile = input('保存位置').replace('\\', '/') or 'D:/test/0-9'
    if not os.path.isdir(outfile):
        print('路径不存在', outfile)
    list_xls = xlsreader(xls)
    list_filelujin, list_filename = filereader_list(filepath, [], [])
    print(list_filename, list_filelujin)
    oldfile = ''
    for ii in list_xls:
        i = str(ii) + '_FWPMT.jpg'
        print(i)
        if i in list_filename:
            oldfile = list_filelujin[list_filename.index(i)]
            newfile = outfile + '/' + i
            shutil.copy(oldfile, newfile)
        else:
            print('找不到该文件', i)
    input('回车退出')
    sys.exit(0)
