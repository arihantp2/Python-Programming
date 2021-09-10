Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> s1="mysirg education services"
print(s1)
SyntaxError: multiple statements found while compiling a single statement
>>> s1="mysirg education services"
>>> s1
'mysirg education services'
>>> s1[-1]
's'
>>> s1[7:16]
'education'
>>> print(s1[7:16])
education
>>> s1[2:-2]
'sirg education servic'
>>> s1[5:23]
'g education servic'
>>> s1[-5:23]
'vic'
>>> len(s1)
25
>>> s1[-5:8]
''
>>> s1[-5:8:-1]
'vres noitacu'
>>> s1[2:23:2]
'sr dcto evc'

>>> s1
'mysirg education services'
>>> s1[24:0:-1]
'secivres noitacude grisy'
>>> s1[24::-1]
'secivres noitacude grisym'
>>> s1[len(s1)::-1]
'secivres noitacude grisym'
>>> s1[::-1]
'secivres noitacude grisym'
>>> s1.upper()
'MYSIRG EDUCATION SERVICES'
>>> s1.lower()
'mysirg education services'
>>> s1.startswith("my")
True
>>> s1.endswith("ces")
True
>>> s1.startswith("hello")
False
>>> s1.split( )
['mysirg', 'education', 'services']
>>> help(str)

>>> 