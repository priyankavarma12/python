#python Program to extract the email

import re

file = open('C://Users//Priyanka_Varma//Desktop//Folder1//emaildata.txt')
file_text = file.read()

match = re.findall(r'[\w.-]+@[\w\.]+', file_text)
print(match)
