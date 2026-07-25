"""
向Python程序输入内容
到目前为止，我们编写的程序都是直接运行的，在运行过程中并没有接收程序外部的输入。
比如，通过Python程序，我们可以快速算出从1到100的乘法结果。
"""
while False:
    num=int(input('please input number:'))
    #注意输入的是字符串，需要转型为数字模型
    result = 1
    for i in range(1,num):
        result = result * i
    print(result)
while True:
    s=input('>>> ')
    if s=='break':
        break
    result=eval(s)
    print(result)