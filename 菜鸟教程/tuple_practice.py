nums_tuple = (3, 1, 4, 1, 5, 9, 2)
point = (12, 35)
nest = ([10,20], 666)
# 一、获取元组下标 2 的元素，截取下标 1 到倒数第 2 个切片。
print(nums_tuple[2])
print(nums_tuple[1:-1])
# 二、统计数字 1 在 nums_tuple 出现次数，查找数字 9 的索引。
print(nums_tuple.count(1))
print(nums_tuple.index(9))
# 三、将两个元组 t1=(1,2) t2=(3,4) 拼接成新元组。
t1=(1,2)    
t2=(3,4)
t_new=t1+t2
print(t_new)
# 四、单元素元组写法：创建只包含数字 8 的元组。
t3=(8,)
print(t3)
# 五、拆包 point 元组，把两个值分别存入 x、y 变量。
x,y=point
print(x,y)
# 六、尝试修改 nums_tuple[0] = 99，观察报错并说明原因。
# nums_tuple[0] = 99
# 报错：元组是不可变的，不能修改元素
# 七、给嵌套元组 nest 内的列表追加元素 30，写出代码。
nest[0].append(30)
print(nest)
# 八、使用 sorted () 对 nums_tuple 排序，观察返回值类型。
result = sorted(nums_tuple)
print(result)#返回值是列表
# 九、判断元组是否支持 +=，写出代码验证 nums_tuple += (7,8)。
nums_tuple+=(7,8)
print(nums_tuple)
# 十、元组转列表、列表转元组，互相转换代码。
print(list(nums_tuple))#元组转列表
print(tuple(list(nums_tuple)))#列表转元组

#10 道元组专项练习题（由浅入深）
# 基础题 1
# 创建一个包含数字 2,4,6,8 的元组，并打印整个元组。
new_tuple = (2,4,6,8)
print(new_tuple)
t4 = (99,)#单元素元组
print(t4)
#已知 t = (11,22,33,44,55)，用索引分别取出第一个元素和最后一个元素。
t=(11,22,33,44,55)
print(t[0])
print(t[-1])
#切片操作：t = (1,3,5,7,9,11)，截取中间 (5,7,9) 生成新元组。
t5 = (1,3,5,7,9,11)
new_t5=t5[2:5]
print(new_t5)
print(t5.count(3))
print(t5.index(7))
#定义函数 get_info ()，返回三个数据：姓名、年龄、城市（用元组返回）；调用函数拆包打印所有信息。
def get_info():
    return 'Llou',30,'饶平'
name,age,dizhi = get_info()
print(name,age,dizhi)