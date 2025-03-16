
def order_by_price(item: tuple):
  return item[1]

if __name__ == "__main__":
  original_products = [("banana", 5.95), ("apple", 3.95), ("grapes", 4.50), ("watermelon", 4.95)]
  print (f'Original List - {original_products}')

  # Passing a function.
  sorted_by_price = original_products.copy()
  sorted_by_price.sort (key=order_by_price)
  print (f'Sorted by price passing a function - {sorted_by_price}')

  # Passing a labda
  sorted_by_name = original_products.copy()
  sorted_by_name.sort (key=lambda item: item[0])
  print (f'Sorted by name using lambda - {sorted_by_name}')

  sorted_by_name_last_character = original_products.copy()
  sorted_by_name_last_character.sort(key=lambda item: item[0][-1])
  print (f'Sorted by name last character using lambda - {sorted_by_name_last_character}')

  # MAP function.
  string_list = ["1", "2", "3", "4"]
  integer_map = map (lambda x: int(x), string_list)
  print(f'{integer}' for integer in integer_map)
  for integer in integer_map:
     print (f'Map output: {integer}')

  # FILTER function.
  integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  def is_even(number):
    return True if number % 2 == 0 else False
  even_numbers = filter (is_even, integers)
  for integer in even_numbers:
     print (f'Filter output: {integer}')

  # REDUCE function.
  from functools import reduce
  integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  sum = reduce (lambda sum, integer: sum + integer, integers, 10)
  print (f'{sum}')