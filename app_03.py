import os
import openai
import streamlit as st
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your model ID
MODEL_ID = "ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"

def main():
    st.set_page_config(page_title="Lestari Bahasa Translator", layout="wide")
    st.title("LESTARI BAHASA - Translator")

    user_input = st.text_input("Type your message to translate to Bahasa Sunda:")

    # Translation function with specific tone
    def translate_to_bahasa_sunda(tone):
        if user_input:
            translation_request = f"Translate this message to '{tone}' Bahasa Sunda: {user_input}"

            try:
                response = openai.ChatCompletion.create(
                    model=MODEL_ID,
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah ahli bahasa sunda dan dapat melakukan translasi berbagai bahasa dunia ke dalam bahasa Sunda. Kamu juga ahli dalam melakukan translasi bahasa sunda alus dan bahasa sunda kasar. Kamu dapat membedakan bahasa Sunda alus dan yang kasar."
                        },
                        {
                            "role": "user",
                            "content": translation_request
                        }
                    ],
                    temperature=1,
                    max_tokens=2048,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                assistant_response = response["choices"][0]["message"]["content"]
                if tone == "Sunda Alus":
                    st.session_state.sunda_alus_response = assistant_response
                    st.write(f"**Lestari Bahasa (Sunda Alus)**: {assistant_response}")
                else:
                    st.session_state.sunda_kasar_response = assistant_response
                    st.write(f"**Lestari Bahasa (Sunda Kasar)**: {assistant_response}")

            except Exception as e:
                st.error(f"Error: {e}")

    if st.button("Sunda Alus"):
        translate_to_bahasa_sunda("Sunda Alus")
        time.sleep(1)

    if st.button("Sunda Kasar"):
        translate_to_bahasa_sunda("Sunda Kasar")
        time.sleep(1)
