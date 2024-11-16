import os
import openai
import pytesseract
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
from utils import get_image_description  # Use this for detailed descriptions

# Ensure set_page_config is first
st.set_page_config(page_title="Image Description & OCR", layout="wide")

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.title("Image Description and OCR with GPT-4")
    st.write("Upload an image to get a detailed description and read any text within the image.")

    # Check if the API key is set
    if not openai.api_key:
        st.error("OpenAI API key not found. Please check the .env file or environment variables.")
        return

    # Textbox for entering a prompt for image description
    prompt = st.text_input("Enter a prompt for the image description", "Describe this image in detail.")

    # Upload image button
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Perform OCR to extract text from the image
        image = Image.open(uploaded_file)
        extracted_text = pytesseract.image_to_string(image)
        if extracted_text:
            st.subheader("Extracted Text from Image")
            st.write(extracted_text)
        else:
            st.write("No readable text found in the image.")

        # Generate a detailed description using OpenAI
        try:
            # Initial prompt for image description
            description_prompt = f"{prompt} Here is the text extracted from the image if relevant: '{extracted_text}'. Provide a detailed description in over 500 words."

            response = openai.ChatCompletion.create(
                model="gpt-4",  # Use gpt-4 or any available model
                messages=[
                    {"role": "system", "content": "You are an advanced image description model and expert in detailed narratives."},
                    {"role": "user", "content": description_prompt}
                ],
                temperature=0.7,
                max_tokens=2048  # Allows for a longer response
            )

            # Display the detailed description
            detailed_description = response['choices'][0]['message']['content']
            st.subheader("Detailed Image Description")
            st.write(detailed_description)

        except Exception as e:
            st.error(f"Error: {e}")




