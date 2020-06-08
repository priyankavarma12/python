import os

os.chdir('C:\\Users\\Priyanka_Varma\\Desktop\\Folder1')

try:
    fd = open('nonexistingfile')
    fd.write('Some strings ')
except:
    print('File Doesnt Exist! ')
else:
    print('Everything Worked Fine! ')
