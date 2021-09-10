Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple round brackets
>>> #cannot change anything in tuple so it is a immutable
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t
()
>>> t=(10)
>>> t
10
>>> type(t)
<class 'int'>
>>> t=(1,2,3)
>>> t
(1, 2, 3)
>>> t=10,20,30
>>> t
(10, 20, 30)
>>> type(t)
<class 'tuple'>
>>> l=[11,22,33,44]
>>> type(l)
<class 'list'>
>>> t=tuple(l)
>>> t
(11, 22, 33, 44)
>>> type(t)
<class 'tuple'>
>>> t=tuple(10,20,30)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t=tuple(10,20,30)
TypeError: tuple expected at most 1 argument, got 3
>>> t=tuple((10,20,30))
>>> t
(10, 20, 30)
>>> type(t)
<class 'tuple'>
>>> t=10,3.4,"ABC") #hetrogeneous data
SyntaxError: unmatched ')'
>>> t=(10,3.4,"ABC") #hetrogeneous data
>>> t
(10, 3.4, 'ABC')
>>> type(t)
<class 'tuple'>
>>> t=(10,20,30,40)
>>> t
(10, 20, 30, 40)
>>> while i < len(t):
	print(t[i)
	      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> 2+3
5
>>> while i < len(t):
	print(t[i])
	i+=1

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    while i < len(t):
NameError: name 'i' is not defined
>>> i=0
>>> while i < len(t):
	print(t[i])
	i+=1

	
10
20
30
40
>>> for x in t:
	print(x)

	
10
20
30
40
>>> for x in t:
	print(x*x)

	
100
400
900
1600
>>> t
(10, 20, 30, 40)
>>> t[0::]
(10, 20, 30, 40)
>>> t[::]
(10, 20, 30, 40)
>>> t[:]
(10, 20, 30, 40)
>>> t=t+(1,2,3)
>>> t
(10, 20, 30, 40, 1, 2, 3)
>>> t[0::2]
(10, 30, 1, 3)
>>> t[2:5]
(30, 40, 1)
>>> a=1
>>> b=2
>>> c=3
>>> t=(a,b,c) #packing
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t=(10,20,30)
>>> a,b,c=t #unpacking
>>> t
(10, 20, 30)
>>> a
10
>>> b
20
>>> c
30
>>> a=(10,20,30)
>>> b=1,2,3
>>> a+b
(10, 20, 30, 1, 2, 3)
>>> b*2
(1, 2, 3, 1, 2, 3)
>>> a*2
(10, 20, 30, 10, 20, 30)
>>> a=1,2,3
>>> b=1,2,3
>>> a==b
True
>>> a!=b
False
>>> c=1,2,4
>>> a==c
False
>>> a>b
False
>>> b<a
False
>>> a>b
False
>>> a>=b
True
>>> a=1,2,3
>>> b=1,2,4
>>> a<b
True
>>> a==b
False
>>> x=input("Enter a tuple")
Enter a tuple 1,2,3
>>> x
' 1,2,3'
>>> type(x)
<class 'str'>
>>> x=tuple(input("Enter a tuple"))
Enter a tuple1,2,3
>>> type(x)
<class 'tuple'>
>>> x
('1', ',', '2', ',', '3')
>>> x=eval(input("Enter a tuple"))
Enter a tuple1,2,3
>>> x
(1, 2, 3)
>>> type(x)
<class 'tuple'>
>>> len(x)
3
>>> x.count(1)
1
>>> x.count(10)
0
>>> x=10,20,30,40,10,20,10,20,30,40,50,10
>>> x
(10, 20, 30, 40, 10, 20, 10, 20, 30, 40, 50, 10)
>>> x.count(10)
4
>>> x.count(20)
3
>>> len(x)
12
>>> x.index(10)
0
>>> x.index(20)
1
>>> if 40 in x:
	print("index is",x.index(40))

	
index is 3
>>> max(x)
50
>>> min(x)
10
>>> sum(x)
290
>>> help(tuple)

>>> 