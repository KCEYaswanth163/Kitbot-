from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyBHmCY_N19tXLGAwhRhOaSzlZlzyMEYSOI"))

## function to load Gemini Pro model and get responses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="chatbot AI")

# Custom CSS to set background color
st.markdown("""
<style>
body {
    background-color: #2c3e50; /* Dark blue background */
    color: white; /* White text color */
}
</style>
""", unsafe_allow_html=True)

st.header("Personal KitBot+")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Questions: ",key="input")
submit=st.button("Ask your Personal KitBot+")
history=st.button("Previous Chats")
if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Answer for your queries:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
    

if history:
    st.subheader("Your's Chat History :") 
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
