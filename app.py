# -*- coding: utf-8 -*-
"""
SMART-AYO
Plateforme intelligente de gestion des volontaires
JOJ Dakar 2026
"""

import streamlit as st

st.set_page_config(
    page_title="SMART-AYO JOJ Dakar 2026",
    page_icon="",
    layout="wide"
)

# =========================================================
# DESIGN GLOBAL
# =========================================================

BACKGROUND = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Olympic_flag.svg/1280px-Olympic_flag.svg.png"

st.markdown(
    f"""
    <style>
    /* Fond principal */
    .stApp {{
        background-image: url("{BACKGROUND}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Sidebar avec effet métallique */
    .css-1d391kg {{
        background: linear-gradient(145deg, #8c8c8c, #6f6f6f); /* dégradé fer */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3); /* ombrage interne pour effet métallique */
        font-weight: bold; /* texte en gras */
        color: #ffffff; /* texte blanc pour contraste */
    }}

    /* Tous les éléments dans la sidebar */
    .css-1d391kg * {{
        color: #ffffff !important;
        font-weight: bold !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CONTENU PRINCIPAL
# =========================================================

st.title("SMART-AYO – Plateforme intelligente JOJ Dakar 2026")

st.markdown("""
Bienvenue dans la plateforme stratégique de pilotage des **Jeux Olympiques de la Jeunesse Dakar 2026**.

Utilisez le menu de gauche pour accéder aux différents modules :

- Dashboard stratégique
- Calendrier opérationnel
- Sites sportifs
- Gestion des volontaires
- Matching IA
- Flux spectateurs
- Transport Smart City
- Incidents terrain
- Command Center
- Impact durable
""")
