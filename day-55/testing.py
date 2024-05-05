 
 
# 
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         function(args[0],args[1],args[2])
#         print(f"You called {function.__name__}{args[0],args[1],args[2]}  ")
#         print(f"It returned: {args[0]*args[1]*args[2]}")
#     return wrapper

# inputs=[8.7, 9.9, 1.3]
#  
# @decorator
# def a_function(a, b, c): 
#     return a * b * c

# a_function(inputs[0], inputs[1], inputs[2])
random_value = 5

def decorator(function):
    global random_value
    def wrapper(*args, **kwargs):
        value= function(*args, **kwargs)  +random_value
        return value
    return wrapper

@decorator
def home(number): 
    return number


a = home(number=5)
print(a)