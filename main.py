import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()
kode_api = os.getenv("API_KEY")

st.title("HELLO WORLD!")

st.write("Helo nama saya rizki")
st.write(kode_api)