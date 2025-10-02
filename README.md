# 🤖 LangGraph Chatbot with Streamlit UI

A modern, interactive chatbot application built with LangGraph, Groq API, and Streamlit. This project features a beautiful Gemini-inspired interface with advanced conversation management using state graphs.

## ✨ Features

- **Modern UI**: Gemini-inspired interface with gradient backgrounds and smooth animations
- **State Management**: Advanced conversation flow using LangGraph's StateGraph
- **Multiple Models**: Support for various Groq models including Mixtral
- **Real-time Chat**: Interactive chat interface with message history
- **Customizable Settings**: Temperature control, model selection, and output length adjustment
- **Memory Management**: Persistent conversation history with MemorySaver
- **Code Highlighting**: Syntax highlighting for code blocks in responses
- **Responsive Design**: Clean, modern interface that works on different screen sizes

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Groq API key (get one from [Groq Console](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mustansir-Hariyanawala/chatbot-using-langgraph.git
   cd chatbot-using-langgraph
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   ```

### Usage

#### Option 1: Streamlit Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```
Open your browser and navigate to `http://localhost:8501`

#### Option 2: Command Line Interface
```bash
python chatbot.py
```

## 📁 Project Structure

```
langgraph_chatbot/
├── chatbot.py              # Core chatbot implementation with LangGraph
├── streamlit_app.py        # Streamlit web interface
├── main.py                 # Alternative entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🛠️ Dependencies

### Core Libraries
- `streamlit>=1.32.0` - Web interface framework
- `langgraph>=0.0.15` - State graph management
- `langchain>=0.1.0` - LangChain core functionality
- `langchain-core>=0.1.0` - Core LangChain components
- `langchain-groq>=0.3.0` - Groq API integration
- `python-dotenv>=1.0.0` - Environment variable management

### Optional Extensions (for RAG and advanced features)
- `pinecone-client>=3.0.0` - Vector database
- `chromadb>=0.4.0` - Local vector store
- `unstructured>=0.10.0` - Document processing
- `pypdf>=3.9.0` - PDF processing
- `tiktoken>=0.5.0` - Token counting

## 🎯 Key Components

### ChatState
```python
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
```
Defines the conversation state structure with automatic message management.

### MainChatBot Class
- **Model Integration**: Uses Groq's advanced language models
- **State Management**: LangGraph StateGraph for conversation flow
- **Memory**: MemorySaver for persistent conversation history
- **Workflow**: Configurable conversation workflow

### Streamlit Interface
- **Responsive Design**: Modern, mobile-friendly interface
- **Real-time Chat**: Interactive chat with streaming responses
- **Settings Panel**: Model selection, temperature control, and more
- **Message History**: Persistent conversation within session

## 🎨 UI Features

- **Gradient Title**: Eye-catching header with modern styling
- **Chat Bubbles**: Distinct styling for user and assistant messages
- **Code Highlighting**: Syntax highlighting for code blocks
- **Loading Animations**: Smooth loading indicators
- **Responsive Layout**: Works on desktop and mobile devices

## 🔧 Configuration

### Model Settings
- **Model Selection**: Choose from available Groq models
- **Temperature**: Control creativity vs. focus (0.0 - 1.0)
- **Max Length**: Set maximum response length
- **Thread Management**: Unique conversation threads

### Environment Variables
```env
GROQ_API_KEY=your-api-key-here
LANGSMITH_API_KEY=optional-langsmith-key
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for state management
- [Groq](https://groq.com/) for fast LLM inference
- [Streamlit](https://streamlit.io/) for the web interface framework
- [LangChain](https://langchain.com/) for LLM orchestration

## 🐛 Known Issues

- Ensure your Groq API key is valid and has sufficient credits
- Some models may have different parameter requirements
- Large conversation histories may impact performance

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Mustansir-Hariyanawala/chatbot-using-langgraph/issues) page
2. Create a new issue with detailed information
3. Provide your Python version and error messages

---

**Built with ❤️ using LangGraph, Groq, and Streamlit**