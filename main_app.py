import streamlit as st
import app_01
import app_02
import app_03

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Chat Assistant", "Image Description", "Bahasa Sunda Translator"])

# Load the selected page
if page == "Chat Assistant":
    app_01.main()
elif page == "Image Description":
    app_02.main()
elif page == "Bahasa Sunda Translator":
    app_03.main()
