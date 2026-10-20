
# pyrefly: ignore[missing-import]
import gradio as gr
from dotenv import load_dotenv
import os
import json


from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Remove debug client.responses.create call if not needed
# response = client.responses.create(...)

# Load fitness FAQ knowledge base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_PATH = os.path.join(BASE_DIR, "data", "fitness_faq.json")
if not os.path.exists(FAQ_PATH):
    FAQ_PATH = os.path.join(BASE_DIR, "fitness_faq.json")

with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Format FAQ into a readable system prompt
faq_text = "\n\n".join(
    f"Q: {item['question']}\nA: {item['answer']}"
    for item in faq_data
)

SYSTEM_PROMPT = f"""You are an expert Fitness Coach AI assistant.
Use the following fitness knowledge base to answer questions accurately.
If the question is covered in the knowledge base, prioritize that answer.
If not, use your general fitness knowledge to help.

=== FITNESS KNOWLEDGE BASE ===
{faq_text}
==============================

Always be encouraging, clear, and practical in your responses.
"""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def chat(message, history):
    # Append user message
    conversation_history.append({"role": "user", "content": message})
    try:
        response = client.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=conversation_history
        )
        reply = response.choices[0].message.content
        # Append assistant response
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=chat,
    title="🏋️ Fitness Coach AI",
    description="Ask me anything about exercises, workout plans, and recovery! Powered by your fitness knowledge base.",
    examples=["How to lose weight?", "How to gain weight?", "How to build muscle?", "What is the best chest exercise?", "How many rest days do I need?"],
)

if __name__ == "__main__":
    demo.launch(share=True, theme=gr.themes.Soft())
