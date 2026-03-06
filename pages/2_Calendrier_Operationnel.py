# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

st.title("Calendrier Opérationnel JOJ Dakar 2026")

@st.cache_data
def load_data():
    return pd.read_excel("data/calendrier_sports.xlsx")

df = load_data()

st.dataframe(df,use_container_width=True)

sports = st.selectbox("Filtrer par sport",["Tous"]+sorted(df["Sport"].unique().tolist()))

if sports!="Tous":
    df=df[df["Sport"]==sports]

st.dataframe(df)

st.metric("Nombre total d'événements",len(df))