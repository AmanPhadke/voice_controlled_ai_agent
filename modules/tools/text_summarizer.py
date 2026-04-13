import os
from config import client

def summarize(prompt):
    llm_prompt=(
    f'Summarize the following text: {prompt}'
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": llm_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        stream=False,
    )

    summary = chat_completion.choices[0].message.content
    return summary


