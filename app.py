import gradio as gr
from modules.speech_to_text import transcribe
from modules.intent_classifier import intent
from modules.tools.files_operations import create_file, write_file, save_summary
from modules.tools.text_summarizer import summarize


def process_audio(audio_input, text_input):
    transcription = transcribe(audio_input)
    user_input = transcription if transcription else text_input
    prompt = ('''
        Classify the user intent into these following categories: ["create_file", "write_code", "summarize", "chat"]
        only give the following json file as an ouput and nothing else.
        {
            intent: one of ["create_file", "write_code", "summarize", "chat"]
            parameters: relevant details (e.g., language for code, filename for file creation)
            confidence: how sure the model is (0-1)
        }

        IMPORTANT NOTES:
        1. WHENEVER GIVING FILE NAME DO NOT ADD FILE EXTENTION IN IT BECAUSE THE LANGUAGE IS ALREADY MENTIONED IN THE language parameter
        2. IF THE USER ASKS TO CREATE A FILE AND THEN WRITE CODE IN IT classify it as 'write_code' intent
        3. IF THE USER WANT TO WRITE SOME CODE ALSWAYS CREATE A NEW PARAMETER CALLED 'task' AND STORE WHATEVER THE USER WANTS THE CODE TO 
        DO in it not the whole code just its short description

        Return EXACTLY this format:
        {{"intent": "...", "parameters": {{}}, "confidence": ...}}

        It should only be one of these 4 intents nothing else
        '''
        f'\nUser_Prompt = {user_input}'

    )

    intent_result = intent(prompt)
    intent_type = intent_result['intent']


    if intent_type == "write_code":
        result = write_file(intent_result)
        output_msg = f"Code saved to: {result.get('file_path')}\n\nCode:\n{result.get('code', 'N/A')}"
    elif intent_type == "create_file":
        result = create_file(intent_result)
        output_msg = f"File created: {result.get('file_path')}"
    elif intent_type == "summarize":
        text_to_summarize = text_input if text_input else user_input
        intent_result.setdefault("parameters", {})
        intent_result["parameters"]["text"] = text_to_summarize
        summary = summarize(text_to_summarize)
        save_result = save_summary(summary)
        output_msg = f"Summary:\n{summary}\n\nSaved to: {save_result.get('file_path')}"
    else:
        result = {"success": False, "message": "Unknown intent"}
        output_msg = result["message"]

    return transcription, intent_result["intent"], output_msg


with gr.Blocks() as app:
    gr.Markdown("Voice Controlled AI Agent")
    
    audio_input = gr.Audio(sources=["microphone", "upload"], label="Record or Upload Audio")
    text_input = gr.Textbox(label="Paste text to summarize (if needed)", lines=5)  # New!
    process_btn = gr.Button("Process")
    
    output_transcript = gr.Textbox(label="Transcribed Text")
    output_intent = gr.Textbox(label="Detected Intent")
    output_result = gr.Textbox(label="Result", lines=20)
    
    process_btn.click(
        process_audio,
        inputs=[audio_input, text_input],
        outputs=[output_transcript, output_intent, output_result]
    )

app.launch()