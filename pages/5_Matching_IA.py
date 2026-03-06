# -*- coding: utf-8 -*-

"""
SMART-AYO
Matching IA Volontaires ↔ Missions
JOJ Dakar 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Matching IA Volontaires ↔ Missions")

# =========================================================
# 1. CHARGEMENT DES DONNEES
# =========================================================

@st.cache_data
def load_volontaires():

    df = pd.read_excel("data/volontaires.xlsx")

    # normalisation des noms de colonnes
    df.columns = df.columns.str.strip().str.lower()

    # renommage automatique si nécessaire
    mapping = {
        "nom": "nom",
        "prenom": "prenom",
        "genre": "genre",
        "age": "age",
        "competence": "competence",
        "competences": "competence",
        "langue": "langues",
        "langues": "langues",
        "experience": "experience",
        "disponibilite": "disponibilite",
        "site": "site"
    }

    df = df.rename(columns=mapping)

    return df


volontaires = load_volontaires()

# =========================================================
# 2. MISSIONS JOJ
# =========================================================

missions = pd.DataFrame({

    "mission":[
        "Accueil Athlétisme",
        "Logistique Boxe",
        "Médias Breaking",
        "Transport Athlètes",
        "Sécurité Village Olympique"
    ],

    "competence_requise":[
        "Accueil",
        "Logistique",
        "Médias",
        "Transport",
        "Sécurité"
    ],

    "langue":[
        "Français",
        "Français",
        "Anglais",
        "Français",
        "Français"
    ],

    "experience_min":[
        1,
        2,
        1,
        1,
        2
    ],

    "site":[
        "Stade Abdoulaye Wade",
        "Dakar Arena",
        "CICAD",
        "Village Olympique",
        "Village Olympique"
    ]
})

# =========================================================
# 3. ALGORITHME IA DE MATCHING
# =========================================================

def score_matching(vol, mission):

    score = 0

    # compétences
    if str(vol.get("competence","")).lower() == mission["competence_requise"].lower():
        score += 40

    # langues
    langues = str(vol.get("langues","")).lower()

    if mission["langue"].lower() in langues:
        score += 25

    # expérience
    exp = vol.get("experience",0)

    if exp >= mission["experience_min"]:
        score += 20
    else:
        score += exp * 5

    # disponibilité
    dispo = str(vol.get("disponibilite","oui")).lower()

    if dispo == "oui":
        score += 10

    # proximité site
    if str(vol.get("site","")).lower() == mission["site"].lower():
        score += 5

    return score


# =========================================================
# 4. MATCHING INTELLIGENT
# =========================================================

def matching_ia(volontaires, missions):

    resultats = []

    for _, vol in volontaires.iterrows():

        meilleur_score = -1
        meilleure_mission = None
        meilleur_site = None

        for _, mis in missions.iterrows():

            score = score_matching(vol, mis)

            if score > meilleur_score:

                meilleur_score = score
                meilleure_mission = mis["mission"]
                meilleur_site = mis["site"]

        resultats.append({

            "Nom": vol.get("nom",""),
            "Prenom": vol.get("prenom",""),
            "Mission attribuée": meilleure_mission,
            "Site": meilleur_site,
            "Score IA": meilleur_score
        })

    return pd.DataFrame(resultats)


matching = matching_ia(volontaires, missions)

# =========================================================
# 5. RESULTATS
# =========================================================

st.subheader("Résultats du Matching IA")

st.dataframe(
    matching.sort_values("Score IA", ascending=False),
    use_container_width=True
)

st.metric("Nombre de volontaires matchés", len(matching))

# =========================================================
# 6. VISUALISATIONS
# =========================================================

st.subheader("Répartition des volontaires par mission")

fig = px.histogram(
    matching,
    x="Mission attribuée",
    color="Mission attribuée",
    title="Distribution des affectations"
)

st.plotly_chart(fig, use_container_width=True)


# =========================================================
# 7. ANALYSE DU SCORE IA
# =========================================================

st.subheader("Distribution des scores IA")

fig2 = px.histogram(
    matching,
    x="Score IA",
    nbins=20,
    title="Qualité du matching"
)

st.plotly_chart(fig2, use_container_width=True)


# =========================================================
# 8. QUALITE DU MATCHING
# =========================================================

score_moyen = round(matching["Score IA"].mean(),1)

st.metric(
    "Score moyen du Matching IA",
    score_moyen
)

if score_moyen > 70:
    st.success("Matching IA très performant")
elif score_moyen > 50:
    st.warning("Matching IA correct")
else:
    st.error("Matching IA à améliorer")