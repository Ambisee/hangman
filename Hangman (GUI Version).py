#---MODULES---#
from tkinter import *
from random import *
from tkinter import messagebox

# >>>>>>>>>> MAIN WINDOW INITIALIZATION <<<<<<<<<< #
mwin = Tk()
mwin.title("Hangman")
mwin.withdraw()
mwin.resizable(height=False, width=False)

#---PLACEMENT---#
winHeight = 400
winWidth = 600

positionx = int(mwin.winfo_screenwidth() / 2 - winWidth / 2)
positiony = int(mwin.winfo_screenheight() / 2 - winHeight / 2)

mwin.geometry("{}x{}+{}+{}".format(winWidth, winHeight, positionx, positiony))

#--- MAIN WINDOW FRAMES---#
retry_frame = Frame(mwin)
gameboard_frame = Frame(mwin)
notification_frame = Frame(mwin)
char1_frame = Frame(mwin)
char2_frame = Frame(mwin)
char3_frame = Frame(mwin)

retry_frame.pack()
gameboard_frame.pack()
notification_frame.pack()
char1_frame.pack()
char2_frame.pack()
char3_frame.pack()

#---MAIN WINDOW MUTABLE WIDGETS---#
retry_label = Label(retry_frame, font=("Courier", 15))
gameboard_label = Label(gameboard_frame, font=("Courier", 15))
notification_label = Label(notification_frame, font=("Courier", 15))

retry_label.pack()
gameboard_label.pack()
notification_label.pack()

# >>>>>>>>>> INITIATE WINDOW <<<<<<<<<< #
#---TOPICS DATABASE---#
animals = ["TIGER", "LION", "GIRAFFE", "BULL", "ELEPHANT", "FOX", "CAT", "DOG", "EAGLE", "MOUSE", "SHARK", "WHALE",
           "CHEETAH", "LEOPARD", "GRASSHOPPER", "SPIDER", "SQUID", "OCTOPUS", "SNAKE", "TURTLE", "TORTOISE", "PIGEON",
           "FALCON", "CHICKEN", "COW", "PIG", "DONKEY", "HORSE"]
countries = ["INDONESIA", "MALAYSIA", "INDIA", "CHINA", "JAPAN", "FRANCE", "AUSTRALIA", "NEW ZEALAND", "CANADA",
             "UNITED STATES OF AMERICA", "ENGLAND", "IRELAND", "SINGAPORE", "THAILAND", "SOUTH KOREA", "EGYPT",
             "GREECE", "ITALY", "ZIMBABWE", "PORTUGAL", "PERU", "NEPAL", "UKRAINE", "MOZAMBIQUE", "TUVALU"]
astronomy = ["MERCURY", "VENUS", "EARTH", "MARS", "JUPITER", "SATURN", "NEPTUNE", "URANUS", "NEBULA", "THE MILKY WAY",
             "ANDROMEDA", "STAR", "MOON", "SOLAR SYSTEM", "GALAXY", "ASTEROID", "COMET", "METEORITE", "METEOR", "ORBIT",
             "OUTER SPACE", "CONSTELLATION", "PLUTO", "SUPERNOVA"]
hard_words = ["MATRIX", "HIEROGLYPHS", "RICKSHAW", "ZEPHYR", "JAZZ", "QUIZZES", "QUINTESSENTIAL", "CRYPT", "SCHIZOPHRENIA",
              "PSYCHIC", "ZIPPER", "ZILCH", "MAGNANIMOUS"]

topics = [animals, countries, astronomy, hard_words]

#---GLOBAL VARIABLES---#
gameboard = []
gameboard_str = ""
wordl = []

#---INITIATION WINDOW---#
class ListButton:
    def __init__(self, root, l_word, cmd):
        self.list_word = l_word
        self.cmd = cmd

        self.button = Button(root, text=self.list_word, bg="Red", fg="White", font=("Courier", 10, "bold"), height=5, width=10, command=self.cmd)

    def pack(self, s, px, py):
        self.button.pack(side=s, padx=px, pady=py)


