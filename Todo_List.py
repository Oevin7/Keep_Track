import customtkinter as ctk
from Dependencies import Frame_Gen as Frm
from Dependencies import Click_Handling as Ch
import time

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("green")


class Todo:

    def __init__(self):
        # Window for program
        self.window = ctk.CTk()
        self.window.title("Todo List")
        self.window.geometry("750x500")

        # Entry Variables
        self.task_added = ctk.StringVar()
        self.task_deleted = ctk.StringVar()

        # Booleans to control UI
        self.add_task_on = False
        self.del_task_on = False

        # The list the label displays
        self.tdo_lst = {}
        self.count = 0

        # Frame for the entries and buttons
        self.etr_frm = Frm.frame_gen(self.window)

        # Entry button to add task
        self.etr_add_btn = ctk.CTkButton(self.etr_frm, text="Add", width=10, height=28, command=self.add_task)
        # enter_clicked = Ch.enter_click(etr=self.etr_add_btn, )

        # Entry button to delete task
        self.etr_del_btn = ctk.CTkButton(self.etr_frm, text="Delete", width=10, height=28,
                                         command=self.delete_task)

        # The entry itself
        self.add_prompt = Ch.CstEntry(master=self.window)

        # Delete Prompt for deleting tasks
        self.delete_prompt = Ch.CstEntry(master=self.window)

        # The label that displays the tasks
        self.labl_title = ctk.CTkLabel(self.window, text="Uncompleted Tasks", font=("Sunny Spells Basic", 50))
        self.labl_title.pack(padx=20, pady=20)

        self.lbl_frame = ctk.CTkFrame(self.window, border_width=2, width=500, height=200)
        self.lbl_frame["relief"] = "sunken"
        self.lbl_frame.pack(padx=10, pady=10)

        self.timed_lbl = ctk.CTkLabel()
        self.timed_lbl_frame = ctk.CTkFrame(self.window)

        self.labl = ctk.CTkLabel(self.lbl_frame, text="", font=("Sunny Spells Basic", 20))
        self.labl.pack()

        # button frame and buttons
        self.btnfrm = Frm.frame_gen(self.window)

        self.btn_add = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Add Task",
                                     font=("Sunny Spells Basic", 25),
                                     command=self.add_task_prompt)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_del = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Delete Task",
                                     font=("Sunny Spells Basic", 25),
                                     command=self.delete_task_prompt)
        self.btn_del.grid(row=0, column=1, padx=5, pady=5)

        self.btn_manage = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Manage Tasks",
                                        font=("Sunny Spells Basic", 25))
        self.btn_manage.grid(row=0, column=2, padx=5, pady=5)

        self.btnfrm.pack(pady=10)

        # Window
        self.window.mainloop()

    # Displays the prompt to add tasks
    def add_task_prompt(self):
        if not self.del_task_on:
            self.etr_frm.pack()
            self.add_prompt.pack()
            self.etr_add_btn.pack(side=ctk.RIGHT)
            self.add_prompt.enter_bind(self.add_task)
            self.add_task_on = True

    def dict_count(self):
        self.count += 1

    # Adds the task the user enters into the prompt
    def add_task(self):
        task = self.add_prompt.get()
        task = task.lower()

        if task not in self.tdo_lst:
            self.dict_count()
            self.tdo_lst[self.count] = task

            self.labl.configure(text=str(self.tdo_lst)[1:-1])

            self.etr_frm.pack_forget()
            self.etr_add_btn.pack_forget()
            self.add_prompt.pack_forget()
            self.add_prompt.delete(0, ctk.END)
            self.add_task_on = False

    # Deletes the task the user prompts
    def delete_task_prompt(self):
        if not self.add_task_on:
            self.etr_frm.pack()
            self.delete_prompt.pack()
            self.etr_del_btn.pack()
            self.del_task_on = True

    def delete_task(self):
        for task_num, task in self.tdo_lst.items():
            if task in self.tdo_lst.values():
                self.tdo_lst.pop(task_num)
        self.etr_frm.pack_forget()
        self.delete_prompt.pack_forget()
        self.delete_prompt.delete(0, ctk.END)
        self.etr_del_btn.pack_forget()
        self.del_task_on = False


Todo()
