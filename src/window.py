from customtkinter import *

class Window(CTk):
    def __init__(self, w:int, h:int, title:str, resizable:bool):
        super().__init__()
        self.title(title)
        self.minsize(w, h)
        self.state("zoomed")
        self.resizable(resizable, resizable)
        set_appearance_mode("dark")
        
        self.columnconfigure(1, weight=5)
        self.rowconfigure(1, weight=2)

    def fullscreen(self):
        if not self.attributes("-fullscreen"):
            self.attributes("-fullscreen", True)
        else: self.attributes("-fullscreen", False)