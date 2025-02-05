print('Hi Dhiraj')
print('-' * 10)

line = "This is a very long line."
print("The first letter of the above line is : " + line[0])
print("The first 6 letters of the above line is : " + line[0:6])
print("The line after skipping 3 letters is : " + line[3:])

name = 'Dhiraj'
print(f'{name}, {line}')

contains = 'very' in line
print (contains)

print (f'{__name__}')
