import streamlit as st
import pandas as pd

st.title("Impact Durable JOJ Dakar 2026")

data={
"Indicateur":[
"Déplacements évités",
"Energie optimisée",
"CO2 évité",
"Optimisation transports"
],
"Valeur":[30,25,40,35]
}

df=pd.DataFrame(data)

st.dataframe(df)

score=sum(df["Valeur"])

st.metric("Score Durable Global",score)