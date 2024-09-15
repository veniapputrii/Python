#lambda is an anonymous function. It can take any number of arguments but only have a single expression.

#sample
numbers = [3,4,5]
sd = map(lambda x: x ** 3, numbers) #map is function
print(list(sd))

#benefit of use lambda
#1. Single-Line Functions : 'lamda'
#funtions allow you to define small functions in single line, shich can be more concise and readable for simple operations

#2. Inline Use
#used when you need a small function for a short period of time, especially as an argument to higher-order functions
#like 'map()', 'filter()', and 'sorted'

#examples comparing the use of 'lamda' with traditional 'def'
#using 'def'
def add(x,y):
    return x * y

result = add (3,5)
print(result)

#using lamba
add = lambda x,y : x + y
result = add (3,5)
print(result)