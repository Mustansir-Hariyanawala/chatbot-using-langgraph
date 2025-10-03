from chatbot import MainChatBot, ChatState
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st

# Set page configuration
st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖", layout="centered")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_model" not in st.session_state:
    st.session_state.chat_model = MainChatBot()
    st.session_state.chat_model.initialize_workflow()

if "thread_id" not in st.session_state:
    st.session_state.thread_id = 1

# Display title
st.title("🤖 LangGraph Chatbot")
st.write("Chat with an AI powered by LangGraph and Groq!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Chat input
if user_input := st.chat_input('Type your message here...'):
    # Add user message to chat history
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    
    # Display user message
    with st.chat_message('user'):
        st.markdown(user_input)
    
    # Get AI response
    config = {"configurable": {'thread_id': st.session_state.thread_id}}
    
    with st.chat_message('assistant'):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_model.workflow.invoke(
                input={"messages": [HumanMessage(content=user_input)]}, 
                config=config
            )
            ai_response = response['messages'][-1].content
            st.markdown(ai_response)
    
    # Add AI response to chat history
    st.session_state.messages.append({'role': 'assistant', 'content': ai_response})