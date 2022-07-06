# --- Modules --- #
from tkinter import *
from PIL import Image, ImageTk
import os

try:
    import config
    import End
except ModuleNotFoundError:
    from Modules_Configs import config, End

# --- Game Window --- #
# Character Button
class CharButton:
    def __init__(self, root, letter):
        # BUTTON
        self.letter = letter
        self.button = Button(root, text=letter, command=self.clicked, width=6, height=3)
        self.button.pack(side=LEFT, padx=2, pady=2)
        config.gamewin.bind(self.letter.lower(), self.kb_clicked)
        config.gamewin.bind(self.letter, self.kb_clicked)

    def kb_clicked(self, event):
        self.clicked()

    def clicked(self):
        if self.button['state'] == DISABLED:
            return

        if self.letter not in config.wordl:
            config.retries -= 1
            config.image_num += 1
            self.retry = "Attempts Remaining = " + str(config.retries)
            config.notification_label.configure(text="That letter is not in the word", fg="Red")
            config.retry_label.configure(text=self.retry)
            try:
                config.image_label.image = config.global_img[config.image_num]
                config.image_label['image'] = config.global_img[config.image_num]
            except IndexError:
                pass
        else:
            num = 0
            while True:
                try:
                    num = config.wordl.index(self.letter, num)
                    config.gameboard[num] = config.wordl[num]
                    num += 1
                except ValueError:
                    break
            config.gameboard_str = " ".join(config.gameboard)
            self.notif = '"' + self.letter + '" entered.'
            config.gameboard_label.configure(text=config.gameboard_str)
            config.notification_label.configure(text=self.notif,fg="Green")
        self.button.configure(state=DISABLED)
        if config.retries < 0:
            End.Defeat(''.join(config.wordl))
            config.gamewin.destroy()
        if config.gameboard == config.wordl:
            End.Victory(''.join(config.wordl))
            config.gamewin.destroy()

# Window
class Game(CharButton):
    def __init__(self):
        # WINDOW
        self.win = Toplevel()
        self.win.title("Hangman")
        self.win.resizable(height=False, width=False)
        self.win.protocol("WM_DELETE_WINDOW", self.win.quit)
        config.gamewin = self.win
        self.win.withdraw()

        self.retry_f = Frame(self.win)
        self.gameboard_f = Frame(self.win)
        self.image_f = Frame(self.win)
        self.notification_f = Frame(self.win)
        self.c1 = Frame(self.win)
        self.c2 = Frame(self.win)
        self.c3 = Frame(self.win)

        self.retry_f.pack()
        self.gameboard_f.pack()
        self.image_f.pack()
        self.notification_f.pack()
        self.c1.pack()
        self.c2.pack()
        self.c3.pack()

        # WIDGETS
        self.images = config.images(config.images_load)

        self.retry_l = Label(self.retry_f, text="Attempts Remaining = " + str(config.retries), font=("Courier",15))
        self.gameboard_l = Label(self.gameboard_f, text=config.gameboard_str, font=("Courier",15))
        self.image_l = Label(self.image_f, image=self.images[0])
        self.image_l.image = self.images[0]
        self.notification_l = Label(self.notification_f, text="Waiting ...", font=("Courier",15))

        self.retry_l.pack()
        self.gameboard_l.pack()
        self.image_l.pack(pady=5)
        self.notification_l.pack(pady=5)

        # REDEFINING CONFIG'S WIDGET VARIABLES
        config.retry_label = self.retry_l
        config.gameboard_label = self.gameboard_l
        config.image_label = self.image_l
        config.notification_label = self.notification_l
        config.global_img = self.images

        # CHARACTER BUTTONS
        self.q = CharButton(self.c1, "Q")
        self.w = CharButton(self.c1, "W")
        self.e = CharButton(self.c1, "E")
        self.r = CharButton(self.c1, "R")
        self.t = CharButton(self.c1, "T")
        self.y = CharButton(self.c1, "Y")
        self.u = CharButton(self.c1, "U")
        self.i = CharButton(self.c1, "I")
        self.o = CharButton(self.c1, "O")
        self.p = CharButton(self.c1, "P")
        self.a = CharButton(self.c2, "A")
        self.s = CharButton(self.c2, "S")
        self.d = CharButton(self.c2, "D")
        self.f = CharButton(self.c2, "F")
        self.g = CharButton(self.c2, "G")
        self.h = CharButton(self.c2, "H")
        self.j = CharButton(self.c2, "J")
        self.k = CharButton(self.c2, "K")
        self.l = CharButton(self.c2, "L")
        self.z = CharButton(self.c3, "Z")
        self.x = CharButton(self.c3, "X")
        self.c = CharButton(self.c3, "C")
        self.v = CharButton(self.c3, "V")
        self.b = CharButton(self.c3, "B")
        self.n = CharButton(self.c3, "N")
        self.m = CharButton(self.c3, "M")

        # SIZE AND POSITION
        self.win.geometry(f"{config.winWidth}x{config.winHeight}+{config.positionx}+{config.positiony}")
        self.win.deiconify()
        self.win.focus_force()


if __name__ == "__main__":
    print("Game Module - Part of 'Hangman'.")
    print("Uses - Displays Game Window.")
