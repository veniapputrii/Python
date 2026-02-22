#control flow statement used to continue to the next iteration of a loop. 
#the continue statement doesn't exit the loop

#example
age = [12, 14, 15, 16, 18]
for number in age :
#print ("not eligible")
if age >= 18:
    continue
print("You're eligible to vote.")
break