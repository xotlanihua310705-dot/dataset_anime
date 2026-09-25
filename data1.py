import streamlit as st
import pandas as pd

names_link = "https://raw.githubusercontent.com/xotlanihua310705-dot/dataset_anime/refs/heads/main/Anime.csv"
names_data = pd.read_csv(names_link) 

st.title("streamlit and pandas")
st.dataframe(names_data)
