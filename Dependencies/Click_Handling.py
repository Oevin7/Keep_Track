import customtkinter as ctk
class Entry(ctk.CTkEntry):
    def __init__(self, master= None, textvariable=None  ):
        self.master = master

        self.entry= ctk.CTkEntry(self.master);
        self.textvariable= textvariable

    def on_enter(self):
            print(self.on_enter())


    def enter_bind(self, on_enter=None):
        self.entry.bind("<Return>", lambda on_enter: self.entry.get())
        self.text_var = on_enter
        return self.text_var
    
