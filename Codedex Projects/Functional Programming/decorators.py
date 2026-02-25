#Defining the decorator function
def decorator_func(func):
    def wrapper():
        print('This text is from the wrapper function')
        func()
        print("The function is decorated")

    return wrapper

#Applying decorator to say_hello() function
@decorator_func
def say_hello():
    print("Hello")

say_hello()