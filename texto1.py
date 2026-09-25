import streamlit as st
import pandas as pd

myname = st.text_input("Nombre")
if (myname):
   st.write(f"tu nombre es : {myname}")

