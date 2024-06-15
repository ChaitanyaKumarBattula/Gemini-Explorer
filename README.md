# Gemini-Explorer
Google Gemini is an AI platform that uses advanced machine learning and natural language processing (NLP) to replicate human conversations.

## Project Overview
Develop a chat interface using Streamlit that connects to Google's cutting-edge language model, Gemini.

## Requirements
- Python 3.11 or above
- Streamlit
- Google Cloud account
- Vertex AI
- 
## Workflow
### Step 1: Enable Google Cloud
- Visit the Google Cloud Platform and start with the free tier.
- Log in with your Google account, complete the billing setup, and create a new project.
- Enable all recommended APIs under Vertex AI.
  ![Gemini_img](https://github.com/ChaitanyaKumarBattula/Gemini-Explorer/blob/main/Gemini_img/RadicalAi-1.png)
  
### Step 2: Initialize Google Cloud
- Install the Google Cloud SDK from here.
- Initialize the SDK: ```gcloud init```
- Log in with your Google account and select or create a project.
- Optionally, set the default compute region and zone.
  ![Gemini_img](https://github.com/ChaitanyaKumarBattula/Gemini-Explorer/blob/main/Gemini_img/RadicalAi-2.png)
### Step 3: Set Up Google Gemini2
- Install Streamlit
### Step 4: Integrate with Streamlit
- Follow the implementation steps.
- Run the Streamlit application: ```streamlit run Gemini_explorer.py```
  ![Gemini_img](https://github.com/ChaitanyaKumarBattula/Gemini-Explorer/blob/main/Gemini_img/RadicalAi-4.png)
### Step 5: Add Initial System Messages
- Customize initial messages for user interaction.
  ![Gemini_img](https://github.com/ChaitanyaKumarBattula/Gemini-Explorer/blob/main/Gemini_img/RadicalAi-5.png)

## Installation
Install the required packages with:
 ```pip install google-cloud-aiplatform streamlit ```
 
## Features
- Custom greetings based on the user's name.
- Interactive chat interface powered by Google Gemini.
- Display of chat history.

## Acknowledgements
- I would like to thank Talha Sabri and Mikhail Ocampo for their support and guidance throughout this project. 
