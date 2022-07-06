# --- Modules --- #
from tkinter import *
from tkinter import messagebox
from random import choice

try:
    import Game
    import config
except ModuleNotFoundError:
    from Modules_Configs import Game, config

# --- Main Menu Window --- #
# List Button
class ListButton:
    def __init__(self, root, l_word, cmd):
        self.list_word = l_word
        self.cmd = cmd
        self.button = Button(root, text=self.list_word, bg="Red", fg="White",font=("Courier", 10, "bold"), height=5,
                             width=10, command=self.cmd)
        config.button_list.append(self)

    def pack(self, s=CENTER, px=0, py=0):
        self.button.pack(side=s, padx=px, pady=py)

# Window
class MainMenu:
    def __init__(self):
        # WINDOW
        self.mwin = Tk()
        self.mwin.title("Hangman")
        self.mwin.resizable(height=False, width=False)
        config.mwin = self.mwin

        self.lblframe = Frame(self.mwin)
        self.r1 = Frame(self.mwin)
        self.r2 = Frame(self.mwin)
        self.r3 = Frame(self.mwin)
        self.rl = Frame(self.mwin)

        self.lblframe.pack()
        self.r1.pack()
        self.r2.pack()
        self.r3.pack()
        self.rl.pack(side=BOTTOM)

        # WIDGETS
        self.label = Label(self.lblframe, text="Select at least one of the following topics.", font=("Calibri", 15))
        self.animals = ListButton(self.r1, "Animals", lambda: self.add_list(config.animals, self.animals))
        self.countries = ListButton(self.r1, "Countries", lambda: self.add_list(config.countries, self.countries))
        self.astronomy = ListButton(self.r1, "Astronomy", lambda: self.add_list(config.astronomy, self.astronomy))
        self.hard_words = ListButton(self.r2, "Hard Words", lambda: self.add_list(config.hard_words, self.hard_words))
        self.add_all = ListButton(self.r2, "Add All", self.add_all)
        self.clear_bttn = Button(self.rl, text="Clear Selected Topic", width=20, command=self.clear)
        self.proceed = Button(self.rl, text="Proceed to Game", width=20, command=self.proceed)

        self.label.pack()
        self.animals.pack(RIGHT, 5, 5)
        self.countries.pack(RIGHT, 5, 5)
        self.astronomy.pack(RIGHT, 5, 5)
        self.hard_words.pack(RIGHT, 5, 5)
        self.add_all.pack(RIGHT, 5, 5)
        self.clear_bttn.pack(side=RIGHT, padx=5, pady=10)
        self.proceed.pack(side=RIGHT, padx=5, pady=10)


        # VARIABLES
        self.listpool = []

        # SIZE AND POSITION
        self.posx = int(self.mwin.winfo_screenwidth() / 2 - config.winWidth / 2)
        config.positionx = self.posx
        self.posy = int(self.mwin.winfo_screenheight() / 2 - config.winHeight / 2)
        config.positiony = self.posy

        self.mwin.geometry(f"{config.winWidth}x{config.winHeight}+{config.positionx}+{config.positiony}")

        # MAINLOOP
        self.mwin.mainloop()

    def add_list(self, list, bttn):
        if not any(x in self.listpool for x in list):
            bttn.button['bg'] = "Green"
            self.listpool.extend(list)
        elif self.add_all.button['bg'] == "Green":
            bttn.button['bg'] = "Green"
            self.add_all.button['bg'] = "Red"
            self.listpool.clear()
            self.listpool.extend(list)
        else:
            bttn.button['bg'] = "Red"
            for item in list:
                self.listpool.remove(item)

    def add_all(self):
        if self.add_all.button['bg'] == "Red":
            self.listpool.clear()
            for item in config.topics:
                self.listpool.extend(item)
            for button in config.button_list:
                button.button['bg'] = "Red"
            self.add_all.button['bg'] = "Green"
        else:
            self.add_all.button.configure(bg="Red")
            self.listpool.clear()

    def clear(self):
        for button in config.button_list:
            button.button.configure(bg="Red")
        self.add_all.button.configure(bg="Red")
        self.listpool.clear()

    def proceed(self):
        if self.listpool == []:
            messagebox.showerror("! ERROR !","Please select at least one item from the selections !")
        else:
            config.retries = 6
            config.gameboard_str = ""
            config.gameboard = []
            config.wordl = []
            config.image_num = 0

            self.word = choice(self.listpool)
            for c in self.word:
                if c == " ":
                    config.wordl.append(" ")
                    config.gameboard.append(" ")
                    continue
                config.gameboard.append("_")
                config.wordl.append(c)

            config.gameboard_str = " ".join(config.gameboard)
            self.listpool.clear()
            for button in config.button_list:
                button.button['bg'] = "Red"

            Game.Game()
            self.mwin.withdraw()


if __name__ == "__main__":
    print("Main Menu Module - Part of 'Hangman'.")
    print("Uses - Displays Main Menu Window.")
