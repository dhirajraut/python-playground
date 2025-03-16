from collections import defaultdict

if __name__ == "__main__":

  # Lists
  points = [10, 9, 10, 8, 7, 7, 10, 7]
  # Print element
  print (f'Original - {points}')

  # Iterating over a collection.
  for point in points:
    print(f'Regular loop {point}')
  [print (f'Comprehension print {point}') for point in points]

  print (f'Accessing specific element - {points[1]}')
  print (f'Max - {max(points)}')
  points.insert(1, 10)
  print (f'Inserting at location 1 - {points}')
  points.remove(10)
  print (f'Removed inserted - {points}')
  points.sort()
  print (f'Sorted - {points}')
  points.append ([4, 5]) # Makes [..., x, [4, 5]]
  print (f'Appened - {points}')
  points.extend ([4, 5]) # Makes [..., 4, 5]
  print (f'Extended - {points}')
  # breakpoint()
  points[2:3] = [2, 3]
  print (f'Replacing multiple indexes - {points}')

  points.clear()
  print (f'Cleared - {points}')

  # Dictionary
  staff = {"first_name": "Dhiraj", "last_name": "Raut", "profession": "Software"}
  print (f'Original - {staff}')

  staff[(10,20)] = "Unknown Value" # Touples are immutable.
  print (f'After adding touple in Dictionary - {staff}')
  staff[(10,20,30)] = "Unknown Value" # Touples are immutable.
  print (f'After adding touple in Dictionary - {staff}')

  del staff["profession"]
  print (f'After deletion - {staff}')
  deleted = staff.pop("Name", "Not Found")
  print (f'After pop - {staff}, deleted - {deleted}')
  deleted = staff.pop("first_name", "Not Found")
  print (f'After pop - {staff}, deleted - {deleted}')

  citiMap = defaultdict(list)
  citiMap["US"] = ["New York", "DC"]
  citiMap["Canada"] = ["Toronto"]
  citiMap["India"] = ["Mumbai"]

  print(citiMap.keys())
  print(citiMap.values())
  