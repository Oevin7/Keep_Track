import customtkinter as ctk
import enum


class Process(enum.Enum):
    BLANK = ""
    ADD = "add"
    DEL = "del"
    MAN = "manage"
    NOTES = "notes"
    CAL = "calender"
    TDO = "todo"


class Todo:

    def __init__(self, window):
        # Window for program
        self.window = window

        # Entry Variables
        self.task_added = ctk.StringVar()
        self.task_deleted = ctk.StringVar()

        # self.ui_settings = ctk.CTkComboBox(self.window, values=["blue", "dark-blue", "green"], command=self.ui_change)
        # self.ui_theme = self.ui_change()

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.font = "Alice Yotsuba Inc."

        # Booleans to control UI
        self.task_process = Process.BLANK
        self.other_process = False

        # The list the label displays
        self.tdo_lst = {}
        self.tdo_lst_del = {}
        self.count = 0

        self.main_frame = ctk.CTkFrame(self.window, height=700, width=500)

        self.btn_frame = ctk.CTkFrame(self.main_frame, height=120)
        self.btn_frame.place(x=0)

        self.add_btn = ctk.CTkButton(self.btn_frame, text="Add", font=(self.font, 16), command=self.add_task_prompt)
        self.add_btn.place(x=30, y=15)

        self.del_btn = ctk.CTkButton(self.btn_frame, text="Delete", font=(self.font, 16), command=self.delete_task_prompt)
        self.del_btn.place(x=30, y=45)

        self.man_btn = ctk.CTkButton(self.btn_frame, text="Manage", font=(self.font, 16))
        self.man_btn.place(x=30, y=75)

        self.etr_frame = ctk.CTkFrame(self.main_frame, height=50, width=100)
        self.prompt = ctk.CTkEntry(self.etr_frame)
        self.etr_add_btn = ctk.CTkButton(self.etr_frame, text="Add", font=(self.font, 14), command=self.add_task)

        self.etr_del_btn = ctk.CTkButton(self.etr_frame, text="Delete", font=(self.font, 14), command=self.delete_task)

        self.lst_frame = ctk.CTkFrame(self.main_frame, width=260)
        self.lst_frame.pack_propagate(False)
        self.lst_frame.place(x=220)

        self.timed_lbl_frame = ctk.CTkFrame(self.main_frame, height=50, width=100)
        self.timed_lbl_frame.pack_propagate(False)
        self.timed_lbl = ctk.CTkLabel(self.timed_lbl_frame)

        self.uncompleted = ctk.CTkLabel(self.lst_frame, text="Uncompleted Tasks:", compound="center",  font=(self.font, 20))
        self.labl = ctk.CTkLabel(self.lst_frame, text="", font=(self.font, 16), wraplength=220, justify=ctk.LEFT)
        self.uncompleted.pack(pady=10)
        self.labl.pack()
        self.main_frame.pack()

    # Displays the prompt to add tasks
    def add_task_prompt(self):
        if self.task_process != Process.ADD and not self.other_process:
            self.etr_frame.place(x=30, y=130)
            self.prompt.pack()
            self.etr_add_btn.pack(side=ctk.RIGHT)
            self.task_process = Process.ADD
            self.other_process = True

    def dict_count_add(self):
        self.count += 1

    def dict_count_minus(self):
        self.count -= 1

    # Adds the task the user enters into the prompt
    def add_task(self):
        task = self.prompt.get()
        task = task.lower()

        if task not in self.tdo_lst:
            self.dict_count_add()
            self.tdo_lst[self.count] = task

            self.labl.configure(text=str(self.tdo_lst)[1:-1])

            self.etr_frame.place_forget()
            self.etr_add_btn.pack_forget()
            self.prompt.pack_forget()
            self.prompt.delete(0, ctk.END)
            self.task_process = Process.BLANK
            self.other_process = False

    # Deletes the task the user prompts
    def delete_task_prompt(self):
        if self.task_process != Process.DEL and not self.other_process:
            self.etr_frame.place(x=30, y=130)
            self.prompt.pack()
            self.etr_del_btn.pack()
            self.task_process = Process.DEL
            self.other_process = True

    def delete_task(self):
        task_to_delete = None
        for task_num, task in self.tdo_lst.items():
            print(task_num, task)
            task_to_delete = self.prompt.get()
            if task == task_to_delete:
                task_to_delete = task_num
                break

        if task_to_delete is not None:
            self.dict_count_minus()
            del_tsk = self.tdo_lst.pop(task_to_delete)
            self.labl.configure(text=str(self.tdo_lst_del)[1:-1])
            self.timed_lbl.configure(text=del_tsk)
            self.show_message(del_tsk)

        self.etr_frame.place_forget()
        self.prompt.pack_forget()
        self.prompt.delete(0, ctk.END)
        self.etr_del_btn.pack_forget()
        self.task_process = Process.BLANK
        self.other_process = False

    def manage_task_prompt(self):
        if self.task_process != Process.MAN and not self.other_process:
            self.etr_frame.place(x=30, y=130)
            self.manage_prompt.pack()
            self.etr_man_btn.pack()
            self.task_process = Process.MAN
            self.other_process = True

    def manage_task(self):
        task = self.manage_prompt.get()
        task_to_manage = None
        task_tags = []
        for task_num, task in self.tdo_lst.items():
            if task_to_manage == task:
                pass

    def show_message(self, text):
        self.timed_lbl.configure(text="Task deleted: " + text)
        self.timed_lbl_frame.place(x=30, y=150)
        self.timed_lbl.pack()
        self.timed_lbl_frame.after(2000, self.timed_lbl_frame.place_forget)
        self.timed_lbl.selection_clear()

    def ui_change(self):
        pass


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Todo List")
    root.geometry("500x700")

    Todo(root)

    root.mainloop()
