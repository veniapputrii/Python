# used in conjunction with a 'try-exception"
#conjunction is a word that is used to connect words, phrases, and clauses.
#in English like and, or, but, because, etc.

a = 5
b = 3

try:
    div = a/b
except ZeroDivisionError: #ZeroDivisionError is always occur if you are using 'try-except' and mostly used after except
    print("Divisior")
finally:
    print("Error")
    
#another exapmle
try:
    result = 10/2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always be printed, wheter an exception occurred or not")