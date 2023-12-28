# Import the Streamlit library
import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
# Define the main function for the Streamlit app

assistant_id = os.getenv("ASSISTANT_ID")
client = openai

# Initialize session state variables for file IDs and chat control
if "file_id_list" not in st.session_state:
    st.session_state.file_id_list = []

if "start_chat" not in st.session_state:
    st.session_state.start_chat = False

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# Set up the Streamlit page with a title and icon
st.set_page_config(page_title="DAVID'S EXAM ASSISTANCE", page_icon=":book:", layout="wide")
st.header(":book: DAVID'S EXAM ASSISTANCE")

#Get the OPENAI API Key
openai_api_key_env = os.getenv('OPENAI_API_KEY')
openai_api_key = st.sidebar.text_input(
    'OpenAI API Key', placeholder='sk-', value=openai_api_key_env)
url = "https://platform.openai.com/account/api-keys"
st.sidebar.markdown("Get an Open AI Access Key [here](%s). " % url)
if openai_api_key:
    openai.api_key = openai_api_key


# Add a slider to choose the difficulty level
difficulty = st.sidebar.slider('Choose the difficulty level', 1, 5, 3)

user_input = st.sidebar.text_input("Ask a question:")
if st.sidebar.button('Submit'):
    # Use the difficulty level in the API call
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        temperature=0.5,
        max_tokens=1000
    )
    # Display the response in a table
    st.write(response.choices[0].text)
