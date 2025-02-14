# Day 54
# Learning about backend with Flask
# Also learning about python decorators

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()

# Decorators exercise
# import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# def speed_calc_decorator(function):
#     def inner_function():
#         function()
#         final = time.time() - current_time
#         print(f"{function.__name__} run speed: {final}")
#     return inner_function

# @speed_calc_decorator
# def fast_function():
#   for i in range(1000000):
#     i * i
        
# @speed_calc_decorator
# def slow_function():
#   for i in range(10000000):
#     i * i

# fast_function()
# slow_function()
