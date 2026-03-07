# -*- coding: utf-8 -*-

"""
SMART-AYO
Logiciel de gestion opérationnelle
JOJ Dakar 2026
"""

import streamlit as st
from auth import login
from config import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
    page_icon=""
)

st.markdown("""
<style>

/* ===== IMAGE DE FOND ===== */

.stApp{
background-image:url("https://lequotidien.sn/wp-content/uploads/2025/05/JOJ-2026.jpg");
background-size:cover;
background-position:center;
background-attachment:fixed;
}


/* ===== SIDEBAR BLANCHE ===== */

[data-testid="stSidebar"]{
background-color:white;
color:black;
}


/* texte sidebar lisible */

[data-testid="stSidebar"] *{
color:black !important;
}


/* titres */

h1,h2,h3,h4{
color:white;
}


/* messages */

.stAlert{
background-color:rgba(255,255,255,0.85);
color:black;
border-radius:10px;
}


/* container principal légèrement transparent */

.main{
background-color:rgba(0,0,0,0.55);
padding:20px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

user = login()

if not user:
    st.stop()

st.title("SMART-AYO Command Center")

st.success(f"Utilisateur connecté : {user}")

st.info("Utilisez le menu de gauche pour naviguer dans les modules.")
