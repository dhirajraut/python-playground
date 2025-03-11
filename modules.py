from math import sqrt
from random import randint
from datetime import datetime

if __name__ == "__main__":

  print (f'Root of 9 is {sqrt(9)}')

  for i in range (10):
    print (f'Random number between 1 to 10 (inclusive) is {randint(1, 10)}')

  print (f'Current time is {datetime.now()}')
  print (f'Current UTC time is {datetime.utcnow()}')