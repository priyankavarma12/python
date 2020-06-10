#Python Program for regex 

import re

Regex = re.compile(r'Hello|World')
string = 'Hello World'
first_match = Regex.search(string)
print(first_match.group())

string1 = "World Hello"
second_match = Regex.search(string1)
print(second_match.group())

our_regex = re.compile(r'bas(ket)?ball')
string1 = 'The are playing basball'
match1 = our_regex.search(string1)
print(match1.group())


string2 = 'They are playing basketball'
match2 = our_regex.search(string2)
print(match2.group())


phone_number = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
match1 = phone_number.search('My number is 065-555-5555. ')
print("Number1 - ", match1.group())


match2 = phone_number.search('My number is 555-5555')
print(match2.group())

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
allmatch = phone_number.findall('I have 2 phone numbers : 065-555-5555 and 555-555-5555')
print('all matches : ',allmatch)

string = 'HelloHelloHello there'
regex = re.compile(r'{Hello}{3}')
match = regex.search(string)
print(match)

vowelRegex = re.compile(r'[aeiouAEIOU]')
string = 'Today is a really nice dAy'
print(vowelRegex.findall(string))

different_regex = re.compile(r'[\w+]')
print(different_regex.findall(string))

