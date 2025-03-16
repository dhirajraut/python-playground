from math import sqrt

if __name__ == "__main__":

  print (sqrt(9))

  # Quadratic Equation
  a = int (input("Enter value of a (sample 1): "))
  b = int (input("Enter value of b (sample 2): "))
  c = int (input("Enter value of c (sample -8): "))
  b_sq = b ** 2
  four_a_c = 4 * a * c
  root1 = ((0 - b) + sqrt (b_sq - four_a_c))/ (2 * a)
  root2 = ((0 - b) - sqrt (b_sq - four_a_c))/ (2 * a)
  print (f'Root 1 = {root1}, root 2 = {root2}')