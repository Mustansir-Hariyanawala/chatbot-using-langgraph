from chatbot import MainChatBot, ChatState
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st

if 'history' not in st.session_state:
    st.session_state['history'] = []

#st.session_state -> dict
#loading conversation
for message in st.session_state['history']:     
    with st.chat_message(message['role']):
        st.text(message['content'])
        
MODEL = MainChatBot()
MODEL.initialize_workflow()
CONFIG = {"configurable": {'thread_id': 'thread-1'}}

user_input = st.chat_input('Type here')


if user_input:
    
    #first add message to message_history
    st.session_state['history'].append({'role': 'user', 'content': user_input})
    
    #display user_input in chat
    with st.chat_message('user'):
        st.text(user_input)
    
    with st.chat_message('assistant'):
        response_message = st.write_stream(
            message_chunk.content for message_chunk, metadat in MODEL.workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    
    #Assistant side    
    
    st.session_state['history'].append({'role': 'assistant', 'content': response_message})
    