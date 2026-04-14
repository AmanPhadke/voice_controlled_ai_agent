# Voice Controlled AI Agent

An AI Agent that converts speech into actionable tasks using LLMs.

---


Demo Video: [https://youtu.be/nCn8jaKRF4c]


Medium Blog: [https://medium.com/@amanphadke004/how-i-created-my-own-voice-controlled-ai-agent-2a6891a996df]


---

## Features

- Audio Input
  - Microphone recording
  - Audio file upload (.wav)

- Speech-to-Text
  - Groq Whisper (`whisper-large-v3-turbo`)

- Intent Classification
  - create_file
  - write_code
  - summarize
  - chat

- Actions
  - File creation
  - Code generation & writing
  - Text summarization
  - General chat

- UI
  - Built with Gradio
  - Displays transcription, intent, action, output

---

## 🏗️ Project Structure

```
VOICE CONTROLLED AGENT/
│
├── modules/
│   ├── audio_input.py          # Handles audio recording
│   ├── speech_to_text.py       # Transcription logic (Groq API)
│   ├── intent_classifier.py    # Intent detection using LLM
│   ├── general_chat.py         # Chat functionality
│   ├── tools/
│   │   ├── files_operations.py # File creation & writing
│   │   ├── text_summarizer.py  # Text summarization
│
├── app.py                      # Gradio UI
├── main.py                     # Main pipeline execution
├── config.py                   # API keys/config
├── .env                        # Environment variables
└── output/                     # Generated files (safe directory)
```

---

## Architecture

1. Audio Input (Mic / Upload)  
2. Speech => Text (Groq Whisper)  
3. Intent Detection (LLM JSON Output)  
4. Action Execution  
5. UI Display (Gradio)  

---

## Example Flow

**Input:**  
"Create a Python file with a retry function"

**Steps:**
1. Transcription  
2. Intent = write_code  
3. Code Generation  
4. File Creation in `/output`  
5. Display Result  

---

## Tech Stack

- Python
- Groq API (Whisper + LLM)
- Gradio
- sounddevice
- scipy

---

## Why API Instead of Local Models?

- Low local compute power  
- Faster inference  
- More stable than local Whisper  

---

## Setup

### 1. Clone

```bash
git clone https://github.com/AmanPhadke/voice_controlled_ai_agent.git
cd voice_controlled_ai_agent
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Environment

Create `.env`:

```
API_KEY = your_api_key_here
```

### 4. Run

```bash
python app.py
```

---

## Challenges

- JSON parsing errors from LLM  
- Audio format mismatch (NumPy → WAV)  
- API rate limits  
- Prompt engineering for structured output  

---

## Future Improvements

- Compound commands  
- Confirmation before file operations  
- Memory/history  
- Multi-language support  
- Better error handling  

---

## 👨‍💻 Author

**Aman Phadke**  
Indore, India  
Aspiring ML Engineer
