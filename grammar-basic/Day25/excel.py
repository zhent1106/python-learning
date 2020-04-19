"""
excel操作
"""
import xlrd
import random
import wordcloud

# 1.打开工作蒲
workbook = xlrd.open_workbook('./res/excel/班级卡片数据.xlsx')

# 2.工作表
# 输出所有sheet的名字
print(workbook.sheet_names())
# 输出所有的sheet
print(workbook.sheets())
# 根据索引获取sheet
print(workbook.sheet_by_index(0))
# 根据名字获取sheet
print(workbook.sheet_by_name('工作表1'))
# 3.行、列操作
sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
# 获取第2行的内容
print(sheet1.row_values(1))
# 获取第3列的内容
print(sheet1.col_values(2))
# 获取第1列的内容
list = sheet1.col_values(1)+sheet1.col_values(13)
list.remove('姓名')
list.remove('signature')
w = wordcloud.WordCloud(width=900,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./res/fonts/SimHei.ttf')
string = " ".join(list)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('./res/img/output5.png')


# 4.单元格的操作
cell1 = sheet1.cell(1, 1).value
print(cell1)
cell2 = sheet1.row(1)[1].value
print(cell2)
cell3 = sheet1.cell(1, 2).value
print(cell3)
cell4 = sheet1.col(2)[1].value
print(cell4)
# 5.日期类型 （在对应的单元格准备好日期数据)
date_value = xlrd.xldate_as_datetime(
    sheet1.cell_value(1, 5), workbook.datemode)
print(type(date_value), date_value)
