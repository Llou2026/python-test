import math
from functools import reduce #reduce函数在functools里面
def add(x,y,f):
    return f(x) + f(y)
result=add(25,9,math.sqrt)
print(result)
def f(x):
    return x*x
for item in map(f,[1,2,3,4,5,6,7,8,9]):
    print(item)

def format_name(s):
    return s[0].upper()+s[1:].lower()
for item in map(format_name,['alice', 'BOB', 'CanDY']):
    print(item)
def k(x,y):
    return x+y
def prod(x,y):
    return x*y
print(reduce(k,[1,3,5,7,9],100))
print(reduce(prod,[1,3,5,7,9]))

def is_odd(x):
    """
    判断x是否是偶数
    偶数对2取余都是0
    奇数对2取余都是1
    """
    return x % 2 == 1 #
for item in filter(is_odd,[1, 4, 6, 7, 9, 12, 17]):#符合is_odd的保留下来不符合的剔除
    print(item)
def is_not_empty(s):
    """判断是否是空字符
    """
    return s and len(s.strip()) > 0 #strip会默认删除空白字符（包括'\n', '\r', '\t', ' '）
for item in filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']):
    print(item)
    
def qrt_is_int(s):
    """判断一个数的平方根是否是整数
    """
    r=math.isqrt(s)
    return r*r == s
for item in filter(qrt_is_int,list(range(1,100))):
    print(item)
    
    
    """自定义排序函数
    """
list=[36, 5, 12, 9, 21]
print(id(list))
print(list)
list=sorted(list)#默认由小到大
print(id(list))
print(list)
score = [('Alice', 72), ('Candy', 90), ('Bob', 62)]
print(sorted(score))
def k(item):
    return item[1]
print(sorted(score,key=k,reverse=True))#reverse=True 倒序（从大到小）
score2=['bob', 'about', 'Zoo', 'Credit']
def k2(item):
    return item.lower()
print(sorted(score2,key=k2))


"""
Python 返回函数
在函数内部定义的函数和外部定义的函数是一样的
只是他们无法被外部访问

"""
#在函数内部，是可以定义子函数的
def func():
    def sub_func():
        print('call sub_func.')
    sub_func()
func()

#函数还可以返回子函数
def myabs1():
    return abs#返回函数（无需括号）
def myabs2(x):
    return abs(x)#返回函数值（需要括号）
def f():
    print('call f()...')
    def g():
        print('call g()...')
    return g#返回函数不需要带小括号
x = f()
print(type(x))

#返回函数有很多应用，比如可以将一些计算延迟执行，
#举个例子，定义一个普通的求和函数。
def calc_sum(list_):
    def lazy_sum(list_):
        return sum(list_)
    return lazy_sum(list_)
    #return sum(list_)
print('--------------------------')
f = calc_sum([1,2,3,4])
print('--------------------------')
print(type(f))
print(f)

def calc_prod(list_):
    def cazy_prod(list_):
        prod=1
        for item in list_:
            prod=prod*item
        return prod
    return cazy_prod(list_)
p =  calc_prod([1,2,3,4])
print(p)

def calc_prod2(list_):
    def lazy_prod2():
        def f(x,y):
            return x*y
        return reduce(f,list_,1)
    return lazy_prod2
cal = calc_prod([1,2,3,4])
print(cal)
"""
闭包
"""
def calc_sum(list_):
    """
    像这种内层函数引用外层函数的变量（参数也算变量）
    然后返回内层函数的情况，称为闭包
    闭包的特点是返回的函数还引用了外层函数的局部变量，
    所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
    """
    def lazy_sum():
        return sum(list_)
    return lazy_sum
#希望一次返回3个函数，分别计算1*1,2*2,3*3
def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
'''你可能认为调用f1()，f2()和f3()结果应该是1，4，9，
但实际结果全部都是 9（请自己动手验证）。
因此，返回函数不要引用任何 循环变量，或者后续会发生变化的变量。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i #不要引用任何循环变量，改成函数，见上面
        fs.append(f)
    return fs

f1, f2, f3 = count()
'''
'''
匿名函数
'''
print('-----------------------匿名函数用lambda定义-------------------------')
result = [item for item in map(lambda x: x*x,[1,2,3,4,5,6,7,8,9])]
print(result)
result_sum=reduce(lambda x,y:x+y,[1,3,5,7,9])
print(result_sum)
srt_score=sorted(['bob', 'about', 'Zoo', 'Credit'],key=lambda x:x.lower())
print(srt_score)


print('--------------------------python编写无参数的decorator----------------------')
def log(f):
    def fn(x):
        print('call '+f.__name__+'()...')
        return f(x)
    return fn
@log
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))

print('------------计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。---------------')
import time
def performance(f):
    def fn(*args,**kw):
        t1=time.time()
        r=f(*args,**kw)
        t2=time.time()
        print('call %s() in %fs' % (f.__name__,(t2-t1)))
        return r
    return fn
@performance
def factorial1(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial1(10))

def int2(x,base=2):
    return int(x,base)
'''
functools.partial就是帮助我们创建一个偏函数，
不需要我们自己定义int2，可以使用下面的代码创建一个
新的函数
'''
import functools
int2 = functools.partial(int,base=2)
int2('10000000000000000')

sorted_ignore_case = functools.partial(sorted,key=lambda item:item.lower())
sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])