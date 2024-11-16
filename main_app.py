import streamlit as st
import app_01
import app_02
import app_03

st.sidebar.title("Pilihan Fitur")
page = st.sidebar.radio("Select a page:", ["Chat Assistant", "Deskripsi Image", "Bahasa Sunda Translator"])

# Load the selected page
if page == "Chat Assistant":
    app_01.main()
elif page == "Deskripsi Image":
    app_02.main()
elif page == "Bahasa Sunda Translator":
    app_03.main()
