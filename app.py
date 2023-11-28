import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='GenAI Tool', layout='wide')

# Title of your app
st.title("GenAI Tool")

# Instructions
st.write("Enter your prompt in the text box below and hit enter to see the magic.")

# Text input box at the bottom
user_input = st.text_input("Prompt", key="prompt_input")

# You can now use the user_input variable to pass to your genAI tool
# For example:
# if user_input:
#    response = your_genai_function(user_input)
#    st.write(response)

# You can put this at the end if you want to display something once the user enters a prompt
if user_input:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here
