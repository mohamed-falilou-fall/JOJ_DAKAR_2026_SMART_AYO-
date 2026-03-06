# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import plotly.express as px

BACKGROUND = "https://actu.rts.sn/wp-content/uploads/2025/10/IMG_4187.jpeg"

st.markdown(
f"""
<style>
.stApp {{
background-image: url("{BACKGROUND}");
background-size: cover;
}}
</style>
""",
unsafe_allow_html=True
)

st.title("Dashboard Stratégique JOJ Dakar 2026")

data = {
"Indicateur":[
"Taux présence volontaires",
"Couverture disciplines",
"Densité spectateurs",
"Incidents critiques",
"Satisfaction athlètes"
],
"Valeur":[92,88,76,3,91]
}

df = pd.DataFrame(data)

fig = px.bar(
df,
x="Indicateur",
y="Valeur",
color="Valeur",
title="Indicateurs stratégiques"
)

st.plotly_chart(fig,use_container_width=True)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Volontaires actifs","8 200","+3%")
c2.metric("Disciplines","25")
c3.metric("Sites sportifs","18")
c4.metric("Directions COJOJ","19")