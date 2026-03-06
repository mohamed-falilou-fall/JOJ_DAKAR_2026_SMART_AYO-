import pandas as pd
import numpy as np

def generer_donnees_historiques():

    sites=[
    "Dakar Arena",
    "Stade Abdoulaye Wade",
    "CICAD",
    "Saly Beach",
    "Iba Mar Diop"
    ]

    data=[]

    for site in sites:

        for heure in range(8,23):

            data.append({
            "Site":site,
            "Heure":heure,
            "Spectateurs":np.random.randint(2000,15000)
            })

    return pd.DataFrame(data)


def prediction_affluence(df):

    pred=df.groupby("Site")["Spectateurs"].mean().reset_index()

    pred.rename(columns={"Spectateurs":"Affluence_prevue"},inplace=True)

    return pred