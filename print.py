
# Generic Print Statement
print('Hi Dhiraj')

# Print with quotes
print('My name is "Dhiraj"') 
# or
print("My name is 'Dhiraj'")

# Print Repeated
print('-' * 10)

# Print Substring
line = "This is a very long line."
print("The first letter of the above line is : " + line[0])
print("The first 6 letters of the above line are : " + line[0:6])
print("The first 12 letters of the above line are : " + line[:12])
print("The line after skipping 3 letters is : " + line[3:])

# Print with variable substitutions
name = 'Dhiraj'
line = "This is a very long line."
print(f'{name}, {line}')

# Print find in string
token = 'very'
contains = token in line
print (f'Does the token {token} present in line {line}?: {contains}')

# Print current method name
print (f'{__name__}')
