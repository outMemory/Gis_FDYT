# -*- coding: utf-8 -*-
import os
import sys
import xlrd

from PIL import Image


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


def fuzhiwenjianjia(path1, path2):
    path_1 = os.listdir(path1)
    for i in path_1:
        i_patn = os.path.join(path1, i)
        if os.path.isdir(i_patn):
            path2.append()


def duquwenjian(photo_path, all_file, all_file_name, guolv):
    """
    :param guolv: 增加一个按照特定字符过滤列表的功能
    :param all_file_name: 输出所有文件的名字
    :param photo_path: 文件路径
    :param all_file: 输出文件list
    :return: 遍历递归
    """
    photo_list = os.listdir(photo_path)
    numb_1 = 1
    for photofile in photo_list:
        photo_ = os.path.join(photo_path, photofile)
        if os.path.isdir(photo_):
            duquwenjian(photo_, all_file, all_file_name, guolv)
        elif photo_[-4:] == '.jpg' and photofile[-9:-4] == guolv:
            all_file.append(photo_)
            all_file_name.append(photofile)
            print('正在读取文件，第', numb_1)
        numb_1 += 1
    # print(all_file_name, all_file)
    # input('dengdai')
    # sys.exit(0)
    return all_file, all_file_name


def ptu(img1path, img2path, outpath):
    """
    :param img1path: 原图
    :param img2path: 覆盖在上面的图片
    :param outpath: 保存位置，需要建立子文件夹目录
    :return:改动之后，直接替换原文件
    """
    img1 = Image.open(img1path)
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


def joinjpg(png1, png2, result):
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size  # 获取两张图片的大小
    joint = Image.new('RGB', (size1[0] + size2[0], size2[1]))
    loc1, loc2 = (0, 0), (size1[0], 0)
    joint.paste(img2, loc2)
    joint.paste(img1, loc1)
    # 因为需要让第一张图片放置在图层的最上面,所以让第一张图片最后最后附着上图片上
    joint.save(result)


def start(items, result, first_path=None):
    # 当first为None时,默认将第一张图片设置为图片列表的第一张图片,第二张图片设置为图片列表的第二张
    # 当这两张图片合成后，将图片列表的已经合成的图片元素移除
    # 然后将合成的图片设置为第一张图片,将剩余的没有合成的图片列表继续操作
    # 当first_path不为None,将第一张图片设置为first_path，第二张图片设置为传进来的列表的第一个元素
    # 合成之后，将刚刚使用的列表的元素删除
    # 最后递归函数，知道列表为空
    try:
        if not first_path:
            path1, path2 = items[0], items[1]
            joinjpg(path1, path2, result)
            items.remove(path1)
            items.remove(path2)
            return start(items, result, first_path=result)
        else:
            path2 = items[0]
            joinjpg(first_path, path2, result)
            items.remove(path2)
            return start(items, result, first_path=result)
    except:
        pass


