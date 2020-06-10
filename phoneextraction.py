#Python Program to extract the useful data with regex

import re

#extarcting phoneno
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
string = "My Phone number is 111-222-1323"
match = phoneNumber.search(string)
print(match)

print('Found a phone number : '+ match.group())

string1 = '''in this string
we have a phone number
which is 111-222-3333
and we have another phone number
which is 4444-444-4444'''

match2 = phoneNumber.search(string1)
print(match2.group())


#split the phone number by codes

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phoneNumber.search('His Phone number is 444-666-6546.')
print(match.group(1))
print(match.group(2))
print(match.group())
print(match.group(0))
