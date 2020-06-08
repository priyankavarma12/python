Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\AppData\\Local\\Programs\\Python\\Python38-32'
>>> os.chdir('C:\\Users\\Priyanka_Varma\\Desktop')
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\Desktop'
>>> os.path.abspath('Folder1')
'C:\\Users\\Priyanka_Varma\\Desktop\\Folder1'
>>> file_path = "C:\\Users\\Priyanka_Varma\\Desktop\\Folder1\\file.txt"
>>> os.path.basename(file_path)
'file.txt'
>>> os.path.dirname(file_path)
'C:\\Users\\Priyanka_Varma\\Desktop\\Folder1'
>>> os.path.split(file_path)
('C:\\Users\\Priyanka_Varma\\Desktop\\Folder1', 'file.txt')
>>> directory, filename = os.path.split(file_path)
>>> print('The Path to the file: '+ filename + 'is at this path : '+ directory)
The Path to the file: file.txtis at this path : C:\Users\Priyanka_Varma\Desktop\Folder1
>>> os.path.getsize(file_path)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.path.getsize(file_path)
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\Priyanka_Varma\\Desktop\\Folder1\\file.txt'
>>> os.path.getsize(file_path)
11
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\Desktop'
>>> file = open('\\Folder1\\file.txt')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    file = open('\\Folder1\\file.txt')
FileNotFoundError: [Errno 2] No such file or directory: '\\Folder1\\file.txt'
>>> os.chdir('C:\\Users\\Priyanka_Varma\\Desktop\\Folder1')
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\Desktop\\Folder1'
>>> file = open('file.txt')
>>> file.close()
>>> fn = open('file.txt', 'r')
>>> fn.read()
'Hello world'
>>> fn.write('Hello everyone')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fn.write('Hello everyone')
io.UnsupportedOperation: not writable
>>> fn.close()
>>> fn.open('file.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fn.open('file.txt', 'w')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> fn = open('file.txt', 'w')
>>> fn.read()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fn.read()
io.UnsupportedOperation: not readable
>>> string = 'Hello everyone !!'
>>> fn.write(string)
17
>>> fn.close()
>>> fn.close()
>>> fn = open('file.txt', 'a')
>>> fn.write(' How is your day today ? ')
25
>>> fn.close()
>>> fn = open('file.txt', 'rt')
>>> fn.read()
'Hello everyone !! How is your day today ? '
>>> fn.close()
>>> file_name = 'file.txt'
>>> fn = open(file_name, 'r')
>>> for line in fn.readlines():
	print(line)

	
Hello everyone !! How is your day today ? 

Jack

John

Jill

Jey

Jenny

>>> fn.read()
''
>>> fn.close()
>>> fn = open(file_name, 'r')
>>> for line in fn.readlines():
	line = line.strip('\n')
	print(line)

	
Hello everyone !! How is your day today ? 
Jack
John
Jill
Jey
Jenny
>>> 