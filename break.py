#a control flow statement used to come out a loop

#🐣 example

number = 0 
while number < 10 :
    print("Current number is:" , number)
    number += 1
    
    if number == 5:
        print("Number is 5, breaking the loop")
        
        break
    print ("loop has ended")
