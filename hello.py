from gtts import gTTS
from pygame import mixer
import tkinter as tk
import os

TEMPFILE = 'speech.mp3'


def say(text):
    if os.path.exists(TEMPFILE):
        os.unlink(TEMPFILE)

    if not text:
        return

    tts = gTTS(text=text)
    tts.save(TEMPFILE)
    mixer.music.load(TEMPFILE)
    mixer.music.play()


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('!!')
    root.wm_resizable(0, 0)
    mixer.init()
    entry = tk.Entry(root)
    btn = tk.Button(root, text='Say', command=lambda: say(entry.get()))
    entry.pack(side='left')
    btn.pack(side='right')
    root.mainloop()

