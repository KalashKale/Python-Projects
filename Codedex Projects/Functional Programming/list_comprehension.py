#Using loops normally
numbers = [1,2,3,4,5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(f'Original numbers: {numbers}')
print(f'Squared numbers: {squares}')

#Using list comprehension
squares_comprehension = [num ** 2 for num in numbers]
print(f'Original numbers: {numbers}')
print(f'Squared numbers using list comprehension: {squares_comprehension}')

numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_numbers = [num for num in numbers if num % 2 == 0]
print(f'\nGiven list: {numbers}')
print(f'Even numbers from the list: {even_numbers}')