import streamlit as st
import pandas as pd

st.title("Incidents Terrain")

incidents=pd.DataFrame({
"Site":["Dakar Arena","Saly Beach","Expo Center"],
"Type":["Logistique","Sécurité","Technique"],
"Niveau":["Faible","Moyen","Critique"]
})

st.dataframe(incidents)

if st.button("Envoyer alerte Command Center"):
    st.error("Alerte envoyée au Smart Command Center")