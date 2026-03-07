# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Carte JOJ Temps Réel")

data = pd.DataFrame({
    "lat":[14.7167,14.7300,14.4500],
    "lon":[-17.4677,-17.2000,-17.0000],
    "site":[
        "Dakar Arena",
        "Diamniadio Stadium",
        "Saly Beach"
    ],
    "flux":[9000,12000,5000]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[lon, lat]",
    get_radius="flux",
    get_fill_color=[255,0,0,140],
    pickable=True
)

view = pdk.ViewState(
    latitude=14.7,
    longitude=-17.3,
    zoom=9
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text": "{site}\nFlux: {flux}"}
)

st.pydeck_chart(deck)