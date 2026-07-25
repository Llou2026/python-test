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


#列表List
my_list= ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123,'runoob']
print(my_list)#打印整个列表
print(my_list[0])#打印第一个元素
print(my_list[-4])
color_list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(color_list[1:-2])#从第二位开始（包含）截取到倒数第二位（不包含）
color_list[0]='红色'
print(color_list[0])