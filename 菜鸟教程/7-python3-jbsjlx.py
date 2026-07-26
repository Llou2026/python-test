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
#元组中的元素值是不允许删除的,只能使用del语句删除整个元组
del tup2#删除整个元组

#--------------------------字典-------------------------
#创建空字典
#使用大括号来创建空字典
emptyDict={}
print(type(emptyDict))
#使用内建函数dict()创建字典
empty_dict = dict()
print(empty_dict)
print("Length:",len(empty_dict))#查看字典长度
print(type(empty_dict))#查看类型
#访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name]:",tinydict['Name'])
print("tinydict['Age]:",tinydict['Age'])
#tinydict['mi'] 如果字典里没有建访问数据 会出现错误

#修改字典
tinydict['Age'] = 8  #更新Age
tinydict['School']='菜鸟教程'#添加信息
print("tinydict['Age']:",tinydict['Age'])
print("tinydict['School']:",tinydict['School'])
#删除字典元素
del tinydict['Name']#删除键Name
tinydict.clear()#清空字典
del tinydict#删除字典
#tinydict = {'Name': ['Runoob'], 'Age': 7}
seq = ('name', 'age', 'sex')
value=['tinydict']
tinydict = dict.fromkeys(seq,value)
#value是所有值的初始值，不能一一对应赋值的
print(tinydict)
#输出的结果是{'name': ['Llou', '18', 'boy'], 'age': ['Llou', '18', 'boy'], 'sex': ['Llou', '18', 'boy']}
dict1=tinydict#直接赋值，指向同一个内存
dict2=tinydict.copy()#浅拷贝，只拷贝父对象，不会拷贝对象的内部子对象，而是直接引用
dict1['name'][0]='dict1'
dict2['name'][0]='dict2'
print(tinydict['name'][0],dict1['name'][0],dict2['name'][0])
import copy
dict3=copy.deepcopy(tinydict)#深拷贝
dict3['name'][0]='dict3'
print(tinydict['name'][0])

#判断键是否存在
print('name' in tinydict)
#判断值是否存在
print('--------------')
print(tinydict.values())
print('--------------')
print(any('name' in val for val in tinydict.values()))
#items方法的使用,在for循环中可以同时拿到keys 和values
print(tinydict.items())
for key,val in tinydict.items():
    print('key:',key)
    print('value:',val)
#tinydict.setdefault(keys,value)获取值，如果键不存在会新建keys 默认值就是你给的value
result = tinydict.setdefault('name')
print(result)
#字典的update()函数 批量合并、覆盖更新字典。
test_str = ['a']
test_str.extend('bcdefghijklmnopqrstuvwxyz')
print(test_str)
'''
append(x)：x 整体作为1 个元素加入列表
extend(x)：把 x 里面每一个元素拆分，全部追加进列表
想合并两个列表、不要嵌套，就用 extend()
'''

#----------------------------集合-----------------------------------
print('--------------------------------集合-----------------------------')
set1={1,2,3,4} #直接使用大括号创建集合
set2=set([4,5,6,7])#使用set（）函数从列表创建集合
print('创建一个空集合必须使用set()而不是{}，因为{}是用来创建一个空字典的')
#列表的去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)#这里演示的是去重功能
#输出{'orange', 'apple', 'banana', 'pear'}
#这个功能可用于列表的快速去重
arr=["a", "b", "a", "c", "b"]
new_arr = list(set(arr))
print(new_arr)