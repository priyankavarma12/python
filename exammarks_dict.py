#Python program - Exam Marks using dictionary, Values, Index, get


exam_marks = {'John':'A','Jack':'D','Janes':'B','Adams':'F'}
age_person = {'John':30,'Jack':35,'Janes':31,'Adams':45}

    
def check_name_of_person(person_name):
    if person_name == None:
        exit()

    if person_name in exam_marks:
        print('Exam Marks for '+ person_name + ' is '+ exam_marks[person_name])
    else:
        print('Cant seem to find the results for '+ person_name)


def values_from_dict():
    for value in age_person.values():
        print(value)

def keys_from_dict():
    for key in age_person.keys():
        print(key)

def item_from_dict():
    for item in age_person.items():
        print(item)

def age_of_person():
    for person,age in age_person.items():
        print('The Age of '+ person + ' is : '+str(age))

def get_age_person():
    print('The Age of '+ person_name + ' is '+str(age_person.get(person_name, 0)) + ' years.')
        
print('Enter A name of A Person you want to check the exam marks ::')
person_name = input('Name : ')
check_name_of_person(person_name)


print('Values from dictionary of age person :: ')
values_from_dict()        


print('Keys from dictionary of age person :: ')
keys_from_dict()

print('Items from Dictionary :: ')
item_from_dict()

age_of_person()

person_name = input('Enter name :')
get_age_person()

