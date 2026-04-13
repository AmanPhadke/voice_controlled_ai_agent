import sounddevice as sd
from scipy.io.wavfile import write

def audio_input(sample_rate = 44100, seconds=10):
    print("Recording...")
    myrecording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()
    write('modules\output.wav', sample_rate, myrecording)
    print('Done!')

audio_input()




