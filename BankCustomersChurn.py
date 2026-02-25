#25. Feb. 2026
#Account information for 10,000 customers at a European bank, including details on their credit score, 
# balance, products, and whether they have churned.
import pandas as pd
df = pd.read_csv('Dataset/Bank_Churn.csv')

print(df.head())
#Questions :
#What attributes are more common among churners than non-churners? 

# Can churn be predicted using the variables in the data?

#What do the overall demographics of the bank's customers look like?

#Is there a difference between German, French, and Spanish customers in terms of account behavior?

#What types of segments exist within the bank's customers?