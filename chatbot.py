from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Optional
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st
import os, re

class ChatState(TypedDict):
            messages: Annotated[list[BaseMessage], add_messages]
            # user_input: str
            # response: Optional[str]
            
class MainChatBot():
    load_dotenv()

    def __init__(self):
        self.model = ChatGroq(model="openai/gpt-oss-20b")
        self.main_graph = StateGraph(ChatState)
        self.checkpoint = MemorySaver()
        

        
    def chat_node(self, state: ChatState):
        messages = state['messages']    
        response = self.model.invoke(messages)
        return {"messages": [response]}
    
    def initialise_workflow(self):
        self.main_graph.add_node('chat_node', self.chat_node)
        self.main_graph.add_edge(START, 'chat_node')
        self.main_graph.add_edge('chat_node', END)
        self.workflow = self.main_graph.compile(checkpointer=self.checkpoint)




