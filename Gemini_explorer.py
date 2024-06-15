#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install google-cloud-aiplatform
# !pip install streamlit
# from vertexai import preview


# In[2]:


# Importing the necessary libraries

import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession


# In[3]:


project = "vibrant-mind-426501-d1"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()


# In[4]:


# Helper function to display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })
    st.session_state.messages.append({
        "role": "model",
        "content": output
    })
    
st.title("Gemini Explorer")

# Initializing the Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# To display and load the Chat History
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message['role'],
        parts = [Part.from_text(message['content'])]
    )
    
    if index!= 0 :
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)

# Capture user information
user_name = st.text_input("Please enter your name")

# Implement Personalized Greetings
if user_name:
    personalized_greeting = f"Hello {user_name}! I'm ReX, an assistant powered by Google Gemini. Let's chat with emojis! 😊"
    llm_function(chat, user_name)
    st.session_state.messages = []

# # For initial message startup
# if len(st.session_state.messages) == 0:
#     initial_prompt = "Ahoy matey! I be ReX, an assistant powered by Google Gemini. Let's set sail on this interactive journey with emojis! Arrr! ⚓🏴‍☠️,You use emojis to be interactive"
#     llm_function(chat, initial_prompt)
#     st.session_state.messages = []
    
# To capture the user's input
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(chat, query)

