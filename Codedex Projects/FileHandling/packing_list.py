import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:    
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)
        for things in reader:
            print(things)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open('packing_list.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

        
