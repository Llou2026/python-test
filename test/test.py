import tools
import sys
print('----')
print(sys.path)
print('----')
from math import pi as PI
from math import sin,cos
print(sin(0))
print(cos(0))
print(PI)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(tools.__file__)
tools.say_hello()
tools.say_goodbye()
#tools.say_hello()
class Person:
    __slots__=('name','sex','age')
    def __init__(self,name,sex,age,**kw):
        self.name=name
        self.sex=sex
        self.age=age
        
    def __str__(self):
       return 'name:{},sex:{},age:{}'.format(self.name,self.sex,self.age)
    def __len__(self):
        return len(self.name)
    def __call__(self, args):
        print('My name is {}...'.format(self.name))
        print('My friend is {}...'.format(args))
p = Person('Bob','girl',20)
p('Alice')
print('#######################################################################')
class Student(Person):
    __slots__=('name','sex','age')
    def __init__(self, name, sex, age, **kw):
        super().__init__(name, sex, age, **kw)

    def who(self):
        return 'I\'m student.'
student = Student('Tony','boy',20)
print('-------------------------------')
#student.score=99  
#print(student.score)
print('-------------------------------')
student.who()
print(str(student))
print(len(student))
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
class Rational:
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def __add__(self, r):
        print('----------------')
        print('{}*{} + {}*{},{}*{}'.format(self.p,r.q,self.q,r.p,self.q,r.q))
        print('---------------')
        return Rational(self.p * r.q + self.q *r.p, self.q * r.q)
    def __sub__(self,r):
        return Rational(self.p*r.q-self.q*r.p,self.q*r.q)
    def __mul__(self,r):
        return Rational(self.p*r.p,self.q*r.q)
        # return Rational(self.p * r.p, self.q * r.q)
    def __truediv__(self, r):
        return Rational(self.p*r.q,self.q*r.p)
    def __str__(self):
        g = gcd(self.p,self.q)
        return '{}/{}'.format(int(self.p/g),int(self.q/g))
        # return '{}/{}'.format(self.p, self.q)
r1=Rational(1,2)
r2=Rational(1,5)
print(r1+r2)
print(r1-r2)
print(r1*r2)
print(r1/r2)
class Fib:
    def __init__(self):
        self.res=[]
    def __call__(self, num):
        a = 0
        b = 1
        for x in range(num):
            self.res.append(a)
            a,b=b,a+b
        return self.res
f=Fib()
a=list(range(10))
print(a)
print(f(10))