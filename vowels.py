# Python program - Remove Vowel from Specified String

def remove_vowels(input_string):
  vowels = ('a','e','i','o','u')
  for c in input_string.lower():
        if c in vowels:
            newStr = input_string.replace(c,'')
  return newStr

print('Enter x for exit. ')
input_string = input('Enter any string to removal all vowels from it :')
if input_string == 'x':
    exit()
else:
    
    print('Removing Vowels from the given String ...')
    newStr = remove_vowels(input_string)  
    print('The New String after successfully removing all the vowels : '+newStr)
    
