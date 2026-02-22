#In Python, the `in` keyword has two primary functions:

#1. Membership Test
#The `in` keyword is used to check if a value exists within a sequence (such as a list, tuple, string, set, or dictionary). 
# It returns `True` if the value is found in the sequence and `False` otherwise.
# Check if an element is in a list
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)  # Output: True
print('orange' in fruits) # Output: False

# Check if a character is in a string
word = 'hello'
print('h' in word)  # Output: True
print('z' in word)  # Output: False


#2. Iteration in Loops
#The `in` keyword is also used in `for` loops to iterate over the elements of a sequence.
# Iterate over a list
for fruit in ['apple', 'banana', 'cherry']:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Iterate over a string
for char in 'hello':
    print(char)
# Output:
# h
# e
# l
# l
# o


#In both cases, `in` helps to determine membership or iterate over elements within a sequence.