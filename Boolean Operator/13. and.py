#used as a locical operator to combine conditional statements. 
#It returns 'True' if both operands (conditions) are true, and 'False' otherwise.

#simple example
a = 5
b = 10
c = 20

mm = a > c
bb = c > b
result = mm and bb
print (result)


#basic example
x = 5
y = 10
if x > 2 and y > 15:
    print("Both conditions are True")
else:
    
    print("at least one condition is False")
    
#multiple Conditions
a = True
b = False
c = True

if a and c and c :
    print("All conditions are True")
else:
    print("at least one condition is False")
    
#Combining with Other Logical Operators
x = 5
y = 10
z = 15

if (x < y and y < z) or z == 15:
    print("Either both conditions are true, or z equals 15")
else:
    print("Both conditions are false and z does not equal 15")
 
#✨ more ✨
# == (equal) is part of Comparison Operations ~ these are higher than that of the Boolean operations (and, or, not)
# These are the Boolean operations, ordered by ascending priority :
# Operation :
# x or y => if x is ture, then x, else y
# x and y => if x is false, then x, else y
# not x => if x is false, then True, else False

#the summarizes the comparison opeartions: 
# < : strictly less than
# <= : less than or equal
# > : strictly greater than
# >= : greater than or equal
# == : equal
# != : not equal
# is : object identity
# is not : negated object identity

# the == operator is always defined but for some object types(for example, class object) is equivalent to "is"
