import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Transport Smart City")

data={
"Infrastructure":["Autoroute A1","TER","Navettes JOJ","Aéroport AIBD"],
"Performance":[90,85,88,80]
}

df=pd.DataFrame(data)

fig=px.bar(df,x="Infrastructure",y="Performance",color="Performance")

st.plotly_chart(fig,use_container_width=True)