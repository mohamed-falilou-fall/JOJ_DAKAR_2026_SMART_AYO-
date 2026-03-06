# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

st.title("Gestion des Volontaires")

@st.cache_data
def load_volontaires():
    return pd.read_excel("data/volontaires.xlsx")

df = load_volontaires()

st.dataframe(df)

st.metric("Nombre total de volontaires",len(df))

genre=df["Genre"].value_counts()

st.bar_chart(genre)