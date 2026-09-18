import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {"configurable": {"thread_id": "thread_1"}}

st.title("My AI Chatbot")

# st.session_state->dict-> accumulate msg and does not erase it on 'enter'

# initialize session state
if 'message_history' not in st.session_state: 
    st.session_state['message_history']=[]

# display prev message
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

# chat input
user_input=st.chat_input('Type here')

if user_input :

    # display user msg
    with st.chat_message('user'):
        st.write(user_input)

    # invoke langgraph chatbot
    response=chatbot.invoke({"messages":[HumanMessage(content=user_input)]},config=CONFIG)

    # get ai response 
    ai_message=response['messages'][-1].content

    # display ai response
    with st.chat_message("assistant"):
        st.write(ai_message)

    # save both messages in session state
    st.session_state['message_history'].append({'role':'user','content':user_input})

    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
