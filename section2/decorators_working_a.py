import functools  # function tools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("Hello!")
        func()
        print("After!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm in the function.")

#my_function()
def decorator_w_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print ("in the decorator")
            if number == 56:
                print ("not running the function")
            else:
                func(*args, **kwargs)
            print("after the decorator")
        return function_that_runs_func
    return my_decorator


@decorator_w_arguments(57)
def my_function_too(x, y):
    print(x + y)

my_function_too(1, 5)
