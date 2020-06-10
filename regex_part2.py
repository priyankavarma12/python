#Python Program for regex_part2

import re

our_regex = re.compile(r'^Hello')
print(our_regex.search('Hello World'))

our_regex.search('World Hello')
endswith = re.compile(r'\d$')
print(endswith.search('The Number of apples on table is 4'))

our_regex = re.compile(r'.ad')
print(our_regex.findall('Bad Sad Dad Glad Mad Had'))

                       
string = 'Twelve:12 Eight nine:89.'
pattern = '/d+'
result = re.split(pattern, string)
print(result)

pattern = '\d+'
result = re.split(pattern, string)
print(result)

string = 'Twelve:12 Eight nine:89 Nine:9'
pattern = '\d+'
result = re.split(pattern, string,1)
print(result)

string = 'abc 12\
de 23 \n f45 6'
print(string)
pattern = '\s+' #whitespace char
replace = '' # empty string
new_string = re.sub(pattern, replace, string)
print(new_string)


string = 'abc12\
de 23\n f45 6'
new_string = re.sub(pattern, replace, string, 1)
print(new_string)

new_string = re.sub(pattern, replace, string, 2)
print(new_string)

new_string = re.sub(pattern, replace, string, 3)
print(new_string)

string = 'abc 12\
de 23\n f45 6'
pattern = '\s+'
replace = ''
new_string = re.subn(pattern, replace, string)
print(new_string)
