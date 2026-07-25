#for 循环 ,range()生成整数序列，常与for循环配合使用
#enumerate()遍历同时获取索引和值
for i,j in enumerate(range(0,10)):
    pass
    print(f'{i}:{j}')
print('------------while循环--------------')
#while 循环，在python中没有do..while循环
x=10
while x>0:
    #print(f'{x}>0')
    print("%d>0"%x)
    x-=1
#python推导式
print('-------------------------python推导式-----------------------------')
#1.列表(list)推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name for name in names if len(name)>3]
print(new_names)
#计算30以内可以被3整除的整数
print('-------------计算 30 以内可以被3整除的整数-----------------')
multiples = [i for i in range(30) if i%3==0]
print(multiples)
#2.字典推导式
listdemo= ['Google','Runoob', 'Taobao']