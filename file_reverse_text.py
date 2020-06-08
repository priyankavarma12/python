import os

os.chdir('C:\\Users\\Priyanka_Varma\\Desktop')

file_name = 'textfile.txt'
fn = open(file_name, 'r')

for line in fn.readlines():
    line = line.strip('\n')
    line = line[::-1]
    print(line)
    fn.close()
    fn = open(file_name, 'a')
    line = line + '\n'
    fn.write(line)
    fn.close()
    fn = open(file_name, 'r')

fn.close()    
