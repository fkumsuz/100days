import time


"""def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        print("2 sn delay")
        function()
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
    
say_hello()"""

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇


def speed_calc_decorator(function): 
    def wrapper_function():
        start_time = time.time()
        function()
        
        end_time = time.time()
        difference = end_time-start_time
        print(f"{function.__name__} run speed: {difference}")
    return wrapper_function

 

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
fast_function()
slow_function()

inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function): 
    def wrapper_function(*args, **kwargs):  # Accept arbitrary arguments and keyword arguments
        print(f"You called {function.__name__}{args}")
        result = function(*args, **kwargs)  # Pass the arguments to the decorated function
        print(f"It returned: {result}") 
        return result  # Return the result of the decorated function
    return wrapper_function



# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c): 
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])