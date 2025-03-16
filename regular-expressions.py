import re

if __name__ == "__main__":
  words = ["First", "Second", "Third", "Forth", "Fifth"]
  for word in words:
    if re.search("t", word):
      print (f'Search {word} Found')

  for word in words:
    if re.match("t", word):
      print (f'Match {word} Found')
  
  numbers_starting_with_f = re.findall("\d+", "One 1, Two 2, Three 3, Four 4, Five 5")
  for number in numbers_starting_with_f:
    print (f'Number {number} Found')