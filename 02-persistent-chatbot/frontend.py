import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage,AIMessage

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

    # stream langgraph chatbot
    full_response=""

    with st.chat_message('assistant'):
        message_placeholder=st.empty()
        for chunk in chatbot.stream({
            'messages':[HumanMessage(content=user_input)]
        },
        config=CONFIG,
        stream_mode='messages'
        ):

            # separate message and metadata
            message,metadata=chunk

            # process only AI message chunk
            if isinstance(message,AIMessage):
                token=message.content
                if token:

                    # accumulate streamed token
                    full_response+=token
                    # display progressively
                    message_placeholder.markdown(full_response + "▌")
        
        # display final response without cursor
        message_placeholder.markdown(full_response)

    # save both messages in session state
    st.session_state['message_history'].append({'role':'user','content':user_input})

    st.session_state['message_history'].append({'role':'assistant','content':full_response})
