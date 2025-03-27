import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    pass

def divide(num1, num2):
    pass

def power(num1, num2):
    return num1 ** num2

def sqrt(num1):
    if num1 < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(num1)

def modulo(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot modulo by zero.")
    return num1 % num2

def average(arr_num):
    pass

def maximum(arr_num):
    pass

def minimum(arr_num):
    pass
