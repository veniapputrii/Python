#I'm still not entirely sure with the expression part. 
#here I looked up another similar exercise for increasing my understanding

#Exercise:

#You need to write a discount program for a grocery store with the following conditions:

#If a customer spends more than 300,000, they will receive a 15% discount.
#A customer named Alya has spent 450,000.

#Hint:

#Remember, you're looking for the total amount to be paid 
#after the discount is applied, not just the discount amount.

# Don't change this code
alya = 450000

#fix it here
if alya > 300000:
    discount = 0.15 * alya
    price_total = alya - discount
else:
    price_total = alya
    
print(f"Alya has to pay : {price_total}")