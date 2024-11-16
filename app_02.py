import openai
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.set_page_config(page_title="Deskripsi Image", layout="wide")
    st.title("Deskripsi Image")
    st.write("Upload an image and provide some context to get a detailed AI-generated description.")

    # Check if the OpenAI API key is set
    if not openai.api_key:
        st.error("OpenAI API key not found. Please check the .env file or environment variables.")
        return

    # Upload image button
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Prompt for image context
    image_context = st.text_input(
        "Provide some context or keywords for the image (e.g., 'A bustling city street at night')",
        "Describe the image in detail based on what can be inferred from its elements."
    )

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Generate detailed description using OpenAI
        try:
            # Prepare prompt with image context
            description_prompt = (
                f"Based on the image context provided: '{image_context}', "
                "generate a detailed and descriptive explanation of over 500 words about this scene, "
                "including any elements or emotions that can be inferred."
            )

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an advanced AI model trained to infer details from images based on context."},
                    {"role": "user", "content": description_prompt}
                ],
                temperature=0.7,
                max_tokens=2048  # Enables a longer response to meet 500+ words
            )

            # Display the generated description
            detailed_description = response['choices'][0]['message']['content']
            st.subheader("Detailed AI-Generated Description")
            st.write(detailed_description)

        except Exception as e:
            st.error(f"Error: {e}")






