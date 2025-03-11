
class Animal:
  alive = True;

class Dog (Animal):
  def speak (self):
    print(f'{self.alive} {self.__class__.__name__} says Woof!')

class Cat (Animal):
  def speak (self):
    print(f'{self.alive} {self.__class__.__name__} says Meow!')

class Car:
  def speak(self):
    pass

if __name__ == "__main__":

  animals = [Dog(), Cat(), Car()]
  for animal in animals:
    animal.speak()