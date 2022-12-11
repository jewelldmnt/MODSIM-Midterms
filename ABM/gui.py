
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkVideoPlayer import TkinterVideo
import pygame
pygame.mixer.init()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Users\Bernard\Desktop\Results\build\ABM\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1360x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



canvas.place(x = 0, y = 0)






videoplayer = TkinterVideo(master=window, scaled=True)
videoplayer.load(r"abm.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1042.5,
    y=417.0,
    width=172.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1042.5,
    y=488.0,
    width=172.0,
    height=41.0
)

is_on = True

on = PhotoImage(file=relative_to_assets("button_3.png"))
off = PhotoImage(file=relative_to_assets("button_4.png"))


def play():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=5)


play()


def stop():
    pygame.mixer.music.stop()


def switch():
    global is_on

    if is_on:
        button_3.config(image=off)
        button_3.config(command=stop())
        is_on = False

    else:
        button_3.config(image=on)
        button_3.config(command=play())
        is_on = True


button_3 = Button(
    image=on,
    borderwidth=0,
    highlightthickness=0,
    command=switch,
    relief="flat"
)
button_3.place(
    x=1168.0,
    y=0.0,
    width=192.0,
    height=91.0
)


window.resizable(False, False)
window.mainloop()
