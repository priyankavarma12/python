import os

os.chdir('C:\\Users\\Priyanka_Varma\\Desktop\\Folder1')

try:
    fd = open('nonexistingfile.txt','w')
    fd.write('Some strings ')
    fd.close()
except:
    print('File Doesnt Exist! ')
else:
    print('Everything Worked Fine! ')
