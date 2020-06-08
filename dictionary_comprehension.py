Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dcitionary1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
>>> double_dict = {k:v*2 fro (k,v) in dcitionary1.items()}
SyntaxError: invalid syntax
>>> double_dict = {k:v*2 for (k,v) in dcitionary1.items()}
>>> double_dict
{'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
>>> double_dict = {k*2:v for (k,v) in dcitionary1.items()}
>>> double_dict
{'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4, 'ee': 5}
>>> numbers =  range(10)
>>> numbers
range(0, 10)
>>> for n in numbers:
	if n%2 == 0
	
SyntaxError: invalid syntax
>>> for n in numbers:
	if n%2 == 0:
		new_dict[n] =  n**2

		
Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    new_dict[n] =  n**2
NameError: name 'new_dict' is not defined
>>> new_dict = {}
>>> for n in numbers:
	if n%2 == 0:
		new_dict[n] = n**2

		
>>> print(new_dict)
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
>>> dictionary1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
>>> dictionary2 = {k:v for (k,v) in dictionary1.items() if v>2}
>>> dictionary2
{'c': 3, 'd': 4, 'e': 5}
>>> dictionary3 = {k:v for (k,v) in dictionary1.items() if v>2 if v%2 == 0 }
>>> dictionary3
{'d': 4}
>>> dictionary3 = {k:v for (k,v) in dictionary1.items() if v>2 if v%2 == 1 }
>>> dictionary3
{'c': 3, 'e': 5}
>>> 