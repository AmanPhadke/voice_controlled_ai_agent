# import os
# import json
# from config import client

# def transcribe(filename):
#     with open(filename, "rb") as file:
#         # Create a transcription of the audio file
#         transcription = client.audio.transcriptions.create(
#         file=file,
#         model="whisper-large-v3-turbo",
#         response_format="verbose_json",  # Optional
#         language="en", 
#         temperature=0.0
#         )

#         transcription = transcription.text
#         return transcription

import os
import json
import io
from config import client
import numpy as np
from scipy.io import wavfile

def transcribe(audio_input):
    if audio_input is None:
        return None
    
    sample_rate, audio_array = audio_input
    wav_buffer = io.BytesIO()
    wavfile.write(wav_buffer, sample_rate, audio_array.astype(np.int16))
    wav_buffer.seek(0)
    wav_buffer.name = "audio.wav"
    transcription = client.audio.transcriptions.create(
        file=wav_buffer,
        model="whisper-large-v3-turbo",
        language="en"
    )
    
    return transcription.text