Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5>6 and 3<7
False
7&9
1
7|9
15
7^9
14
not 6
False
not -6
False
5<<3
40
5<<4
80
5>>2
1
5>>>2
SyntaxError: invalid syntax
5<<<3
SyntaxError: invalid syntax
num1=10
type(num1)
<class 'int'>
num is int
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    num is int
NameError: name 'num' is not defined. Did you mean: 'num1'?
num1 is int
False
type(5) is int
True
type(num1) is int
True
type(num1) is not str
True
print(num1)
10
num1
10
print('hi')
hi
'hi'
'hi'
print('hi' + 'hello')
hihello
print(num1+10)
20
print(num1+'10')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(num1+'10')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
KeyboardInterrupt
>>> print('hi' + '10')
hi10
>>> print('Sum : ' + num1+10)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print('Sum : ' + num1+10)
TypeError: can only concatenate str (not "int") to str
>>> print('Sum : ' , num1+10)
Sum :  20
>>> print('Sum : ' + '/n' , num1+10)
Sum : /n 20
>>> print('Sum : ' + '\n' , num1+10)
Sum : 
 20
>>> input()
5
'5'
>>> input()
hi
'hi'
>>> input()
True
'True'
>>> input('Enter a number ')
Enter a number 5
'5'
>>> input('Enter a num : ')
Enter a num : 10
'10'
>>> int(input('Enter a num : '))
Enter a num : 5
5
>>> float(input('Enter a num : '))
Enter a num : 5.0
5.0
>>> bool(input('Enter a num : '))
Enter a num : 5
True
>>> bool(input('Enter a num : '))
Enter a num : 0
True
