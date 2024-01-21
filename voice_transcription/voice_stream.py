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
alternatives = ["jet", "chad", "chet", "church", "cat", "that", "said", "at", "cut"]
run = True
partial_sentence = ""
input_index = 1
stream = ""
open_voice_stream = False
p = pyaudio.PyAudio()



handle = pvcheetah.create(access_key=API_KEY, endpoint_duration_sec=1, enable_automatic_punctuation=True)

def open_stream():
    global open_voice_stream
    global stream
    if open_voice_stream == False:
        stream = p.open(
            frames_per_buffer=FRAMES_PER_BUFFER,
            rate=SAMPLE_RATE,
            format=pyaudio.paInt16,
            channels=1,
            input=True,
            input_device_index=input_index,
        )
    open_voice_stream = True

def close_stream():
    stream.close()
    global open_voice_stream
    open_voice_stream = False


def get_p_instance():
    return p


def is_stream_open():
    return open_voice_stream


def set_input_index(index):
    global input_index
    input_index = index
    global open_voice_stream
    open_voice_stream = False


def get_next_audio_frame():
    data = stream.read(FRAMES_PER_BUFFER)
    audio_frame = np.frombuffer(data, dtype=np.int16)
    return audio_frame


def sentence_filter(sentence):
    if sentence.lower().startswith(filter_word):
        return sentence
    else:
        for word in alternatives:
            if sentence.lower().startswith(word):
                sentence = sentence.lower().replace(word, filter_word)
                print(sentence)
                return sentence
    return ""


def run_transcript():
    global partial_sentence
    partial_transcript, is_endpoint = handle.process(get_next_audio_frame())
    if partial_transcript != "":
        partial_sentence = partial_transcript
    final_transcript = ""
    if is_endpoint:
        final_transcript = handle.flush()
        print("final: " + final_transcript)
    sentence = partial_sentence + final_transcript
    if sentence != "":
        print(sentence)
    if sentence_filter(sentence) != "" and is_endpoint:
        sentence = sentence_filter(sentence)
        chat_response = handle_sentence(sentence)
        partial_sentence = ""
    else:
        chat_response = ""
    if is_endpoint:
        partial_sentence = ""
    return chat_response





if __name__ == '__main__':
    sentence_filter("Cat hello.")
