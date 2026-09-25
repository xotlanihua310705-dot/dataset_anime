import streamlit as st
import pandas as pd

myname = st.text_input("name :")
if st.button("search") :
 st.write(f"search name : {myname}")
