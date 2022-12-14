from tkinter import *
from pathlib import Path
import pygame


# Frame for Instructions page
class InstructionsPage(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # instructions page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the background design for instructions page
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        canvas.create_image(680.0, 400.0, image=self.image_bg)

        # creating the let's start button
        self.button_imgStart = PhotoImage(file=self.relative_to_assets("button_Start.png"))
        button_Start = Button(self, image=self.button_imgStart, borderwidth=0, highlightthickness=0,
                              command=lambda: controller.show_frame("First", controller.name), relief="flat")
        button_Start.place(x=611.0, y=623.0, width=138.0994873046875, height=43.87261962890625)

        # creating the back to home page button
        self.button_imgHome = PhotoImage(file=self.relative_to_assets("button_Home.png"))
        button_Home = Button(self, image=self.button_imgHome, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("HomePage", controller.name), relief="flat")
        button_Home.place(x=0.0, y=0.0, width=197.0, height=98.0)

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=1163.0, y=2.0, width=197.0, height=98.0)

        self.play()

    # function for the right path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # for playing the music
    def play(self):
        pygame.mixer.music.load("StartPage/assets/song.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=5)

    # for stopping the music
    def stop(self):
        pygame.mixer.music.stop()

    # on/off of the music
    def switch(self):
        if self.is_on:
            self.button_Sound.config(image=self.off)
            self.button_Sound.config(command=self.stop())
            self.is_on = False

        else:
            self.button_Sound.config(image=self.on)
            self.button_Sound.config(command=self.play())
            self.is_on = True
