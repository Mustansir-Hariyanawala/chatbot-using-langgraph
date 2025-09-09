import streamlit as st
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful chatbot.")
    ]

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

class ChatBot:
    def __init__(self, model_name: str = "openai/gpt-oss-20b"):
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY not found in environment variables. Please add it to your .env file.")
            
        self.model = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=model_name
        )
        self.workflow = self._create_workflow()

    def _chat_node(self, state: ChatState):
        messages = state['messages']
        response = self.model.invoke(messages)
        return {"messages": [AIMessage(content=response.content)]}

    def _create_workflow(self):
        workflow = StateGraph(ChatState)
        workflow.add_node("chat", self._chat_node)
        workflow.set_entry_point("chat")
        workflow.add_edge("chat", END)
        return workflow.compile()

    def chat(self, message: str, history: List[BaseMessage] = None) -> str:
        if history is None:
            history = []
        
        initial_state: ChatState = {
            "messages": history + [HumanMessage(content=message)]
        }
        
        final_state = self.workflow.invoke(initial_state)
        return final_state['messages'][-1].content

def main():
    st.title("🤖 LangGraph Chatbot")
    st.write("Chat with an AI powered by LangGraph and Groq!")

    # Initialize the chatbot
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()
        
    # Add a clear chat button
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful chatbot.")
        ]
        st.rerun()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
            st.write(message.content)

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append(HumanMessage(content=prompt))
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.chat(
                    prompt,
                    st.session_state.messages[:-1]  # Pass previous messages as history
                )
                st.write(response)
                st.session_state.messages.append(AIMessage(content=response))

if __name__ == "__main__":
    main()
