import tkinter as tk
from voice_transcription import voice_stream
from utils.audio_input_util import list_audio_devices
from utils.audio_input_util import get_index_by_name

chat_response = "Hi \n Hello"

audio_device_options = list_audio_devices()

#TODO Stream schließen und öffnen/Check ob Stream schon offen
run = True

window = tk.Tk(className="Chat")
window.geometry("400x300")

variable = tk.StringVar(window)
variable.set(audio_device_options[0])

audio_device_option_menu = tk.OptionMenu(window, variable, *audio_device_options)
audio_device_option_menu.pack()


chat_response_widget = tk.Label(window, font = "Helvetica 12 bold ", text=chat_response, pady=5,
                                wraplength="10c")



def start_recording_handler(event):
    print("Recording started")


def stop_recording_handler(event):
    print("Recording stopped")


def confirm_handler(event):
    print(variable.get())


def confirm_device():
    index = get_index_by_name(variable.get())
    voice_stream.set_input_index(index)
    voice_stream.open_stream()

def start_transcript():
    global run
    run = True
    voice_stream.open_stream()
    run_transcript()

def run_transcript():

    while run:
        chat_response = voice_stream.run_transcript()
        if chat_response != "":
            chat_response_widget.config(text=chat_response)
        window.update()



def stop_transcript():
    global run
    run = False
    voice_stream.close_stream()

confirm_button = tk.Button(text="Confirm", command=confirm_device)
confirm_button.pack()
chat_response_widget.pack()
start_recording_button = tk.Button(text="Start Recording", height=3, width=15, bg="blue", fg="white",
                                   command=start_transcript)
stop_recording_button = tk.Button(text="Stop Recording", height=3, width=15, bg="blue", fg="white",
                                  command=stop_transcript)
#start_recording_button.grid(row=4, column=4)
#stop_recording_button.grid(row=4, column=5)

start_recording_button.pack()
stop_recording_button.pack()

start_recording_button.bind("<Button-1>", start_recording_handler)
stop_recording_button.bind("<Button-1>", stop_recording_handler)
confirm_button.bind("<Button-1>", confirm_handler)


window.mainloop()
