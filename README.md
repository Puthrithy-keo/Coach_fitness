# AI_Chatbot_Fitness
About my project

## Fitness Coach AI Chatbot

Fitness Coach AI is an AI-powered fitness coaching assistant built with a curated knowledge base, Groq-accelerated LLMs, and a Gradio conversational interface.

## 1. The Target User
- **Beginner to Intermediate Gym Goers:** Individuals seeking clear guidance on workout routines, exercises, and proper form.
- **Fitness Enthusiasts:** People looking for practical advice on muscle building, fat loss, and rest/recovery.
- **Busy Individuals:** Users who need fast, actionable answers without scrolling through conflicting online articles.

## 2. The User Need
- **Instant & Reliable Fitness Guidance:** Fast answers to common questions about exercises, nutrition, and recovery.
- **Context-Aware Recommendations:** Advice grounded in vetted fitness principles rather than generic or unsafe suggestions.
- **Accessible Chat Interface:** An intuitive, conversational platform that retains context and is available anytime.

## 3. The Knowledge Base
- **File:** [`data/fitness_faq.json`](file:///d:/0.SUNRISE/DS/AI/AI_Chatbot_Fitness/data/fitness_faq.json)
- **Content:** Curated questions and answers covering key fitness topics:
  - **Exercises & Form:** Compound and isolation lifts (e.g., bench press, squats, back development).
  - **Workout Plans:** Split routines, training frequency, rest days, and progressive overload.
  - **Nutrition & Weight Management:** Hypertrophy, fat loss, calorie deficits, and protein intake.
  - **Recovery & Injury Prevention:** Soreness management, sleep, and warm-up protocols.
- **Search & Retrieval:** Indexed using `minsearch` for fast keyword-based retrieval and injected into the LLM context.

## 4. The Ideal Output
- **Accurate & Knowledge-Grounded:** Answers directly align with the curated FAQ knowledge base when a topic is covered.
- **Practical & Actionable:** Clear instructions (e.g., recommended sets, reps, form cues, or nutrition targets).
- **Safe & Encouraging Tone:** Empathetic, motivating, and mindful of training safety.
- **Concise:** Directly addresses the user's question without unnecessary filler text.

## 5. Success Metrics
- **Retrieval Performance:**
  - **Hit Rate@K:** Proportion of test queries where the correct FAQ document appears in the top-K results (target: $\ge 85\%$).
  - **MRR (Mean Reciprocal Rank):** Evaluates how close the correct document ranks to the top position.
- **Generation Quality (LLM-as-a-Judge):**
  - **Relevance Rate:** Evaluated via [`judge.py`](file:///d:/0.SUNRISE/DS/AI/AI_Chatbot_Fitness/judge.py) (`RELEVANT`, `PARTLY_RELEVANT`, `NON_RELEVANT`) aiming for $\ge 90\%$ `RELEVANT`.
  - **Groundedness / Hallucination Rate:** Minimizing non-factual or fabricated health claims.
- **Latency & Usability:**
  - Response latency under 2 seconds (powered by Groq LPUs).

## 6. How to Setup This Project

### Prerequisites
- Python 3.12+
- A [Groq API Key](https://console.groq.com/)

### Step 1: Clone and Navigate to the Repository
```bash
git clone <repository-url>
cd AI_Chatbot_Fitness
```

### Step 2: Set Up Virtual Environment & Dependencies
Using `uv`:
```bash
uv venv
uv pip install -r pyproject.toml
uv pip install gradio pydantic
```
Or using standard `pip`:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -e .
pip install gradio pydantic
```

### Step 3: Configure Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 4: Run the Application
Launch the Gradio Chatbot UI:
```bash
python app.py
```
Open the provided local URL (e.g., `http://127.0.0.1:7860`) in your browser.

### Step 5: (Optional) Run Evaluation & Indexing
- **Index creation & search validation:** Open and run [`ingest_and_index.ipynb`](file:///d:/0.SUNRISE/DS/AI/AI_Chatbot_Fitness/ingest_and_index.ipynb).
- **Retrieval & LLM Judge evaluation:** Run [`judge.py`](file:///d:/0.SUNRISE/DS/AI/AI_Chatbot_Fitness/judge.py) or execute [`rag-eval.ipynb`](file:///d:/0.SUNRISE/DS/AI/AI_Chatbot_Fitness/rag-eval.ipynb).