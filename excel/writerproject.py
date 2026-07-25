'''
通过一个excel做个一数据分析柱状图
再通过邮件发送给邮箱
实现步骤
步骤一:xlrd模块读取Excel数据
步骤二:xlsxwriter模块生成就业数据图表
步骤三:smtplib模块发送附件邮件
1.smtplib模块对smtp协议进行了封装，提供更便捷的方式发送电子邮件
登录→服务器设置
写邮件→（信息发送方、信息接收方、邮件主题、邮件内容（附件））
发送
'''
import xlrd
import xlsxwriter
import smtplib #负责邮件的发送
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#1.读取
data = xlrd.open_workbook("info.xlsx")
class_info= []
#print(data.sheets())
for sheet in data.sheets():#data.sheets()拿到所有工作表
    dict={'name':sheet.name,'avg_salary':0}#班级信息
    #print(sheet.name + '\n')
    sum=0 #存储薪资
    for i in range(sheet.nrows):
        if i>1:
            sum+=float(sheet.cell(i,5).value)
    dict['avg_salary']=sum/(sheet.nrows-2) #通过sun得到一个总薪资/行数=平均工资
    class_info.append(dict)
#print(class_info)
#print(dict)
#2.写入excel
Workbook=xlsxwriter.Workbook('newinfo.xlsx')#创建一个文件
sheet=Workbook.add_worksheet()#创建一个工作表，不指定，默认是sheet1、sheet2
#写入班级数据,先定义两个空的列表来接收数据
name_info=[] 
salary_info=[]
for item in class_info:
    name_info.append(item['name'])
    salary_info.append(item['avg_salary'])
sheet.write_column('A1',name_info)
sheet.write_column('B1',salary_info)
# print(name_info)
# print('\n')
# print(salary_info)
#写入图表
chart= Workbook.add_chart({'type':'column'})#创建一个图表，column是柱状图类型
#指定图表的标题
chart.set_title({'name':'平均就业薪资'})#里面可以设置显示的名称name，也可以传入样式的对象
#数据源
chart.add_series({
    'name':'班级',
    'categories':'=Sheet1!$A$1:$A$3',#工作表名称！$列$起始列：$列$结束行
    'values':'=Sheet1!$B$1:$B$3',#图表的数据源
    'data_labels':{'value':True}
})
sheet.insert_chart('A7',chart)
Workbook.close()#写入关闭掉
#3.发送邮件
host_server='smtp.163.com'#主机地址
#发件人邮箱
sender="llou9602@163.com"
#发件人邮箱密码、授权码
code='SMuQ4768mreVTyF7'
#收件人邮箱
user1='1009891635@qq.com'
#准备邮件数据
#邮件标题
mail_title="！！！1月份平均就业薪资"
#内容
mail_content="1月份平均就业薪资，请具体查看附件"
#构建附件
attachment= MIMEApplication(open('newinfo.xlsx','rb').read())#用open打开要发送的文件，可读的方式，再用一个read去读取
attachment.add_header('Content-Disposition','attachment',filename='data.xlsx')#给这个附件设置头部的信息,和发送的文件名
#Content-Disposition：告诉接收方的邮件程序，接下来的数据是应该直接显示在邮件正文中，还是作为一个独立的文件供用户下载
#attachment：这是 Content-Disposition 字段的一个具体取值，意为“附件”

#SMTP
smtp=smtplib.SMTP(host_server)
#登录
smtp.login(sender,code)
#发送
msg=MIMEMultipart()#带附件的实例
msg['Subject']=mail_title#指定邮件的主题
msg['From']=sender#发件人
msg['To']=user1#收件人
msg.attach(MIMEText(mail_content))#邮件的内容
msg.attach(attachment)#添加附件 attachment 添加的附件
smtp.sendmail(sender,user1,msg.as_string())