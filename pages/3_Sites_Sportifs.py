# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analyse des Sites Sportifs")

df = pd.read_excel("data/calendrier_sports.xlsx")

sites = df.groupby("Site").size().reset_index(name="Nb_Epreuves")

fig = px.bar(
sites,
x="Site",
y="Nb_Epreuves",
color="Nb_Epreuves",
title="Répartition des épreuves par site"
)

st.plotly_chart(fig,use_container_width=True)