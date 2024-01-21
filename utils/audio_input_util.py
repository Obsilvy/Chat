import pyaudio
from voice_transcription.voice_stream import get_p_instance

p = get_p_instance()

def list_audio_devices():
    l = []
    for i in range(0, p.get_device_count()):
        l.append(p.get_device_info_by_index(i)['name'])
    return l

def get_index_by_name(name):
    for i in range(0, p.get_device_count()):
        if p.get_device_info_by_index(i)['name'] == name:
            return p.get_device_info_by_index(i)['index']


if __name__ == "__main__":
    list_audio_devices(pyaudio.PyAudio())