class InitiateWindow:
    global retry_label
    global gameboard_label
    global notification_label

    global gameboard
    global gameboard_str
    global wordl

    listpool = []
    word = ""
    retry_str = ""

    def __init__(self):
        # WINDOW ( FRAMES, SIZE, POSITION )
        initiate = self.initiate =  Toplevel(mwin)
        initiate.title("Topics Selection")
        initiate.resizable(height=False, width=False)
        initiate.geometry("{}x{}+{}+{}".format(winWidth, winHeight, positionx, positiony))
        initiate.protocol("WM_DELETE_WINDOW", mwin.quit)
        initiate.deiconify()

        lbl1_frame = self.lblframe = Frame(initiate)
        b_row_1 = self.r1 = Frame(initiate)
        b_row_2 = self.r2 = Frame(initiate)
        b_row_3 = self.r3 = Frame(initiate)
        b_row_last = self.rl = Frame(initiate)

        lbl1_frame.pack()
        b_row_1.pack()
        b_row_2.pack()
        b_row_3.pack()
        b_row_last.pack(side=BOTTOM)

        # WIDGETS
        label = self.label = Label(lbl1_frame, text="Select at least one of the following topics.", font=("Calibri", 15))
        label.pack()

        animals_bttn = self.animals = ListButton(b_row_1, "Animals", lambda: self.add_list(animals, animals_bttn))
        countries_bttn = self.countries = ListButton(b_row_1, "Countries", lambda: self.add_list(countries, countries_bttn))
        astronomy_bttn = self.astronomy = ListButton(b_row_1, "Astronomy", lambda: self.add_list(astronomy, astronomy_bttn))
        hard_words_bttn = self.hard_words = ListButton(b_row_2, "Hard Words", lambda: self.add_list(hard_words, hard_words_bttn))

        animals_bttn.pack(RIGHT, 5, 5)
        countries_bttn.pack(RIGHT, 5, 5)
        astronomy_bttn.pack(RIGHT, 5, 5)
        hard_words_bttn.pack(RIGHT, 5, 5)

        self.bttn_list = [animals_bttn, countries_bttn, astronomy_bttn, hard_words_bttn]

        self.add_all = ListButton(b_row_2, "Add All", self.add_all)
        self.add_all.pack(RIGHT, 5, 5)

        self.clear_bttn = Button(b_row_last, text="Clear Selected Topic", width=20, command=self.clear)
        self.proceed = Button(b_row_last, text="Proceed to Game", width=20, command=self.proceed)

        self.clear_bttn.pack(side=RIGHT, padx=5, pady=10)
        self.proceed.pack(side=RIGHT, padx=5, pady=10)

    def add_list(self, l, bttn):
        if any(x in self.listpool for x in l) == False:
            bttn.button.configure(bg="Green")
            self.listpool.extend(l)
        elif self.add_all.button["bg"] == "Green":
            bttn.button.configure(bg="Green")
            self.add_all.button.configure(bg="Red")
            self.listpool.clear()
            self.listpool.extend(l)
        else:
            bttn.button.configure(bg="Red")
            for item in l:
                self.listpool.remove(item)

    def add_all(self):
        if self.add_all.button['bg'] == "Red":
            self.listpool.clear()
            for item in topics:
                self.listpool.extend(item)
            for button in self.bttn_list:
                button.button.configure(bg="Red")
            self.add_all.button.configure(bg="Green")
        else:
            self.add_all.button.configure(bg="Red")
            self.listpool.clear()

    def clear(self):
        for button in self.bttn_list:
            button.button.configure(bg="Red")
        self.add_all.button.configure(bg="Red")
        self.listpool.clear()

    def proceed(self):
        if self.listpool == []:
            messagebox.showerror("! ERROR !", "Please select at least one of the selections !")
        else:
            global retries

            self.word = choice(self.listpool)
            for c in self.word:
                if c == " ":
                   wordl.append(" ")
                   gameboard.append(" ")
                   continue
                gameboard.append("_")
                wordl.append(c)
            retries = 6
            gameboard_str = " ".join(gameboard)
            self.retry_str = "Attempts Remaining = " + str(retries)

            retry_label.configure(text=self.retry_str)
            gameboard_label.configure(text=gameboard_str)
            notification_label.configure(text="Waiting ...")
            self.initiate.withdraw()
            mwin.deiconify()


InitWin = InitiateWindow()

