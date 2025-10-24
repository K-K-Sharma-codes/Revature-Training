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
print('hi' + '10')
hi10
print('Sum : ' + num1+10)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print('Sum : ' + num1+10)
TypeError: can only concatenate str (not "int") to str
print('Sum : ' , num1+10)
Sum :  20
print('Sum : ' + '/n' , num1+10)
Sum : /n 20
print('Sum : ' + '\n' , num1+10)
Sum : 
 20
input()
5
'5'
input()
hi
'hi'
input()
True
'True'
input('Enter a number ')
Enter a number 5
'5'
input('Enter a num : ')
Enter a num : 10
'10'
int(input('Enter a num : '))
Enter a num : 5
5
float(input('Enter a num : '))
Enter a num : 5.0
5.0
bool(input('Enter a num : '))
Enter a num : 5
True
bool(input('Enter a num : '))
Enter a num : 0
True
'hi'
'hi'
"hi"
'hi'
"Ram's house"
"Ram's house"
str1= 'hello there !'
str1
'hello there !'
len(str1)
13
str1[0]
'h'
str1[10]
'e'
str[12]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    str[12]
TypeError: type 'str' is not subscriptable
str1[12]
'!'
str1[11]
' '
str1[-5]
'e'
str1[-7]
't'
str1[-13]
'h'
str1[-14]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str1[-14]
IndexError: string index out of range
str1[o:3]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    str1[o:3]
NameError: name 'o' is not defined
str1[0:3]
'hel'
str1[5:10]
' ther'
str1[5:]
' there !'
str1[0:10:1]
'hello ther'
str1[0:10:2]
'hlote'
str1[0:10:3]
'hltr'
str[0::3]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str[0::3]
TypeError: type 'str' is not subscriptable
str1[0::3]
'hltr!'
str1[0::4]
'hoe!'
str1[:4]
'hell'
str1[-9:-5]
'o th'
str1[-10:-1:2]
'l hr '



str1
'hello there !'
str1.capitalize()
'Hello there !'
str1.upper()
'HELLO THERE !'
str1.count('h')
2
str1.count('e')
3


str1.endswith('!')
True
str1.endswith('h')
False
str1.find('t')
6
str1.find('s')
-1
str1.index('t')
6
str1.index('s')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    str1.index('s')
ValueError: substring not found
str1.encode('utf-8')
b'hello there !'
str1.encode('utf-16')
b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00t\x00h\x00e\x00r\x00e\x00 \x00!\x00'
str1.replace('o' , '0')
'hell0 there !'
str1.split()
['hello', 'there', '!']
numbers=[10, 20, 30]
numbers
[10, 20, 30]
id(numbers)
2647919452224
numbers.append(40)
numbers
[10, 20, 30, 40]
id(numbers)
2647919452224
numbers.append(40)
numbers
[10, 20, 30, 40, 40]
numbers[2]
30
numbers[3]=100
numbers
[10, 20, 30, 100, 40]
numbers.count(20)
1
numbers.index(100)
3
numbers.insert(2, 600)
numbers
[10, 20, 600, 30, 100, 40]
numbers.remove(600)
numbers
[10, 20, 30, 100, 40]
numbers.remove(60)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    numbers.remove(60)
ValueError: list.remove(x): x not in list
numbers.pop()
40
numbers.pop(-2)
30
numbers
[10, 20, 100]
numbers.reverse()
numbers
[100, 20, 10]
numbers.sort()
numbers
[10, 20, 100]
numbers.sort(reverse=True)
numbers
[100, 20, 10]
numbers.extend()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    numbers.extend()
TypeError: list.extend() takes exactly one argument (0 given)
nums1=numbers
id(nums1)
2647919452224
numbers.extend(nums)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    numbers.extend(nums)
NameError: name 'nums' is not defined. Did you mean: 'num1'?
numbers.clear()
numbers
[]
tup1=(10, 20, 30)
tup1
(10, 20, 30)
tup1[2]
30
tup1.count(10)
1
tup1.clear()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    tup1.clear()
AttributeError: 'tuple' object has no attribute 'clear'
tup1.index(20)
1
set1={22, 11, 33, 55, 9, 7}
set1
{33, 55, 22, 7, 9, 11}
set1(2)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    set1(2)
TypeError: 'set' object is not callable
set1[2]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
set1.add(43)
set1
{33, 55, 22, 7, 9, 11, 43}
set1
{33, 55, 22, 7, 9, 11, 43}
set2={100, 200, 300}
set2
{100, 300, 200}
set1.union(set2)
{33, 100, 7, 200, 9, 11, 43, 300, 22, 55}
set3=set1.union(set2)
set3
{33, 100, 7, 200, 9, 11, 43, 300, 22, 55}
set3.intersection(set2

                  0
                  
SyntaxError: '(' was never closed
set3.intersection(set2)
                  
{200, 100, 300}
set4=set3.intersection(set2)
                  
set4
                  
{200, 100, 300}
set5=set1.difference(set4)
                  
set5
                  
{33, 7, 9, 11, 43, 22, 55}
>>> set1.discard(33)
...                   
>>> set1
...                   
{55, 22, 7, 9, 11, 43}
>>> dic1={1:10, 2:20}
...                   
>>> dic1
...                   
{1: 10, 2: 20}
>>> dict1[2]
...                   
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    dict1[2]
NameError: name 'dict1' is not defined. Did you mean: 'dic1'?
>>> dic1[2]
...                   
20
>>> dic1[2]=200
...                   
>>> dic1
...                   
{1: 10, 2: 200}
>>> dic2={'rno':'123' , 'name':'Krishna'}
...                   
>>> dic2
...                   
{'rno': '123', 'name': 'Krishna'}
>>> dic2['rno']
...                   
'123'
>>> dic2.keys
...                   
<built-in method keys of dict object at 0x00000268844DC800>
>>> dic2.keys()
...                   
dict_keys(['rno', 'name'])
>>> dic2.values()
...                   
dict_values(['123', 'Krishna'])
