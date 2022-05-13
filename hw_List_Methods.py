'''Lists'''
a=[1,20.5,'hello']
print(a)#[1, 20.5, 'hello']

'''List methods'''

'''append()'''
_a=[1,2,3,4]
_a.append("hello")
print(_a)#[1, 2, 3, 4, 'hello']

'''clear()'''
c=[1,2,3,4,5]
c.clear()
print(c)#[]

'''copy()'''
d=a.copy()
print(d)#[1, 20.5, 'hello']

'''count()'''
e=[1,2,1,3,4,5,6,7,1]
x=e.count(1)
print(x)#3

'''extend()'''
a.extend(d)
print(a)#[1, 20.5, 'hello', 1, 20.5, 'hello']

'''index()'''
y=a.index(20.5)
print(y)#1

'''insert()'''
a.insert(2,'python')
print(a)#[1, 20.5, 'python', 'hello', 1, 20.5, 'hello']

'''pop()'''
z=a.pop(2)
print(z)#python

'''remove()'''
a.remove(1)
print(a)#[20.5, 'hello', 1, 20.5, 'hello']

'''reverse()'''
a.reverse()
print(a)#['hello', 20.5, 1, 'hello', 20.5]

'''sort()'''
e.sort()
print(e)#[1, 1, 1, 2, 3, 4, 5, 6, 7]