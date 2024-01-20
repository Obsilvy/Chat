import tkinter as tk
from voice_transcription import voice_stream

chat_response = "Hi \n Hello"


window = tk.Tk()

chat_response_widget = tk.Label(text=chat_response)
chat_response_widget.pack()

start_recording_button = tk.Button(text="Start Recording", height=5, width=25, bg="blue", fg="white",
                                   command=voice_stream.start_transcript())
stop_recording_button = tk.Button(text="Stop Recording", height=5, width=25, bg="blue", fg="white",
                                  command=voice_stream.stop_transcript())


start_recording_button.pack()
stop_recording_button.pack()


def start_recording_handler(event):
    print("Recording started")


def stop_recording_handler(event):
    print("Recording stopped")


start_recording_button.bind("<Button-1>", start_recording_handler)
stop_recording_button.bind("<Button-1>", stop_recording_handler)

window.mainloop()
