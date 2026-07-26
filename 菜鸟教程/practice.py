lst =  [10, 20, 30, 20, 50]
#1.往列表末尾追加数字 60，写出代码并输出最终列表
lst.append(60)
print(lst)
#2.现有新数据 [70, 80]，要求把里面每个数字拆开合并进 lst，不能生成嵌套列表，写出代码。
lst+=[70,80]
#lst.extend([70,80])
print(lst)
#3.删除列表最后一个元素，并打印被删掉的值。
delete_lst=lst.pop()#移除列表最后一个元素，并返回。默认是-1 最后一个
print(delete_lst)
#4.删除列表中第一个 20，写出代码。
lst.remove(20)
print(lst)
#5.查询数字 30 在列表中的下标索引。
print('查询数字 30 在列表中的下标索引。用index',lst.index(30))