def pingjietupian_list(mianji, list_muban):
    """
    将要拼接的图片找到，并返回路径列表
    :param list_muban:照片路径的模板，从里面提取
    :param mianji: 面积
    :return:返回的是图片路径，下一步进行拼接
    """
    list_muban_lujin = []  # 返回一个列表储存照片路径
    list_shuzi = ['0', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # numb_fwpmt = ['D:/test/房屋平面图模板/0.jpg', 'D:/test/房屋平面图模板/00.jpg', 'D:/test/房屋平面图模板/1.jpg', 'D:/test/房屋平面图模板/2.jpg',
    #               'D:/test/房屋平面图模板/3.jpg', 'D:/test/房屋平面图模板/4.jpg', 'D:/test/房屋平面图模板/5.jpg', 'D:/test/房屋平面图模板/6.jpg',
    #               'D:/test/房屋平面图模板/7.jpg', 'D:/test/房屋平面图模板/8.jpg', 'D:/test/房屋平面图模板/9.jpg']
    mianji_str = str(mianji)
    mianji_list = list(mianji_str)
    for ii1 in mianji_list:
        list_muban_lujin.append(list_muban[list_shuzi.index(ii1)])
    return list_muban_lujin


def duquxlsx(path_1):
    path_3 = ''
    path_2 = os.listdir(path_1)
    for II in path_2:
        print(II)
        if II[-5:] == '.xlsx':
            path_3 = path_1 + '/' + II
        else:
            print('文件夹中没有xlsx文件')
            input()
            sys.exit(0)
    return path_3


def pt_1(path_1, fenzhi):
    """
    做成模块，优化结构，分支控制两种不同的图，
    :param path_1:
    :param fenzhi: 只能填两个值
    :return:
    """
    result = ''
    path_save = 'D:/'

    if fenzhi == 'fwpmt':
        lujin_fwpmt, name_fwpmt = duquwenjian(path_1, [], [], 'FWPMT')
        result = 'D:/test/房屋平面图面积.jpg'
        path_save = 'D:/test/修改后的房屋平面图'
    elif fenzhi == 'zdt':
        lujin_fwpmt, name_fwpmt = duquwenjian(path_1, [], [], 'ZDT_表')
        result = 'D:/test/宗地图面积.jpg'
        path_save = 'D:/test/修改后的宗地图'
    else:
        print('程序意外终止，请按回车推出程序，分支超限')
        input()
        sys.exit(0)

    if not os.path.isdir('D:/'):
        print('系统没有d盘，程序终止，请按回车退出程序')
        input()
        sys.exit(0)

    if not os.path.isdir(path_save):
        os.makedirs(path_save)  # 保证路径存在
    numb = 1
    for ii in name_fwpmt:
        try:
            if fenzhi == 'fwpmt':
                numb_maji = JZMJ_list[ZDDM_list.index(ii[:-10])]  # 找到jpg文件中的编号在宗地代码列表中顺序，在找到这个位置的宗地面积
                ii_lujin = lujin_fwpmt[name_fwpmt.index(ii)]
                start(pingjietupian_list(numb_maji, numb_fwpmt), result)
                image_result = Image.open(result)
                image_fugai = Image.open('D:/test/房屋平面图模板/k.jpg')
                ResizeImage(ii_lujin, path_save + '/' + ii, 3840, 4800, 'jpeg')
                image_fwpmt = Image.open(path_save + '/' + ii)
                image_fwpmt.paste(image_fugai, (2980, 601))
                image_fwpmt.paste(image_fugai, (2980, 880))
                image_fwpmt.paste(image_result, (2980, 605))
                image_fwpmt.paste(image_result, (2980, 882))

                image_fwpmt.save(path_save + '/' + ii)
            elif fenzhi == 'zdt':
                numb_maji = ZDMJ_list[ZDDM_list.index(ii[:-10])]  # 找到jpg文件中的编号在宗地代码列表中顺序，在找到这个位置的宗地面积
                ii_lujin = lujin_fwpmt[name_fwpmt.index(ii)]
                start(pingjietupian_list(numb_maji, numb_zdt), result)
                image_result = Image.open(result)
                image_fugai = Image.open('D:/test/宗地图模板/k.jpg')
                ResizeImage(ii_lujin, path_save + '/' + ii, 1653, 2597, 'jpeg')
                image_fwpmt = Image.open(path_save + '/' + ii)
                image_fwpmt.paste(image_fugai, (1135, 442))
                image_fwpmt.paste(image_result, (1135, 444))
                image_fwpmt.save(path_save + '/' + ii)
        except StopIteration:
            print('迭代器没有更多的值')
        except OSError:
            print('操作系统错误')
        except WindowsError:
            print('Windows系统调用失败')
        except IndexError:
            print('序列中没有此索引', numb, numb_fwpmt, numb_maji, numb_zdt, ii_lujin)
        except LookupError:
            print('无效数据查询', numb, numb_fwpmt, numb_maji, numb_zdt, ii_lujin)


        print("完成", numb, path_save + '/' + ii)
        numb += 1


if __name__ == '__main__':
    numb_fwpmt = ['D:/test/房屋平面图模板/0.jpg', 'D:/test/房屋平面图模板/00.jpg', 'D:/test/房屋平面图模板/1.jpg', 'D:/test/房屋平面图模板/2.jpg',
                  'D:/test/房屋平面图模板/3.jpg', 'D:/test/房屋平面图模板/4.jpg', 'D:/test/房屋平面图模板/5.jpg', 'D:/test/房屋平面图模板/6.jpg',
                  'D:/test/房屋平面图模板/7.jpg', 'D:/test/房屋平面图模板/8.jpg', 'D:/test/房屋平面图模板/9.jpg']
    numb_zdt = ['D:/test/宗地图模板/0.jpg', 'D:/test/宗地图模板/00.jpg', 'D:/test/宗地图模板/1.jpg', 'D:/test/宗地图模板/2.jpg',
                'D:/test/宗地图模板/3.jpg', 'D:/test/宗地图模板/4.jpg', 'D:/test/宗地图模板/5.jpg', 'D:/test/宗地图模板/6.jpg',
                'D:/test/宗地图模板/7.jpg', 'D:/test/宗地图模板/8.jpg', 'D:/test/宗地图模板/9.jpg']
    print('输入xlsx文件所在文件夹，文件夹里面只放一个文件')
    # result = 'D:/test/贴图用.png'  # 拼接好的面积的图片，后面根据面积的不同，保存在不同的位置
    path_xlsx = input().replace('\\', '/') or 'D:/test/xlsx模板'
    path_xlsx_ture = duquxlsx(path_xlsx)  # xlsx文件本身路径
    # 打开xlsx
    xlsx = xlrd.open_workbook(path_xlsx_ture)
    sheet = xlsx.sheets()[0]
    ZDDM_list = []
    ZDMJ_list = []
    JZMJ_list = []
    path_fwpmt = input('房屋平面图所在位置').replace('\\', '/') or 'D:/test/0-9'
    path_zdt = input('宗地图所在位置').replace('\\', '/') or 'D:/test/0-9'
    for i in range(0, sheet.nrows - 5):
        ZDDM_list.append(sheet.cell_value(i + 5, 7))
        ZDMJ_list.append(sheet.cell_value(i + 5, 9))
        JZMJ_list.append(sheet.cell_value(i + 5, 11))
        # print(ZDDM_list, ZDMJ_list, JZMJ_list)
    numb = 1
    try:
        pt_1(path_fwpmt, 'fwpmt')
        pt_1(path_zdt, 'zdt')
    except:
        print('异常')
        input('回车退出')
    else:
        input('回车退出')

    # 先处理房屋平面图
    # 获取所有的房屋平面图的路径列表及文件名称
