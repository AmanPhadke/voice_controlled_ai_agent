import os
from config import client
import json
from datetime import datetime


def create_file(intent_result):
    filename = intent_result["parameters"].get("filename")
    if not filename:
        filename = 'new file'
    filename = filename.replace(' ', '_')
    content = intent_result["parameters"].get("content", "")
    language = intent_result["parameters"].get("language")
    language = language.lower()

    extensions = {
            "python": ".py",
            "javascript": ".js",
            "java": ".java",
            "c++": ".cpp"
        }
    
    valid_ext = extensions.get(language, ".txt")

    os.makedirs("output", exist_ok=True)
    with open(f"output/{filename + valid_ext}", "w") as f:
        f.write(content)
    
    return {
        "success": True,
        "file_path": f"output/{filename}",
        "message": "File Created"
    }


def write_file(intent_result):
    filename = intent_result["parameters"].get("filename")
    if not filename:
        filename = 'new file' 
    filename = filename.replace(' ', '_')
    language = intent_result["parameters"].get("language")
    language = language.lower()

    extensions = {
            "python": ".py",
            "javascript": ".js",
            "java": ".java",
            "c++": ".cpp"
        }
    
    valid_ext = extensions.get(language, ".txt")

    function = intent_result['parameters'].get('task')

    prompt=(
    f'Write an efficient code of language = {language} performing this function: {function}'
    f'STRICTLY DO NOT EXPLAIN THE CODE ONLY GIVE THE CODE AS AN OUTPUT THAT IS IT'
    f'Also DO NOT USE (``) THESE QUOTES IN THE OUTPUT'
    )

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

    code = chat_completion.choices[0].message.content

    os.makedirs("output", exist_ok=True)
    with open(f"output/{filename + valid_ext}", "w") as f:
        f.write(code)

    return {
        "success": True,
        "file_path": f"output/{filename}",
        "message": "Written code performing: {function}",
        "code": code
    }


def save_summary(summary_text):
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"output/summary_{timestamp}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary_text)

    return {
        "success": True,
        "file_path": file_path,
        "message": "Summary saved"
    }

