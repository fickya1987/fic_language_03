import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Ensure set_page_config is first
st.set_page_config(page_title="Chat Assistant", layout="wide")

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your model ID
MODEL_ID = "ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"

def main():
    st.title("LESTARI BAHASA - Chat Assistant")
    
    # Initialize the message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful Worldwide Translator and Language Expert."}
        ]

    # Display the chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**User**: {message['content']}")
        else:
            st.write(f"**Assistant**: {message['content']}")

    # User input
    user_input = st.text_input("Type your message:")

    # Send button functionality
    if st.button("Send"):
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            try:
                response = openai.ChatCompletion.create(
                    model=MODEL_ID,
                    messages=st.session_state.messages,
                    temperature=1,
                    max_tokens=2048,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                assistant_response = response.choices[0].message['content'].strip()
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                st.write(f"**Assistant**: {assistant_response}")
            except Exception as e:
                st.error(f"Error: {e}")
