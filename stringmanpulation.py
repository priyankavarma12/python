Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = 'Hello'
>>> string2 = "Hello"
>>> string == string2
True
>>> string3 = "I'm good today."
>>> string3
"I'm good today."
>>> string3 = 'I\'m good today.'
>>> string3 = 'I\"m good today.'
>>> string3
'I"m good today.'
>>> string4 = '\tHello'
>>> string4
'\tHello'
>>> string4 = 'Hello\tWorld'
>>> string4
'Hello\tWorld'
>>> print(string4)
Hello	World
>>> string5 = 'Today\tis\ta\tgood\tday.'
>>> print(string5)
Today	is	a	good	day.
>>> string6 = 'Hello\nWorld!'
>>> print(string6)
Hello
World!
>>> string7 = 'Hello\\ World'
>>> print(string7)
Hello\ World
>>> print("What is your name?\nHow old are you?\n\t I\'m 20 years old!")
What is your name?
How old are you?
	 I'm 20 years old!
>>> string8 = '''Hello There
My name is Adam
I am 20 years old
And I like to play Table tennis '''
>>> print(string8)
Hello There
My name is Adam
I am 20 years old
And I like to play Table tennis 
>>> string = "hello"
>>> string[0]
'h'
>>> string[0:3]
'hel'
>>> string[-1]
'o'
>>> string[:3]
'hel'
>>> string[3:]
'lo'
>>> 'Today is a nice day'
'Today is a nice day'
>>> 'Today' in 'Today is a nice day'
True
>>> string1 = 'Today is a nice day'
>>> string2 = 'Today'
>>> string2 in string1
True
>>> 'TODAY' in 'Today is a nice day'
False
>>> 'Tomorrow' in 'Today is a nice day'
False
>>> 'tomorrow' not in 'Today is a nice day'
True
>>> string = 'today'
>>> string.upper()
'TODAY'
>>> string2 = 'TODAY'
>>> string1 = 'Today is a nice day'
>>> string2.lower() in string1
False
>>> string2.lower()
'today'
>>> string2.upper() in string1.upper
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    string2.upper() in string1.upper
TypeError: argument of type 'builtin_function_or_method' is not iterable
>>> string2.upper() in string1.upper()
True
>>> name = input('Enter your name : ')
Enter your name : Adam
>>> print(name)
Adam
>>> print(name.upper())
ADAM
>>> print(name.lower())
adam
>>> name.islower()
False
>>> name.isupper()
False
>>> 