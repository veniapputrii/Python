#assert statement is used for debugging purposes. The primary use of 'assert' is to catch and handle errors 
#during development, ensuring that certain conditions hold true at specific points in the code

#using an assertion message
x = -1
assert x > 0, "x must be positive"

#Assertions in funcitons
def divide(a,b):
    assert b != 0, "b can't be zero"
    return a/b
result = divide(10,2)
print(result)

result = divide(10,0)

#more info
#!= is not equal