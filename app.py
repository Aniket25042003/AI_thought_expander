import gradio as gr
import openai
import os
from dotenv import load_dotenv  # Import the dotenv module

load_dotenv()
# Nebius API Key and Client Setup
nebius_api_key = os.getenv("NEBIUS_API_KEY")  # Get API key from environment variables
# Nebius AI Studio API details
client = openai.OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",  # Nebius API base URL
    api_key=nebius_api_key,  # Your Nebius API key
)

# Global variable to hold the initial concept
initial_concept = None

# Function to generate responses based on the concept
def generate_expansion(concept):
    global initial_concept
    initial_concept = concept  # Store initial concept for chatbot context

    # Defining the message for the system and user prompts
    messages = [
        {"role": "system", "content": "You are a creative AI that can expand ideas into rich, multifaceted perspectives, helping users explore different dimensions of any concept."},
        {"role": "user", "content": f"""
Expand the concept: "{concept}" in multiple ways, providing diverse insights and approaches:

1️⃣ **Scientific Perspective:**
   - Explain the concept using logical reasoning, scientific theories, and empirical research.
   - Consider its implications in various scientific fields (e.g., physics, biology, technology).
   - What experiments or data support this idea, and what challenges might arise?

2️⃣ **Philosophical Perspective:**
   - Provide an existential, ethical, or metaphysical interpretation of the concept.
   - Explore questions of meaning, morality, and its impact on human existence.
   - How might different philosophical schools of thought (e.g., existentialism, utilitarianism, deontology) view this concept?

3️⃣ **Artistic Perspective:**
   - Describe how artists, writers, or filmmakers might interpret the concept in their creative works.
   - Explore visual, narrative, or musical representations.
   - How does this concept inspire artistic expression and innovation? Could it be portrayed through a painting, a poem, or a film?

4️⃣ **Humorous Perspective:**
   - Provide a funny, satirical, or exaggerated take on the concept.
   - What humorous comparisons, puns, or ironic observations can be made?
   - Imagine a comedic scenario where this concept leads to absurd or amusing outcomes.

5️⃣ **Real-World Applications:**
   - Discuss how this concept is applied in everyday life or in specific industries.
   - What real-world problems does it solve, or what new opportunities does it create?
   - How is this concept transforming fields like business, technology, healthcare, or education?

6️⃣ **Counterarguments & Criticism:**
   - What are the main opposing viewpoints or criticisms related to this concept?
   - Are there logical flaws, ethical concerns, or practical limitations?
   - What are the potential dangers or consequences of embracing this idea, and how can they be addressed?
    """
        }
    ]

    try:
        # Making the request to Nebius API
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct",  # Nebius best model
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle chatbot interaction based on the concept
def chatbot_response(conversation_history, user_message):
    # Check if the initial concept is provided
    if initial_concept is None:
        # If no concept has been provided, notify the user to enter one first
        return conversation_history + [{"role": "assistant", "content": "Please provide a concept or idea first before asking questions."}], ""

    # Append the user's message to the conversation history, with the initial concept in context
    conversation_history.append({"role": "user", "content": user_message})

    # Ensure every response is tied to the initial concept entered
    conversation_history.append({
        "role": "system",
        "content": f"Please respond to the user's question in the context of the concept: '{initial_concept}'."
    })

    # Generate a response based on the conversation history
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-fast",  # Nebius best model
            messages=conversation_history,
            temperature=0.7,
        )
        bot_message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": bot_message})
        return conversation_history, ""  # Clear user input after response
    except Exception as e:
        return conversation_history, f"Error: {str(e)}"

# Gradio UI Setup
with gr.Blocks() as demo:
    gr.Markdown("## 🌍 AI Thought Expander")
    gr.Markdown("Enter a concept and explore different perspectives!")

    # Create a row layout with two columns
    with gr.Row():
        # Left Column (Concept or Idea and its Output)
        with gr.Column():
            # Input and output UI elements for the concept or idea
            input_text = gr.Textbox(label="Enter a concept or idea", placeholder="e.g., Artificial Intelligence in Art")
            output_text = gr.Markdown(label="Expanded Perspectives")  # Space for output
            submit_btn = gr.Button("Expand Thought")  # Button to trigger concept expansion

        # Right Column (Chatbot area)
        with gr.Column():
            # Chatbot interface for asking follow-up questions
            chatbot = gr.Chatbot(label="AI Assistant - Ask Questions", type='messages')

            # Textbox to type in questions for the chatbot
            user_message = gr.Textbox(label="Ask a follow-up question", placeholder="e.g., Can you elaborate on the philosophical perspective?", interactive=True)
    
    # Handle concept expansion when the button is clicked
    submit_btn.click(fn=generate_expansion, inputs=[input_text], outputs=[output_text])

    # Handle chatbot responses when user submits a question
    user_message.submit(fn=chatbot_response, inputs=[chatbot, user_message], outputs=[chatbot, user_message])

# Launch the Gradio app
demo.launch()