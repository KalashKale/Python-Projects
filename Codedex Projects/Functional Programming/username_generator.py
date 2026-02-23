import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(suffix):
  return suffix.capitalize()
capital_suffix = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, capital_suffix) for names in range(10)]

def fire_in_name(name):
  return True if 'Fire' in name else False

def concatenate_names(name1, name2):
  return name1 + ', ' + name2

fire_names = list(filter(fire_in_name, random_names))
reduced_names = reduce(concatenate_names, fire_names)

def display_name_info():
  print('Fantasy names:')
  for name in random_names:
    print(name)
  print('\nNames containing Fire:')
  print(fire_names)
  print('\nConcatenated names: ')
  print(reduced_names)

display_name_info()