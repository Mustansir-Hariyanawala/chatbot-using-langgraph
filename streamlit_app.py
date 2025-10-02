import streamlit as st
from typing import List
import time

# Configure Streamlit page
st.set_page_config(
    page_title="Gemini Clone",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Gemini-like styling with enhanced UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    
    /* Title styling */
    .title-container {
        background: linear-gradient(90deg, #4CAF50 0%, #2196F3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .title-text {
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .subtitle-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Chat message styling */
    .user-message {
        background-color: #e3f2fd;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-top-right-radius: 5px;
    }
    
    .assistant-message {
        background-color: white;
        padding: 1.2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e1e4e8;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-top-left-radius: 5px;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: white;
        padding: 1.5rem;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: white;
        border-radius: 25px;
        padding: 0.8rem 1.2rem;
        border: 2px solid #e1e4e8;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #2196F3;
        box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.2);
    }
    
    /* Code block styling */
    code {
        background-color: #f6f8fa;
        padding: 0.3em 0.6em;
        border-radius: 5px;
        font-family: 'Consolas', 'Monaco', monospace;
    }
    
    pre {
        background-color: #f6f8fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e1e4e8;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 25px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Slider styling */
    .stSlider > div > div {
        height: 3px;
    }
    
    .stSlider > div > div > div > div {
        background-color: #2196F3;
    }
    
    /* Chat container */
    .chat-container {
        background-color: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_model" not in st.session_state:
    st.session_state.current_model = "gemini-pro"

# Sidebar
with st.sidebar:
    st.title("🤖 Gemini Clone")
    
    # Model selection
    st.subheader("Model Settings")
    model = st.selectbox(
        "Choose a model",
        ["gemini-pro", "gemini-pro-vision"],
        index=0
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher values make the output more creative but less focused"
    )
    
    # Max output length
    max_length = st.number_input(
        "Maximum output length",
        min_value=1,
        max_value=2048,
        value=1024,
        help="Maximum number of tokens in the response"
    )
    
    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    # Divider
    st.divider()
    
    # About section
    st.markdown("""
    ### About
    This is a clone of Google's Gemini interface built with Streamlit.
    
    Features:
    - Chat interface
    - Code highlighting
    - Markdown support
    - Model settings
    - Temperature control
    """)

# Main chat container with enhanced title
st.markdown("""
<div class="title-container">
    <h1 class="title-text">🤖 Gemini Clone</h1>
    <p class="subtitle-text">Your AI Assistant powered by Advanced Language Models</p>
</div>
""", unsafe_allow_html=True)

# Display chat messages in a container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for idx, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message["content"])
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Message Gemini..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Simulate AI response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate stream of response with a loading animation
        with st.spinner("Thinking..."):
            time.sleep(1)  # Simulate API call
            response = f"""This is a placeholder response to: "{prompt}"
            
Here's a code example:
```python
def hello_world():
    print("Hello from Gemini!")
```

And here's a list:
1. First item
2. Second item
3. Third item

> This is a blockquote for emphasis

You can replace this with actual AI responses later."""
            
            # Simulate streaming response
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("---")
st.markdown("*This is a demo interface. Connect your own model for actual AI responses.*")
