import os
import openai
import streamlit as st
from dotenv import load_dotenv
from utils import get_image_description

# Ensure set_page_config is first
st.set_page_config(page_title="Deskripsi Image", layout="wide")

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.title("Deskripsi Image dengan Lestari Bahasa")
    st.write("Upload an image")

    api_key = st.text_input("Enter your OpenAI API key", type="password")
    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY", "")

    if api_key:
        model_choice = st.selectbox("Select the model", ["ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"])
        prompt = st.text_input("Enter the prompt for image description", "What’s in this image?")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            try:
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
                st.write("Classifying...")
                description = get_image_description(openai, uploaded_file, prompt, model_choice)
                st.write(description)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please provide a valid OpenAI API key.")

