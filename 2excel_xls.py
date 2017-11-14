#################################################################
#
#
#    diff_excel.py
#
#    example: diff_excel.py
#
#    auther: Devin Li
#    date:    2016/8/29
#    function: compare excel files
#
#################################################################

import sys
from tkinter import *
import tkinter.filedialog
import subprocess
import xlwt
import xlrd

# ===================================================================================
def Input():
    global file1, file2
    label = Label(Tk(), text='选择第一个对比文件')
    label.pack()
    file1 = tkinter.filedialog.askopenfilename(filetypes=[("xlsx格式,xls格式", "xlsx xls"), ("All files", "*")],
                                               title='选择第一个对比文件')

    label = Label(Tk(), text='选择第二个对比文件')
    label.pack()
    file2 = tkinter.filedialog.askopenfilename(filetypes=[("xlsx格式,xls格式", "xlsx xls"), ("All files", "*")],
                                               title='选择第二个对比文件')


# ===================================================================================

# ===================================================================================
def Diff():

    wb1 = xlrd.open_workbook(file1)
    wb2 = xlrd.open_workbook(file2)

    sheet1 = wb1.sheet_by_index(0)
    sheet2 = wb2.sheet_by_index(0)

    wb_result = xlwt.Workbook()  # 新建一个文件，用来保存结果
    sheet_result = wb_result.add_sheet('result', cell_overwrite_ok=True)

    cols2 = sheet2.col_values(0)

    for r in range(0, sheet1.nrows):
        sheet1_cell_value = sheet1.cell_value(r,0)
        if (sheet1_cell_value not in cols2):
            sheet_result.write(r, 0, sheet1_cell_value)

    wb_result.save('result.xls')

    # ===================================================================================

def main():
    # file1 = sys.argv[1]
    # file2 = sys.argv[2]

    Input()
    Diff()


if __name__ == '__main__':
    # if len(sys.argv)<3:
    #    exit()
    main()

