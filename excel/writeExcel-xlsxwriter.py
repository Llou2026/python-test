'''
xlswriter模块介绍
xlsxwriter为Python第三方模块，用于向生成的Excel表格插入数据、图表等操作
安装:pip install xlsxwriter
导入:import xlsxwriter

xlsxwriter如何脱颖而出
xlsxwriter较其他模块支持更多的Excel功能
100%兼容Excel xlsx文件，支持Excel 2003、Excel 2007等版本
xlsxwriter处理速度更快，支持大文件写入
'''
import xlsxwriter
wb=xlsxwriter.Workbook("data.xlsx")#创建data.xlsx文件
cell_format=wb.add_format({'bold':True})#创建一个格式对象,定义一个变量cell_format去接收
#{'bold':True}设置字体加粗
cell_format1=wb.add_format()
cell_format1.set_bold()#设置加粗，默认是True
cell_format1.set_font_color("red")#字体的颜色
cell_format1.set_font_size(14)#字体大小
cell_format1.set_align("center")#对齐方式

cell_format2=wb.add_format()
cell_format2.set_bg_color("#808080")#设置背景颜色
#创建sheet工作表
sheet=wb.add_worksheet("newsheet")#如果不传入则默认是sheet1、sheet2...
#写入
#sheet.write_string()
sheet.write(0,0,"2020年度",cell_format)#写入单个单元格的数据
sheet.merge_range(1,0,2,2,"第一季度销售统计",cell_format1)
#合并单元格 参数：起始行，起始列，结束行，结束列，文本内容
data=(
    ["一月份",500,450],
    ["二月份",600,450],
    ["三月份",700,550]
)#元组嵌套列表，元组内容不看变
sheet.write_row(3,0,["月份","预期销售额","实际的销售额"],cell_format2)
for index,item in enumerate(data):#依次写入数据
    sheet.write_row(index+4,0,item)
#写入 
sheet.write(7,1,"=sum(B5:B7)")
sheet.write(7,2,"=sum(C5:C7)")

sheet.write_url(9,0,"http://www.baidu.com",string="更多数据")#write_url(row, col, url, cell_format=None, string=None)
sheet.insert_image(10,0,'view.png')#插入图片

#------------写入图表开始-----------------------
chart=wb.add_chart({'type':'bar'})#创建一个图表对象，column是柱状图，line是线形图
chart.set_title({'name':'第一季度销售统计'})
#X Y轴信息
chart.set_x_axis({'name':'月份'})
chart.set_y_axis({'name':'销售额'})
#数据
chart.add_series({
    'name':'预期销售额',
    'categories':'=newsheet!$A$5:$A$7',
    'values':['newsheet',4,1,6,1],
    'data_labels':{'value':True}#加图表数字

})
chart.add_series({
    'name':'实际销售额',
    'categories':'=newsheet!$A$5:$A$7',
    'values':['newsheet',4,2,6,2],
    'data_labels':{'value':True}#加图片数字
})
sheet.insert_chart('A24',chart)#写入表格
#----------------写入图表完成----------------
wb.close()