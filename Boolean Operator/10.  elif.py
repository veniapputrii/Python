#A shorthand for "else if"
#it allows you to check multiple expressions for truth
#value and execute a block of coe as soon as one of the conditions is true

score = 85

if score >= 90:
    print("Excellent") #If score is 90 or above, it prints "Excellent".
elif score >= 80:
    print("Good") #If score is 80 or above but less than 90, it prints "Good".
elif score >= 70:
    print("Fair") #If score is 70 or above but less than 80, it prints "Fair".
else:
    print("Needs Improvement")
    
#In this example:




#If score is less than 70, it prints "Needs Improvement".

#So, the 'elif' statements allow for multiple conditions to be checked in squence
