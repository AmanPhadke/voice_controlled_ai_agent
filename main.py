from modules.intent_classifier import intent_result
from modules.tools.files_operations import create_file, write_file
from modules.tools.text_summarizer import summarize

intent_type = intent_result["intent"]
    
if intent_type == "create_file":
    create_file(intent_result)


elif intent_type == 'write_code':
    write_file(intent_result)

elif intent_type == 'summarize':
    user_input = input('What would you like to summarize? Paste or write the prompt here: ')
    print(f'\n\nSummary: {summarize(user_input)}')

    
