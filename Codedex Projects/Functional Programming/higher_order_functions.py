def apply_operation(operation, number):   #takes an operation and numbers
    result = []
    for num in number:
        result.append(operation(num))
    return result

def double(x):                             #defining an operation
    return x * 2

numbers_list = [1,2,3,4,5]

doubled_numbers = apply_operation(double, numbers_list) #giving operation and numbers

print('Numbers list: ', numbers_list)
print('Doubled numbers: ', doubled_numbers)