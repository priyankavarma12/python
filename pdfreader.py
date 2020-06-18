Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import PyPDF2
>>> pdfFileObj = open('pdfile.pdf', 'rb')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pdfFileObj = open('pdfile.pdf', 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'pdfile.pdf'
>>> pdfFileObj = open('C:\Users\Priyanka_Varma\Desktop\Folder1\pdfile.pdf', 'rb')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> pdfFileObj = open('C://Users//Priyanka_Varma//Desktop//Folder1//pdfile.pdf', 'rb')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pdfFileObj = open('C://Users//Priyanka_Varma//Desktop//Folder1//pdfile.pdf', 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'C://Users//Priyanka_Varma//Desktop//Folder1//pdfile.pdf'
>>> pdfFileObj = open('C://Users//Priyanka_Varma//Desktop//Folder1//pdf.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> print(pdfReader.numPages)
5
>>> pageObj = pdfReader.getPAge(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pageObj = pdfReader.getPAge(0)
AttributeError: 'PdfFileReader' object has no attribute 'getPAge'
>>> pageObj = pdfReader.getPage(0)
>>> print(pageObj)
{'/Type': '/Page', '/MediaBox': [0, 0, 612, 792], '/Rotate': 0, '/Parent': IndirectObject(3, 0), '/Resources': {'/ProcSet': ['/PDF', '/Text'], '/ExtGState': IndirectObject(41, 0), '/Font': IndirectObject(42, 0)}, '/Annots': [IndirectObject(13, 0), IndirectObject(14, 0), IndirectObject(15, 0), IndirectObject(16, 0), IndirectObject(17, 0), IndirectObject(18, 0), IndirectObject(19, 0), IndirectObject(20, 0), IndirectObject(21, 0), IndirectObject(22, 0), IndirectObject(23, 0), IndirectObject(24, 0), IndirectObject(25, 0), IndirectObject(26, 0)], '/Contents': IndirectObject(30, 0)}
>>> print(pagrObj.extractText)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(pagrObj.extractText)
NameError: name 'pagrObj' is not defined
>>> print(pageObj.extractText)
<bound method PageObject.extractText of {'/Type': '/Page', '/MediaBox': [0, 0, 612, 792], '/Rotate': 0, '/Parent': IndirectObject(3, 0), '/Resources': {'/ProcSet': ['/PDF', '/Text'], '/ExtGState': IndirectObject(41, 0), '/Font': IndirectObject(42, 0)}, '/Annots': [IndirectObject(13, 0), IndirectObject(14, 0), IndirectObject(15, 0), IndirectObject(16, 0), IndirectObject(17, 0), IndirectObject(18, 0), IndirectObject(19, 0), IndirectObject(20, 0), IndirectObject(21, 0), IndirectObject(22, 0), IndirectObject(23, 0), IndirectObject(24, 0), IndirectObject(25, 0), IndirectObject(26, 0)], '/Contents': IndirectObject(30, 0)}>
>>> pageObj = pdfReader.getPage(1)
>>> print(pageObj.extractText)
<bound method PageObject.extractText of {'/Type': '/Page', '/MediaBox': [0, 0, 612, 792], '/Rotate': 0, '/Parent': IndirectObject(3, 0), '/Resources': {'/ProcSet': ['/PDF', '/ImageC', '/Text'], '/ExtGState': IndirectObject(57, 0), '/Font': IndirectObject(58, 0)}, '/Annots': [IndirectObject(43, 0)], '/Contents': IndirectObject(47, 0)}>
>>> 

