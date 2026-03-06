import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart City Command Center")

data={
"Système":[
"Trafic A1",
"TER",
"Sécurité",
"Santé",
"Logistique",
"Presse CICAD"
],
"Statut":[85,90,92,88,80,87]
}

df=pd.DataFrame(data)

fig=px.bar(df,x="Système",y="Statut",color="Statut")

st.plotly_chart(fig,use_container_width=True)