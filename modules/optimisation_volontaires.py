import pandas as pd

def taux_couverture(df):

    total_requis=df["Volontaires_requis"].sum()
    total_actuels=df["Volontaires_actuels"].sum()

    return round((total_actuels/total_requis)*100,2)