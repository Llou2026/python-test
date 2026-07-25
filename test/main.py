names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
scores = [45, 60, 75, 86, 49]
index = 0
for name in names:
    score = scores[index]
    print('name = {1}, score = {2},index = {0}'.format(name, score,index))
    index = index + 1



d = {'Alice': 45,'Bob': 60,'Candy': 75,'David': 86,'Ellena': 49,'list':[20,89]}
alice=d['list'][0]
print(alice)
print(id(d['Alice']))
print(id(alice))
alice=1000000000
print(d)

