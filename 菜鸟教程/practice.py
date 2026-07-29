# lst =  [10, 20, 30, 20, 50]
# #1.往列表末尾追加数字 60，写出代码并输出最终列表
# lst.append(60)
# print(lst)
# #2.现有新数据 [70, 80]，要求把里面每个数字拆开合并进 lst，不能生成嵌套列表，写出代码。
# lst+=[70,80]
# #lst.extend([70,80])
# print(lst)
# #3.删除列表最后一个元素，并打印被删掉的值。
# delete_lst=lst.pop()#移除列表最后一个元素，并返回。默认是-1 最后一个
# print(delete_lst)
# #4.删除列表中第一个 20，写出代码。该方法没有返回值
# lst.remove(20)
# print(lst)
# #5.查询数字 30 在列表中第一个匹配项的下标索引。
# print('查询数字 30 在列表中的下标索引。用index',lst.index(30))
# #list.index(x[, start[, end]])
# # x-- 查找的对象。
# # start-- 可选，查找的起始位置。
# # end-- 可选，查找的结束位置。
# #6.截取列表第 2 个到倒数第 2 个元素（切片），打印结果。
# print(lst[1:-1])#最后一个取不到，要取最后一个直接不写，取到倒数第二个写-1
# #7.统计列表中数字 20 一共出现多少次。
# print('20 出现了：',lst.count(20))
# #8.对列表进行从小到大排序，原地修改列表。
# print(lst)
# lst.sort()#reverse 默认是false 升序
# print(lst)

# #9.反转整个列表顺序（原地反转）。
# lst.reverse()
# print(lst)

# #10.列表复制：创建一份全新独立副本 new_lst，修改 new_lst 不影响原 lst。
# import copy
# new_lst1=lst.copy()
# new_lst=copy.deepcopy(lst)
# print(new_lst)

# print('------------------------------------------------')

# a=[[0,1],[1,2],[2,3]]
# a.insert(2,a[1])
# a.append(a[3])
# print (a)
# a[1][1]=0
# a[4][1]=4
# print(a)
#-------------------------------进阶练习---------------------------
# 基础列表
nums = [5, 2, 8, 2, 9, 5, 3]
# 嵌套列表
info = [["张三", 22,], ["李四", 25]]
# 1.区分 append 与 extend：现有 add_data = [1,3]，分别用两种方法把数据加到 nums 
# 末尾，写出两段代码，并写出两段代码执行后的列表区别。
add_data=[1,3]
#nums.append(add_data)#嵌套列表，把整个列表当成1个元素
#[5, 2, 8, 2, 9, 5, 3, [1, 3]]
nums.extend(add_data)#拆分元素追加，无嵌套
print(nums)

# 2.使用切片截取 nums 中索引 1 到 4（包含 1，不包含 4）的元素，打印结果。
print(nums[1:4])
# 3.使用切片把 nums 全部复制一份新列表 new_nums，修改 new_nums 第一个元素，验证不会影响原 nums。
new_nums = nums[:]#切片拷贝和copy()一样，内层列表依然共用
new_nums[0]=99
print(nums)
# 4.删除 nums 中最后 2 个元素，用两种写法实现（pop + 循环 / 切片截断）。
#写法1pop运行两次
# nums.pop()
# nums.pop()
#写法二
# nums=nums[:-2]

# 5.统计 nums 中数字 5 出现的次数；再找到数字 9 的索引下标。
print(nums.count(5))
print(nums.index(9))
# 6.将 nums 从小到大原地排序；再直接反转排序为从大到小（两种方式：sort 参数 /reverse ()）。
nums.sort()
print(nums)
nums.reverse()
print(nums)
# 7.往嵌套列表 info 里新增一条数据 ["王五",21]；再把李四的年龄修改为 26。
info.append(['王五',21])
info[1][1]=26
print(info)
# 8.不使用集合，用循环把 nums 列表去重，生成无重复新列表。
new_nums=[]
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
print(new_nums)
# 合并两个列表 a=[10,20]、b=[30,40]，分别写出 a.extend(b) 和 c = a + b，说明两者区别。
a=[10,20]
b=[30,40]
c=a+b
a.extend(b)
print(a)
print(c)
# 清空 nums 列表，写出两种清空列表的写法。
nums[:]=[]#清空原列表；nums=[]只是重新赋值，不修改原列表
nums.clear()
print(nums)

#-------------------更难的题目--------------------------
# 1.深浅拷贝坑题：写代码区分三种复制方式，观察修改内层列表的差异
a = [[1,2], 3, 4]
b1 = a          # 直接赋值
b2 = a[:]       # 切片浅拷贝
import copy
b3 = copy.deepcopy(a) # 深拷贝
# 分别修改 b1[0].append(99)、b2[0].append(99)、b3[0].append(99)，打印原列表a，说明三种复制区别

# 2.切片高阶操作：不创建新列表，原地删除 num_list 所有偶数（用切片赋值完成，禁止循环 pop/remove）
num_list = [2, 5, 2, 8, 1, 5, 9, 8, 2]
# 筛选所有奇数，切片原地覆盖原列表
num_list[:]=[x for x in num_list if x%2 !=0]
print(num_list)
#3.嵌套列表排序：将 staff 列表按照薪资从高到低排序，原地修改，打印排序后的完整列表
staff = [["小明", 24, 6000], ["小红", 22, 8000], ["小刚", 26, 5500]]
staff.sort(key=lambda x:x[2],reverse=True)#匿名函数取第三个元素薪资
print(staff)
#4.原地去重（不生成新列表）：直接修改原 num_list，
# 删除所有重复数字，保留元素第一次出现的顺序，禁止转集合（集合会打乱顺序）
num_list = [2, 5, 2, 8, 1, 5, 9, 8, 2]
temp=[]
i = 0
while i<len(num_list):
    val =num_list[i]
    if val in temp:
        num_list.pop(i)
    else:
        temp.append(val)
        i+=1
print(num_list)