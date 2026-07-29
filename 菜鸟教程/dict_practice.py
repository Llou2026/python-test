# 题目 1：创建与访问
# 创建一个字典 学生信息，包含：姓名=小明、年龄=18、城市=北京。
# 打印出"姓名"对应的值
# 尝试访问"电话"这个键（不存在），观察报错
student={'name':'小明','age':18,'city':'北京'}
print(student['name'])


# 题目 2：字典遍历
# 已知 成绩表 = {"语文": 88, "数学": 95, "英语": 76}。
# 遍历所有键并打印
# 遍历所有值并打印
# 以"科目: 分数"的格式遍历并打印

score = {"语文": 88, "数学": 95, "英语": 76}
for i in score.keys():#遍历所有键
    print(i)
for i in score.values():#遍历所有值
    print(i)
for key,val in score.items():#遍历所有键值对
    print(key,':',val)#打印键值对
print('-------------')#打印分隔线
#题目 3：修改与增删
# 已知 inventory = {"苹果": 10, "香蕉": 20, "橘子": 15}。
inventory = {"苹果": 10, "香蕉": 20, "橘子": 15}
# 将苹果数量改为 12
# 新增"葡萄"，数量为 8
# 删除"香蕉"键值对
# 打印最终字典
inventory['苹果']=12
inventory['葡萄']=8
del inventory['香蕉']
print(inventory)
print('-------------')#打印分隔线
#题目 4：get 方法与默认值
user ={'name':'小红','age':20,'city':'北京'}
print(user.get('name'))
print(user.get('phone','未设置'))
print(user.get('phone'))
print('-------------')#打印分隔线
#目 5：keys/values/items 方法
course = {'语文':80,'数学':90,'英语':70}
course_name=course.keys()
print(course_name)
course_score=course.values()
print(course_score)
if '语文' in course_name:
    print('语文成绩是:',course['语文'])
    print('--------------------')#打印分隔线
#题目 6：字典推导式
square={x:x**2 for x in range(1,6)}
print(square)
words = ["hello", "world", "python"]
dict_words = {x:len(x) for x in words}
print(dict_words)
# 题目 7：嵌套字典
clbum={
    'name':"二班",
    'student': {
        "小明": {"年龄": 18, "分数": 90},
        "小红": {"年龄": 19, "分数": 85}
    }
}
print(clbum['student']['小明']['分数'])
clbum['student']['小刚']={"年龄": 17, "分数": 92}
#print(clbum)
score_all = [x['分数'] for x in clbum['student'].values()]
print(score_all)
score_ave=sum(score_all)/len(clbum['student'])
print(score_ave)
import pprint
import json
pprint.pprint(clbum)
print(json.dumps(clbum,ensure_ascii=False,indent=4))
