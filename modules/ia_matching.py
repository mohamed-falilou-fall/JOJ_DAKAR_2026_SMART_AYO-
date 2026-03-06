import pandas as pd

def score_matching(volontaire, mission):

    score=0

    if volontaire["Competence"]==mission["Competence_requise"]:
        score+=5

    if mission["Langue"] in volontaire["Langues"]:
        score+=3

    if volontaire["Experience"]>=mission["Experience_min"]:
        score+=2

    return score


def matching_volontaires(volontaires_df,missions_df):

    results=[]

    for _,vol in volontaires_df.iterrows():

        best_score=-1
        best_mission=None

        for _,mis in missions_df.iterrows():

            s=score_matching(vol,mis)

            if s>best_score:
                best_score=s
                best_mission=mis["Mission"]

        results.append({
        "Volontaire":vol["Nom"],
        "Mission_proposee":best_mission,
        "Score_matching":best_score
        })

    return pd.DataFrame(results)