from chatbot import MainChatBot, ChatState
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
import uuid

#Main chat bot object in which the workflow is created and initialized       
MODEL = MainChatBot()
MODEL.initialize_workflow()

#Configuring threads
CONFIG = {"configurable": {'thread_id': st.session_state['thread_id']}}
# ***************************Utility Functions***********************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id  
    add_thread(st.session_state['thread_id']) 
    st.session_state['history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
        
def load_conversation(thread_id, workflow: MainChatBot):
    return workflow.workflow.get_state(config = {'configurable' : {'thread_id' : thread_id}}).values['message']
# ************************************* Session Setup **************************
if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    
add_thread(st.session_state['thread_id'])
# ************************************** SideBar UI ****************************** 
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        load_conversation(thread_id=thread_id)
# ************************************** Main Chat Section *******************
#st.session_state -> dict
#loading conversation
for message in st.session_state['history']:     
    with st.chat_message(message['role']):
        st.text(message['content'])

#
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
    