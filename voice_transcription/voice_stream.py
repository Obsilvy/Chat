import sys
sys.path.append("D:\pythonc-code\Chat")


import pvcheetah
import pyaudio
import numpy as np
from apis.api_handler import handle_sentence
from main import print_response


SAMPLE_RATE = 16000
FRAMES_PER_BUFFER = 512
API_KEY = "FPvQOZYGIaOjrKWiJzMyCnHxA8ta2C4a373bTyll9JleKL2EeQ1ilA=="
filter_word = "chat"
alternatives = ["jet", "chad"]
run = True

p = pyaudio.PyAudio()

for i in range(0, p.get_device_count()):
    print(p.get_device_info_by_index(i))
stream = p.open(
    frames_per_buffer=FRAMES_PER_BUFFER,
    rate=SAMPLE_RATE,
    format=pyaudio.paInt16,
    channels=1,
    input=True,
    input_device_index=1,
)
handle = pvcheetah.create(access_key=API_KEY, endpoint_duration_sec=1, enable_automatic_punctuation=True)


def get_next_audio_frame():
    data = stream.read(FRAMES_PER_BUFFER)
    audio_frame = np.frombuffer(data, dtype=np.int16)
    return audio_frame


def sentence_filter():
    if sentence.lower().startswith(filter_word):
        return sentence
    else:
        for word in alternatives:
            if sentence.startswith(word):
                sentence.replace(word, filter_word)
                return sentence
    return ""


while True:
    partial_transcript, is_endpoint = handle.process(get_next_audio_frame())
    if partial_transcript != "":
        print(partial_transcript)
    final_transcript = ""
    if is_endpoint:
        final_transcript = handle.flush()
        print("final: " + final_transcript)
    sentence = partial_transcript + final_transcript
    #if sentence_filter(sentence) != "":
       # print_response(handle_sentence(sentence))