# >>>>>>>>>> END WINDOW <<<<<<<<<< #
class End:
    def __init__(self, w):
        # WINDOW ( FRAME, SIZE, POSITION )
        end = self.end = Toplevel(mwin)
        end.geometry("{}x{}+{}+{}".format(winWidth, winHeight, positionx, positiony))
        end.resizable(width=False, height=False)
        end.protocol("WM_WINDOW_DELETE", mwin.quit)
        end.deiconify()

        status_frame = self.sf = Frame(end)
        word_frame = self.wf = Frame(end)
        button_frame = self.bf = Frame(end)

        status_frame.pack()
        word_frame.pack()
        button_frame.pack(side=BOTTOM)

        # WIDGETS
        self.w = "The word is " + str(w)

        status = self.status = Label(status_frame, font=("Courier", 35))
        status.pack()
        word = self.word = Label(word_frame, text=self.w, font=("Courier", 20))
        word.pack(pady=70)
        wquit = self.wquit = Button(button_frame, text="Quit", command=mwin.quit)
        wquit.pack(side=RIGHT, ipadx=20, ipady=10, padx=5, pady=5)
        retry = self.retry = Button(button_frame, text="Retry", command=self.replay)
        retry.pack(side=RIGHT, ipadx=20, ipady=10, padx=5, pady=5)

    def replay(self):
        global gameboard_str
        global gameboard
        global wordl

        InitWin.initiate.deiconify()
        self.end.withdraw()
        InitWin.add_all.button.configure(bg="Red")
        InitWin.listpool.clear()
        gameboard.clear()
        wordl.clear()
        gameboard_str = ""
        for bttn in InitWin.bttn_list:
            bttn.button.configure(bg="Red")
        for bttn in q.bttn_list:
            bttn.configure(state=NORMAL)

class Victory(End):
    def __init__(self, w):
        super().__init__(w)
        self.end.protocol("WM_DELETE_WINDOW", mwin.quit)
        self.status.configure(text="VICTORY \nYou win !!!", fg="Green")

class Defeat(End):
    def __init__(self, w):
        super().__init__(w)
        self.end.protocol("WM_DELETE_WINDOW", mwin.quit)
        self.status.configure(text="DEFEAT \nYou lose !!!", fg="Red")


# >>>>>>>>>> MAIN WINDOW WIDGET <<<<<<<<<< #
class CharB:
    bttn_list = []

    def __init__(self, root, letter):
        self.letter = letter
        self.button = Button(root, text=letter, command=self.input, width=6, height=3)
        self.button.pack(side=LEFT, padx=2, pady=2)
        self.bttn_list.append(self.button)
        mwin.bind(self.letter.lower(), self.kb_input)
        mwin.bind(self.letter, self.kb_input)

    def kb_input(self, event):
        self.input()

    def input(self):
        global gameboard_label
        global retry_label
        global notification_label

        global gameboard
        global gameboard_str
        global retries
        global wordl

        if self.button['state'] == DISABLED:
            return

        if self.letter not in wordl:
            retries -= 1
            self.retry = "Attempts Remaining = " + str(retries)
            notification_label.configure(text="That letter is not in the word", fg="Red")
            retry_label.configure(text=self.retry)
        else:
            num = 0
            while True:
                try:
                    num = wordl.index(self.letter, num)
                    gameboard[num] = wordl[num]
                    num += 1
                except ValueError:
                    break
            gameboard_str = " ".join(gameboard)
            self.notif = '"' + self.letter + '" entered.'
            gameboard_label.configure(text=gameboard_str)
            notification_label.configure(text=self.notif, fg="Green")
        if retries < 0:
            self.defeat = Defeat(''.join(wordl))
            mwin.withdraw()
        if gameboard == wordl:
            self.victory = Victory(''.join(wordl))
            mwin.withdraw()
        self.button.configure(state=DISABLED)

#---CREATING BUTTONS---#
q = CharB(char1_frame, "Q")
w = CharB(char1_frame, "W")
e = CharB(char1_frame, "E")
r = CharB(char1_frame, "R")
t = CharB(char1_frame, "T")
y = CharB(char1_frame, "Y")
u = CharB(char1_frame, "U")
i = CharB(char1_frame, "I")
o = CharB(char1_frame, "O")
p = CharB(char1_frame, "P")
a = CharB(char2_frame, "A")
s = CharB(char2_frame,"S")
d = CharB(char2_frame, "D")
f = CharB(char2_frame, "F")
g = CharB(char2_frame, "G")
h = CharB(char2_frame,"H")
j = CharB(char2_frame, "J")
k = CharB(char2_frame, "K")
l = CharB(char2_frame, "L")
z = CharB(char3_frame, "Z")
x = CharB(char3_frame, "X")
c = CharB(char3_frame, "C")
v = CharB(char3_frame, "V")
b = CharB(char3_frame, "B")
n = CharB(char3_frame, "N")
m = CharB(char3_frame,"M")

# >>>>>>>>>> MAINLOOP <<<<<<<<<< #
mwin.mainloop()