from config import client
import json

# filename = os.path.dirname(__file__) + "\output.wav"

# transcription = transcribe(filename)
def intent(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        stream=False,
    )

    intent_json = chat_completion.choices[0].message.content
    
    intent_data = json.loads(intent_json)
    return intent_data