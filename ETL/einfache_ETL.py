import pandas as pd
#import matplotlib.pyplot as plt

#Teil 1 : laden di CSV-Datei

df_geladen = pd.read_csv('Dataset/mitarbeiter_daten.csv')
print("1. Daten erfolgreich aus der CSV-Datei geladen!")
print(df_geladen.head())

#Teil 2 : Daten soriteren
