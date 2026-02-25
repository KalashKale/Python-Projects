def square_generator(limit):
    num = 1
    while num <= limit:
        yield num ** 2   #yield instead of return
        num += 1

for squares in square_generator(5):
    print(squares)