Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #sets
>>> #No duplicate values
>>> #curly brackets
>>> #no indexing
>>> #no slicing
>>> s={10,20,30}
>>> s
{10, 20, 30}
>>> type(s)
<class 'set'>
>>> s=1,,3,2,2,3,1,2,3,3,3
SyntaxError: invalid syntax
>>> s=1,3,2,2,3,1,2,3,3,3
>>> s
(1, 3, 2, 2, 3, 1, 2, 3, 3, 3)
>>> s={1,3,2,2,3,1,2,3,3,3}
>>> s
{1, 2, 3}
>>> s=set()
>>> s
set()
>>> s=set(10)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s=set(10)
TypeError: 'int' object is not iterable
>>> s=set(10,20,30)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s=set(10,20,30)
TypeError: set expected at most 1 argument, got 3
>>> s=set([10,20,30])
>>> s
{10, 20, 30}
>>> type(s)
<class 'set'>
>>> s=set(""Arihant)
SyntaxError: invalid syntax
>>> s=set("Arihant")
>>> s
{'A', 'r', 'i', 't', 'n', 'a', 'h'}
>>> l=[10,20,10,30,20]
>>> l
[10, 20, 10, 30, 20]
>>> s=set(l)
>>> s
{10, 20, 30}
>>> s=set([10])
>>> s
{10}
>>> s.add(20,30,40)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.add(20,30,40)
TypeError: add() takes exactly one argument (3 given)
>>> s.add(20)
>>> s
{10, 20}
>>> s.add([20,30,40])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.add([20,30,40])
TypeError: unhashable type: 'list'
>>> s.add("hello)
      
SyntaxError: EOL while scanning string literal
>>> s.add("hello")
>>> s
{'hello', 10, 20}
>>> s={1,2,3}
>>> l={1,3,5,7}
>>> s.update(l)
>>> s
{1, 2, 3, 5, 7}
>>> s.update([3,5,9],(5,6,7,8))
>>> s
{1, 2, 3, 5, 6, 7, 8, 9}
>>> s.discard(4)
>>> s
{1, 2, 3, 5, 6, 7, 8, 9}
>>> s.remove(4)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.remove(4)
KeyError: 4
>>> s.discard(9)
>>> s
{1, 2, 3, 5, 6, 7, 8}
>>> s1={1, 2, 3, 5, 6, 7, 8}
>>> s2={2,3,5,7}
>>> s1.intersection(s2)
{2, 3, 5, 7}
>>> s1.clear()
>>> s1
set()
>>> s1.union(s2)
{2, 3, 5, 7}
>>> s1={1,2,3,4}
>>> s2={2,3}
>>> s2.issubset(s1)
True
>>> s1.issuperset(s2)
True
>>> s1.pop()
1
>>> #pop removes random element
>>> a=s1.copy()
>>> a
{2, 3, 4}
>>> s1
{2, 3, 4}
>>> id(a)
52490840
>>> id(s1)
52491288
>>> 