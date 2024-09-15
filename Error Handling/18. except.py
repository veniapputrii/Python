#it tells to do when an exception occurs

a = 0
b = 10

try:
    div  = b/a
except ZeroDivisionError:
    print("Divisor can't be zero")