# Python Program - Calculate Area of Circle

def calculate_radius(rad):
    radius = float(rad)
    area = 3.14 * radius * radius
    print('The area of the circle is : '+str(area))

print('Specify x to close the program! ')

while True:
    rad = input('Enter Radius of Circle : ')
    if rad == 'x':
        break
    calculate_radius(rad)
        
