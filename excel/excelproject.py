import xlrd
from datetime import datetime
#第一步：通过xlrd模块读取Excel数据
data=xlrd.open_workbook("data2.xlsx")
sheet = data.sheet_by_index(0)#获取到工作表
question_list=[]#构建试题列表
#试题类
class Question:
    pass
for i in range(sheet.nrows): #从0开始，到 `sheet.nrows-1` 结束，步长默认 1
    if i>1:
        obj=Question()#构建试题对象
        obj.subject=sheet.cell(i,1).value#题目
        obj.questionType = sheet.cell(i,2).value #题型
        obj.optionA = sheet.cell(i,3).value #选项A
        obj.optionB = sheet.cell(i,4).value #选项B
        obj.optionC = sheet.cell(i,5).value #选项C
        obj.optionD = sheet.cell(i,6).value #选项D
        obj.score = sheet.cell(i,7).value #分值
        obj.answer = sheet.cell(i,8).value #答案
        question_list.append(obj)
#print(question_list)
#导入操作 pymysql pip install
from mysqlhelper import *
#1.连接到数据库
db=dbhelper('127.0.0.1',3306,"root","123456","test")
#插入语句
now = datetime.now().replace(microsecond=0)
sql=f"insert into question(subject,questionType,optionA,optionB,optionC,optionD,score,answer) values (%s,%s,%s,%s,%s,%s,%s,%s)"
val=[]#空列表来存储元组数据
for item in question_list:
    val.append((item.subject,item.questionType,item.optionA,item.optionB,item.optionC,item.optionD,item.score,item.answer))
#print(val)
db.executemanydata(sql,val)
#第二步：通过pymysql模块连接数据库
#第三步：组装数据、执行插入操作
#第四步：关闭数据库连接