#7.python3基本数据类型
counter = 100 #整型变量
miles = 1000.0 #浮点型变量
name = 'runoob' #字符串
#同时为多个变量赋值
#a=b=c=1
#同时为多个变量同时指定不同的值
a,b,c=1,2,"runoob"
print(a,b,c)
#通过type()函数查看变量的类型
print(type(counter),type(miles),type(name))
#可以使用isinstance()来判断
print(isinstance(miles,int))#输出false
print(isinstance(miles,float))#输出True
#通过del 语句删除对象引用

del miles,a #删除变量miles

#数值运算
result1 = 5/2 #除法得到一个浮点数
result2 = 5//2 #整除，得到一个整数(向下取整)
result3 = 5%2 #取余
print(result1,result2,result3)

#字符串
my_str = 'Runoob'
print(my_str)
print(my_str[0:-1])#打印0到倒数第二个字符(不包含最后一个)
print(my_str[0:5])#和上面作用一样 打印0到第4个字符（不包含最后一个）
print(my_str[2:])#打印从索引2开始到末尾
print(my_str*3)#重复打印3次
print(my_str+"+号:可用于字符串拼接")
#\反斜杠转义特殊字符，如果不想让反斜杠发生转义，可以在字符串前面添加一个r
print('这里是一个转义字符\n这里输出了换行')
print(r'这里是一个转义字符\n这里字符串前面加了r直接输出\n没有发生转义')
print('可以通过下标访问字符串某个字符，但是不能赋值'+my_str[0])
#布尔
print('0、空字符串、空列表、空元组等被视为 False。')


#列表List,可变，有序，允许重复，最灵活频繁增删改除
#addend在末尾添加列表
#pop 用索引删除元素并返回
#del list[2] #删除第三个元素
my_list= ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123,'runoob']
print(my_list)#打印整个列表
print(my_list[0])#打印第一个元素
print(my_list[-4])
color_list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(color_list[1:-2])#从第二位开始（包含）截取到倒数第二位（不包含）
#color_list[0]='红色'
print(color_list[0])
color_list.append('蓝色')
print(color_list)
result=color_list.pop(-1)
print(result)
print('red' in color_list)#用 in 判断 元素是否在与列表中
color_list+=['红色','白色','黄色']#列表支持拼接操作
print(color_list)
#支持嵌套列表,就像c语言里的二维数组
color_list=[['red', 'red','green', 'blue', 'yellow', 'white', 'black'],['红色','白色','黄色']]
print(color_list)
#统计列表中某个元素的数量
print(color_list[0].count('red'))
#-------------------元组-----------------------
tup1=()#创建一个空元组
tup2=(1, 2, 3, 4, 5 )
tup3="a", "b", "c", "d"#不需要括号也可以
print(type(tup3))
tup4=(40,)#元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用
print(type(tup4))
#元组中的元素是不允许修改的，但是我们可以对元组进行连接组合
new_tup=tup2+tup3
print(new_tup)