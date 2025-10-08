from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, BaseMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

class ChatState(TypedDict):
    """
    Represents the state of the chat. It's a dictionary that holds the
    conversation history.

    Attributes:
        messages (list[BaseMessage]): A list of messages that make up the
                                      conversation, managed by `add_messages`.
    """
    messages: Annotated[list[BaseMessage], add_messages]

class MainChatBot():
    """
    A chatbot class that uses LangGraph and the Groq API to create a
    stateful conversational agent.

    This class encapsulates the logic for creating a graph-based workflow,
    managing conversation state in memory, and interacting with a large
    language model.

    Attributes:
        model (ChatGroq): An instance of the Groq chat model.
        main_graph (StateGraph): The LangGraph StateGraph that defines the
                                 chatbot's logic.
        checkpoint (MemorySaver): An in-memory checkpointer to save and
                                  load conversation states.
        workflow (CompiledGraph): The compiled, runnable LangGraph application.
    """
    def __init__(self):
        """
        Initializes the MainChatBot instance.

        This constructor sets up the core components:
        1. The ChatGroq model to be used for generation.
        2. The StateGraph with the defined `ChatState`.
        3. The MemorySaver for in-memory (RAM) conversation history.
        """
        self.model = ChatGroq(model="openai/gpt-oss-20b")
        self.main_graph = StateGraph(ChatState)
        self.checkpoint = MemorySaver()
        self.workflow = None # Will be initialized by initialize_workflow

    def chat_node(self, state: ChatState):
        """
        The primary node for the chat workflow that invokes the LLM.

        This function is called by the graph execution engine. It takes the
        current conversation state, passes the messages to the LLM, and
        returns the model's response.

        Args:
            state (ChatState): The current state of the graph, containing
                               the list of messages.

        Returns:
            dict: A dictionary with a "messages" key containing a list with
                  the new AIMessage from the model.
        """
        messages = state['messages']
        response = self.model.invoke(messages)
        return {"messages": [response]}

    def initialize_workflow(self):
        """
        Builds and compiles the LangGraph workflow.

        This method defines the structure of the conversation graph:
        1. Adds the `chat_node` as the main processing step.
        2. Sets the entry point (`START`) to direct to the `chat_node`.
        3. Sets the `chat_node` as the final step before the `END`.
        4. Compiles the graph with the in-memory checkpointer, making it
           a runnable application.
        """
        self.main_graph.add_node('chat_node', self.chat_node)
        self.main_graph.add_edge(START, 'chat_node')
        self.main_graph.add_edge('chat_node', END)
        self.workflow = self.main_graph.compile(checkpointer=self.checkpoint)
        
        
        
# # --- Main execution ---
# model = MainChatBot()
# model.initialize_workflow()

# # The config dictionary provides a unique ID for the conversation thread
# config = {"configurable": {"thread_id": "user-123"}}

# # The input message must be a list of BaseMessage objects (e.g., HumanMessage)
# initial_input = {"messages": [HumanMessage(content='Hello, how are you? Tell me about Taj Mahal')]}

# # Invoke the workflow with the input and the config
# for message_chunk, metadata in model.workflow.stream(initial_input, config=config, stream_mode='messages'):
#     if message_chunk.content:
#         print(message_chunk.content, end=" ", flush=True)

# print(type(response))
# print(response['messages'][-1].content)