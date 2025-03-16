
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
