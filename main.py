from chatbot import MainChatBot, ChatState
from langchain_core.messages import HumanMessage, SystemMessage
import re


if __name__ == "__main__":
    initial_state: ChatState = {
        "messages": [SystemMessage(content="You are a helpful chatbot.")],
    }
    chatbot = MainChatBot()
    chatbot.initialise_workflow()
    thread_id = 1
    
    while(True):
        human_message = input("You: ")
        
        config = {'configurable': {'thread_id': thread_id}}
        final_state = chatbot.workflow.invoke({"messages": [HumanMessage(content=human_message)]}, config=config)
        print("AI:", final_state['messages'][-1].content)  
        
        if re.search('exit|bye', human_message.strip().lower()):
            break