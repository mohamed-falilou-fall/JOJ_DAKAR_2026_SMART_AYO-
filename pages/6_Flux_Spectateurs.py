# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import plotly.express as px

from modules.prediction_flux import generer_donnees_historiques
from modules.prediction_flux import prediction_affluence

st.title("Flux Spectateurs")

df=generer_donnees_historiques()

pred=prediction_affluence(df)

fig=px.bar(pred,x="Site",y="Affluence_prevue")

st.plotly_chart(fig,use_container_width=True)