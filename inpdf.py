# -*- coding: utf-8 -*-
"2021年1月8日"
from PyPDF2 import PdfFileReader, PdfFileWriter
import os, openpyxl
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait


def getimgfile(input_paths, file_type=".jpg"):
    """
    转pdf之前先获取图片的大小
    :param input_paths:
    :param file_type:
    :return:
    """
    pathDir = os.listdir(os.path.abspath(input_paths))
    imglist = list()
    for i in pathDir:
        if file_type in i:
            imglist.append(i)
    return imglist


def imgtopdf(imgpath, outputpath="./docimg.pdf", file_type=".jpg"):
    """
    图片转pdf
    :param input_paths:
    :param outputpath:
    :param file_type:
    :return:
    """
    img = Image.open(imgpath)
    out = img.resize((596, 842), Image.ANTIALIAS)
    imgpath_ = imgpath + '.jpg'
    out.save(imgpath_, 'jpeg')
    (maxw, maxh) = Image.open(imgpath_).size
    print('修改图片大小')
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(imgpath_, 0, 0, maxw, maxh)
    c.showPage()
    c.save()


def file2list(path_, guolv):
    """
    将输入路径中的文件转成两个list，一个存名称，一个路径
    :param guolv:
    :param path_:
    :return:
    """
    list_mc = []
    list_ph = []
    for i_pdf in os.listdir(path_):
        if i_pdf[-4:] == guolv:
            list_ph.append(path_ + '/' + i_pdf)
            print('找到', path_ + '/' + i_pdf)
            if guolv == '.pdf':
                list_mc.append(i_pdf[0:len(i_pdf) - 17])
            elif guolv == '.jpg':
                list_mc.append(i_pdf[0:len(i_pdf) - 13])
    return list_mc, list_ph


def addBlankpage(pdf_1, pdf_2, pdf_in):
    pdfFileWriter = PdfFileWriter()
    numb_page = 0
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(pdf_1)
    pdfFileReader_ = PdfFileReader(pdf_in)
    numPages = pdfFileReader.getNumPages()
    pdf_in_ = pdfFileReader_.getPage(0)
    for index in range(0, numPages):
        pageObj = pdfFileReader.getPage(index)
        text = str(pageObj.extractText())
        print('`````````', text, index, '!!!!!!!!!!!')
        if 'J1-J2:' in text:
            print(index, '~~~~~~~~~')
            numb_page = index
        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
    if numb_page == 0:
        print(pdf_2)
        input('出错，按回车继续')
        pass
    else:
        pdfFileWriter.insertPage(pdf_in_, numb_page - 1)
        pdfFileWriter.write(open(pdf_2, 'wb'))


if __name__ == '__main__':
    try:
        print('岳阳房地一体专用插件，作者wjl' + '\n' + '请做好数据备份！！！！！')
        path_pdf = input('输入pdf所在路径').replace('\\', '/') or 'D:/test/pdf/1'
        path_jpeg = input('输入照片所在路径').replace('\\', '/') or 'D:/test/pdf/2'
        # list_ph_pdf = []  # pdf路径存一个列表
        # list_mc_pdf = []  # pdf名称存一个列表

        xlsx_jieguo = openpyxl.Workbook()
        xlsx_jieguo_sheet = xlsx_jieguo.active
        xlsx_jieguo_sheet.title = 'jieguo'
        numb_ = 1
        path_jieguo = 'D:/test/检查结果/'
        if os.path.isdir(path_jieguo):
            pass
        else:
            os.mkdir(path_jieguo)
        if os.path.isdir('D:/test/检查结果/改好的pdf'):
            pass
        else:
            os.mkdir('D:/test/检查结果/改好的pdf')

        list_mc_pdf, list_ph_pdf = file2list(path_pdf, '.pdf')
        list_mc_jpg, list_ph_jpg = file2list(path_jpeg, '.jpg')
        print(list_mc_pdf, list_ph_pdf, list_mc_jpg, list_ph_jpg)

        for i in list_mc_pdf:
            if i in list_mc_jpg:
                index_ = list_mc_pdf.index(i)
                print(i)
                pdf_file = PdfFileReader(list_ph_pdf[index_])
                pagenumb = pdf_file.getNumPages()
                img_file_ph = list_ph_jpg[index_]
                imgtopdf(img_file_ph, 'D:/test/检查结果/中转pdf.pdf')
                addBlankpage(list_ph_pdf[index_], 'D:/test/检查结果/改好的pdf/' + list_mc_pdf[index_] + '_宅基地权籍调查表-解析法.pdf',
                             'D:/test/检查结果/中转pdf.pdf')
            else:
                print('找不到对应的照片', i)
                xlsx_jieguo_sheet.cell(row=numb_, column=1).value = i
                xlsx_jieguo_sheet.cell(row=numb_ + 1, column=2).value = i

        xlsx_jieguo.save(path_jieguo + '结果.xlsx')
    except Exception as e:
        print(e)
    else:
        print('运行结束，回车退出')
        input()