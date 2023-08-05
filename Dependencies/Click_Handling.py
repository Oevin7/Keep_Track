import customtkinter as ctk


class CstEntry(ctk.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.entry = ctk.CTkEntry(self.master)

    def on_enter(self):
        print(self.on_enter())

    def enter_bind(self, on_enter=None):
        self.entry.bind("<Return>", lambda on_enter: self.entry.get())
        textvariable = on_enter
        return textvariable
