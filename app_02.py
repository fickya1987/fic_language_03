import os
import streamlit as st
from openai import OpenAI
import base64
from utils import get_image_description

def main():
    st.title("Image Description using GPT-4o and GPT-4o Mini")
    st.write("Upload an image and get a description using GPT-4o or GPT-4o Mini.")

    api_key = st.text_input("Enter your OpenAI API key", type="password")
    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY", "")

    if api_key:
        client = OpenAI(api_key=api_key)
        model_choice = st.selectbox("Select the model", ["gpt-4o", "ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr", "gpt-4o-mini"])
        prompt = st.text_input("Enter the prompt for image description", "What’s in this image?")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            try:
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
                st.write("Classifying...")
                description = get_image_description(client, uploaded_file, prompt, model_choice)
                st.write(description)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please provide a valid OpenAI API key.")
