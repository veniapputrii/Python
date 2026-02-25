#25. Feb. 2026
#Account information for 10,000 customers at a European bank, including details on their credit score, 
# balance, products, and whether they have churned.
import pandas as pd
df = pd.read_csv('Dataset/Bank_Churn.csv')

print(df.head())

import csv
from tabulate import tabulate # Muss mit 'pip install tabulate' installiert werden

with open('Dataset/Bank_Churn.csv') as f:
    contents = list(csv.reader(f))
    # Zeigt die ersten 10 Zeilen schön formatiert an
    print(tabulate(contents[:10], headers="firstrow", tablefmt="grid"))

#Questions :
#What attributes are more common among churners than non-churners? 

# Can churn be predicted using the variables in the data?

#What do the overall demographics of the bank's customers look like?

#Is there a difference between German, French, and Spanish customers in terms of account behavior?

#What types of segments exist within the bank's customers?