from tkinter import StringVar
import customtkinter as ctk
from Dependencies import BtnFrm as frm

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("green")

class Todo:

    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Todo List")
        self.window.geometry("500x750")

        self.add_prompt = ctk.CTkEntry(self.window, textvariable= StringVar())

        # button frame and buttons
        self.btnfrm = frm.button_frame_gen(self.window)
        self.btn_add = ctk.CTkButton(self.btnfrm, text= "Add", font= ("Sunny Spells Basic", 16), command= self.add_task)
        self.btn_add.grid(row= 0, column= 0, padx= 5, pady= 5)
        self.btn_del = ctk.CTkButton(self.btnfrm, text="Delete", font=("Sunny Spells Basic", 16))
        self.btn_del.grid(row=0, column=1, padx= 5, pady= 5)
        self.btn_manage = ctk.CTkButton(self.btnfrm, text="Manage", font=("Sunny Spells Basic", 16))
        self.btn_manage.grid(row=0, column=2, padx=5, pady= 5)

        self.btnfrm.pack(pady= 10)

        self.labl = ctk.CTkLabel(self.window, text=" ", font=("Sunny Spells Basic", 20))
        self.labl.pack(pady= 10)

        self.window.mainloop()

    def add_task(self):
        self.add_prompt.pack()
        self.add_prompt.bind("<Return>")
        task= self.add_prompt.get()

        if task != "":
            self.labl.configure(text= task)


Todo()