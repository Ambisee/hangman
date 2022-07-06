# --- Modules --- #
from tkinter import *

try:
    import config
except ModuleNotFoundError:
    from Modules_Configs import config

# --- End Window --- #
# Parent End Winodw
class End:
    def __init__(self, w):
        # WINDOW
        self.end = Toplevel()
        self.end.resizable(width=False, height=False)
        self.end.protocol("WM_WINDOW_DELETE", self.end.quit)
        self.end.withdraw()

        self.sf = Frame(self.end)
        self.wf = Frame(self.end)
        self.bf = Frame(self.end)

        self.sf.pack()
        self.wf.pack()
        self.bf.pack(side=BOTTOM)

        # WIDGETS
        self.w = "The word is " + str(w)

        self.status = Label(self.sf, font=("Courier",35))
        self.status.pack()
        self.word = Label(self.wf, text=self.w, font=("Courier",20))
        self.word.pack(pady=10)
        self.image = Label(self.wf)
        self.image.pack()
        self.wquit = Button(self.bf, text="Quit (Q)", command=self.end.quit)
        self.wquit.pack(side=RIGHT, ipadx=20, ipady=10, padx=5, pady=5)
        self.retry = Button(self.bf, text="Retry (R)", command=self.replay)
        self.retry.pack(side=RIGHT, ipadx=20, ipady=10, padx=5, pady=5)

        # SIZE AND POSITION
        self.end.geometry(f"{config.winWidth}x{config.winHeight}+{config.positionx}+{config.positiony}")
        self.end.deiconify()
        self.end.focus_force()

        self.end.bind("r", self.kb_replay)
        self.end.bind("q", lambda event: self.end.quit())
        self.imgs = config.global_img[-2:]

    def replay(self):
        config.mwin.deiconify()
        self.end.destroy()
    
    def kb_replay(self, event):
        self.replay()

# Victory Sub-Class
class Victory(End):
    def __init__(self, w):
        super().__init__(w)
        self.image['image'] = self.imgs[1]
        self.end.protocol("WM_DELETE_WINDOW", self.end.quit)
        self.status.configure(text="VICTORY \nYou win !!!", fg="Green")

# Defeat Sub-Class
class Defeat(End):
    def __init__(self, w):
        super().__init__(w)
        self.image['image'] = self.imgs[0]
        self.end.protocol("WM_DELETE_WINDOW", self.end.quit)
        self.status.configure(text="DEFEAT \nYou lose !!!", fg="Red")

if __name__ == "__main__":
    print("End Module - Part of 'Hangman'.")
    print("Uses - Displays Victory or Defeat Window.")
