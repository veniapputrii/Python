#the while loop is used to repeatedly esecute a block of code as long as a given condition is true
#the condition is evaluated before each iteration, and if it evaluates to "True",
#the code within the loop is executed. If the condition evaluates to "False", the loop stops

#basic example
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    
#Using 'else' with 'while'
count = 0
while count < 10:
    print("Count is:", count)
    count += 1
else:
    print("Loop is done")
    
#✨ more ✨
#What += means?
#it adds the value on its right to the variable on its left and then assigns the result 
#back to the variable on the left.
#essentially, "a += b" is equivalent to "a = a + b"
