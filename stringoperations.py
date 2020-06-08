Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string1 = 'My name is John.'
>>> string1.startswith('My')
True
>>> string1.endswith('John')
False
>>> name = input('Enter your name:')
Enter your name:Adam
>>> if name.startswith('Adam'):
	print('Hello Admin :: '+name)
else:
	print('Hello users: '+name)

	
Hello Admin :: Adam
>>> list1 = ['John', 'Jack', 'Jane', 'Adam']
>>> ''.join(list)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ''.join(list)
TypeError: can only join an iterable
>>> ''.join(list1)
'JohnJackJaneAdam'
>>> ' '.join(list1)
'John Jack Jane Adam'
>>> ','.join(list1)
'John,Jack,Jane,Adam'
>>> string_to_split = 'The lord of the Rings'
>>> list2 = string_to_split.split()
>>> list2
['The', 'lord', 'of', 'the', 'Rings']
>>> 'Hello, how, are, you, today'.split(',')
['Hello', ' how', ' are', ' you', ' today']
>>> 'Hello, how, are, you, today'.split('a')
['Hello, how, ', 're, you, tod', 'y']
>>> multi_libne_string.split('\n')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    multi_libne_string.split('\n')
NameError: name 'multi_libne_string' is not defined
>>> multi_libne_string = '''Hello,
Do you have any plans for today?
I would like to see you...'''
>>> print(multi_libne_string)
Hello,
Do you have any plans for today?
I would like to see you...
>>> multi_libne_string.split('\n')
['Hello,', 'Do you have any plans for today?', 'I would like to see you...']
>>> name = ' John'
>>> name
' John'
>>> name = '   john'
>>> name
'   john'
>>> name.strip()
'john'
>>> name.strip('\t')
'   john'
>>> 