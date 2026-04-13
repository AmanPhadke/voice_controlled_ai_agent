from config import client


def chat_response(user_input):
    prompt = (
        'You are a helpful, concise AI assistant in a voice-controlled desktop app. '
        'Answer naturally and clearly. '
        f'\nUser: {user_input}'
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        stream=False,
    )

    return chat_completion.choices[0].message.content
