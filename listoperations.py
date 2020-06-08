#Python Program for list - Append, Insert, Remove and Sort elements

print('List of Dairy Products :: ')
list = ['milk','cheese','ham','soda']
number_list = [-3,12,3,4,0]
def print_values():
    for i in list:
        print(i)
    for j in number_list:
        print(j)

list.append('water')
list.insert(2,'apple')
list.insert(0,'carrot')
list.remove('soda')
number_list.remove(4)
list.sort()
number_list.sort()
print_values()

print('Index of elements '+str(list.index('carrot')))    
