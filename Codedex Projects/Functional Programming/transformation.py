from functools import reduce

# map()
def half_the_number(x):
  return x/2
halved_numbers = map(half_the_number, [1,2,3,4,5])
print(list(halved_numbers))

# filter()
def even_filter(x):
  return x % 2 == 0
even_numbers = filter(even_filter, [1,2,3,4,5,6,7,8,9,10])
print(list(even_numbers))

# reduce()
def multiply(x,y):
  return x * y
multiply_elements = reduce(multiply, [1,2,3,4,5])
print(multiply_elements)