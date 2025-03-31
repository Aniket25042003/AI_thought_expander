# AI Thought Expander & Chatbot

## 🌍 Overview
AI Thought Expander & Chatbot is an AI-powered web application built using Gradio, which helps users explore diverse perspectives on any concept or idea. The application can expand a given concept in multiple ways, including scientific, philosophical, artistic, humorous, and real-world applications. Additionally, it features a chatbot interface to answer questions related to the concept or idea provided by the user.

## ⚙️ Features
- **Concept Expansion**: Provides multiple perspectives (scientific, philosophical, artistic, etc.) on any given concept.
- **AI Chatbot**: Allows users to interact with an AI assistant that answers questions related to the provided concept.
- **Interactive UI**: Easy-to-use interface with a text input area for the concept and a chatbot area for interactive communication.

## 🛠️ Technology Stack
- **Frontend**: Gradio (for building the user interface)
- **Backend**: Nebius AI Studio (for generating responses using LLaMA or other models)
- **Deployment**: Local/Cloud (via Gradio's launch functionality)

## 📝 Installation

### Prerequisites
- Python 3.7 or later
- Dependencies installed (listed in `requirements.txt`)

### Step-by-Step Setup

1. **Clone the repository**:
```bash
   git clone https://github.com/yourusername/ai-thought-expander-chatbot.git
   cd ai-thought-expander-chatbot
```
2. **Install dependencies**:
```bash
  pip install -r requirements.txt
```
3. **Create a ```.env``` file**:
- In the project root, create a ```.env``` file to store your API keys and other sensitive information:
```bash
  NEBIUS_API_KEY=your_nebius_api_key
```
4. **Run the application**:
```bash
  python3 app.py
```
The app will run locally at ```http://127.0.0.1:7860```.

## 🌱 Usage
- Concept Expansion: Enter a concept (e.g., "Artificial Intelligence in Art") into the input box, and click the Expand Thought button to explore multiple perspectives on the concept.
- Chatbot: After entering a concept, you can interact with the chatbot, asking it any questions related to that concept. The chatbot will respond accordingly.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for improvements or bug fixes.

## 📢 Acknowledgements
- Gradio: For building the web interface
- Nebius: For the integration with the Nebius AI Studio API for enhanced model capabilities
