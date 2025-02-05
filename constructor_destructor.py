class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(f'{self.name} is being created')

  def __del__(self):
    print(f'{self.name} has been deleted')

p = Person('Dhiraj', 44) 