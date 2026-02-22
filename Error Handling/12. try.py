#used for exception handling.
#it allows you to test a blockof code for errors. If an error occurs, the code in the "except" block is executed.
#optionally, you can use "else" and "finally" blocks to handle code that should run if no errors occur, and code that should run no matter what.

#Basic :
try:
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    
#Handling multiple exceptions :
try:
    x = int("not a number")
except ValueError:
    print("ValueError occured")
except TypeError:
    print("TypeError occured")
    
#Else block

try:
    x = int("42")
except ValueError:
    print("ValueError occured")
else:
    print("No error occured, x is", x)
    
#finally block
try :
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always be executed")

#combining "else" and "finally" blocks 
try:
    x = int("42")
except ValueError:
    print("ValueError occurred")
else:
    print("No error occured, x is", x)
finally:
    print("this will always be executed")
    
#raising exeptions
try:
    raise ValueError("An error occured")
except ValueError as b:
    print(b)