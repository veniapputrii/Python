import pandas as pd
import matplotlib.pyplot as plt

#Teil 1 : laden di CSV-Datei

df_geladen = pd.read_csv('Dataset/mitarbeiter_daten.csv')
print("1. Daten erfolgreich aus der CSV-Datei geladen!")
print(df_geladen.head())

#Teil 2 : Daten sortieren

df_sortiert = df_geladen.sort_values(by='Gehalt', ascending=False)
print("\n2. Hier ist undsere Tabelle, sortiert nach Gehalt Top-Verdiener oben :")
print(df_sortiert.head(3))

#Teil 3 : Das Diagram
#Wer verdient im Durchschnitt am besten?
#Wir gruppieren nach Abteilung, berechnen den Durchschnitt (.mean()) für das Gehalt
gehalt_pro_abteilung = df_geladen.groupby('Abteilung')['Gehalt'].mean()
print("\n3. Durchschnittgehalt pro Abteilung :")
print(gehalt_pro_abteilung)

#Jetzt zeichnen wir das Ergebnis als Balkendiagramm(Bar chart)
gehalt_pro_abteilung.plot(kind="bar", color = "darkblue", title="Durchschnittsgehalt nach Abteilung")
plt.ylabel('Gehalt in €')
plt.xlabel('Abteilung')
plt.tight_layout()

#Diagram anzeigen
plt.show()
