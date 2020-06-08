#Python program - File Creating, Appending Text and creating Multiple file and appending the text

import os

directory = input('Enter Directory (Use \\\ To separate directory): ')
directory = directory.strip('\n')

os.chdir(directory)
file_name = input('Enter the name of the file that you want to create : ')

content_of_file = 'Hello!\nHow was your day ?\nMy Day was great!'

fn =open(file_name,'wt')
fn.write(content_of_file)
fn.close()
