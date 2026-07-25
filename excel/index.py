import xlrd
#------------xlrd的常用函数------------------
data=xlrd.open_workbook('公司数据表.xls')
# '''print(data.sheet_loaded(0) )
# data.unload_sheet(0)
# print(data.sheet_loaded(0))'''
# ''' 判断指定索引的工作表是否已经加载到内存
# 判断指定索引的工作表**是否已经加载到内存**。
# xlrd 打开文件时，默认**不会一次性加载所有 sheet 数据**；
# 只有访问 `book.sheet_by_index(n)` 时才会解析该 sheet 存入内存。

# - 返回 `True`：该 sheet 已加载
# - 返回 `False`：还未加载，此时读取单元格会触发加载
# '''
# #print(data.sheet_loaded(1))
# print(data.sheets())#获取全部sheet，返回值是一个列表，可以通过索引访问某个表格
# print(data.sheets()[0])

# data.sheet_by_index(0)#根据索引获取工作表
# result=data.sheet_by_name('在职花名册')#根据名字去获取
#                                         #严格区分大小写
# all_names=data.sheet_names()
# #获取所有工作表的名字
# #就可和sheet_by_name配合获取各个表格
# #取个all_names列表的长度就知道有多少个工作表
# sheet_len=data.nsheets#返回excel工作表的数量
# print(result)
# print(all_names)
# print(data.nsheets)


#-------------xlrd操作excel行---------------------
# sheet=data.sheet_by_index(0)#获取第一个工作表
# print(sheet.nrows)#获取sheet下的有效行数
# print(sheet.row(0))#该行单元格对象组成的列表
# print(sheet.row_types(1))#获取单元格的数字类型
# #输出array('B', [1, 1, 1, 1, 1, 1, 0])
# # 1 代表字符串 2 表示数字 3表示时间 4 表示布尔 5表示挨罗
# print(sheet.row(3)[3])#输出  text:'梁竹文'
# print(sheet.row(3)[3].value)#得到单元格value 输出 梁竹文
# print(sheet.row_values(3))#得到指定行单元格的value
# print(sheet.row_len(3))#得到单元格的长度


#-----------------xlrd操作列----------------------------
# sheet = data.sheet_by_index(0)
# print(sheet.ncols)#获取表格的列数
# #print(sheet.col_types(1))
# print(sheet.col(1))#返回该列单元格对象组成的列表
# print(sheet.col(1)[2])
# print(sheet.col(1)[2].value)
# print(sheet.col_values(1))#返回该列所有单元格的value组成的列表
# print(sheet.col_types(2))#查看数据类型

#--------------------xlrd操作excel单元格------------------
# sheet = data.sheet_by_index(0)
# print(sheet.cell(1,1))#获取单元格内容
# print(sheet.cell_type(1,1))#获取单元格数据类型
# print(sheet.cell(1,1).ctype)#也可以获取到单元格的数据类型
# print(sheet.cell(1,2).value)#获取单元格的值
# print(sheet.cell_value(1,2))#获取单元格的值

