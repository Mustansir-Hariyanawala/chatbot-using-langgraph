from chatbot import MainChatBot, ChatState
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
import re

message_history = []
chat_model = MainChatBot()
chat_model.initialize_workflow()
thread_id = 1

for message in message_history:
    with st.chat_message(message['role']):
        st.text(message['content'])
        

user_input = st.chat_input('Type here')

config = {"configurable" :{'thread_id': thread_id}}
thread_id += 1
if user_input:
    
    #first add the message to message history
    message_history.append({'role': 'human', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    response = chat_model.workflow.invoke(input={"messages": [HumanMessage(content=user_input)]}, config=config)
    message_history.append({'role': 'human', 'content': response['messages'][-1].content})
    with st.chat_message('ai'):
        st.text(response['messages'][-1].content)