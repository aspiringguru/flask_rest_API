import functools

def decorator_arguments(number):
    def my_decorator(f):
        @functools.wraps(f)
        def function_that_runs_f(*args, **kwargs):
            print("Hello!")
            if number == 56:
                print("Not running!")
            else:
                f(*args, **kwargs)
            print("After")
        return function_that_runs_f
    return my_decorator

@decorator_arguments(56)
def my_function():
    print("Hello!")
    

my_function()
