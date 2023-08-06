import customtkinter as ctk
from Dependencies import Click_Handling as Ch
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
        ctk.set_appearance_mode("dark-blue")

        self.main_frame = ctk.CTkFrame(self.window, height=500, width=650)
        self.main_frame["relief"] = "sunken"

        # Booleans to control UI
        self.task_process = Process.BLANK
        self.other_process = False

        # The list the label displays
        self.tdo_lst = {}
        self.tdo_lst_del = {}
        self.count = 0

        # Frame for the entries and buttons
        self.etr_frm = ctk.CTkFrame(self.main_frame)

        # Entry button to add task
        self.etr_add_btn = ctk.CTkButton(self.etr_frm, text="Add", width=10, height=28, command=self.add_task)
        # enter_clicked = Ch.enter_click(etr=self.etr_add_btn, )

        # Entry button to delete task
        self.etr_del_btn = ctk.CTkButton(self.etr_frm, text="Delete", width=10, height=28,
                                         command=self.delete_task)

        self.etr_man_btn = ctk.CTkButton(self.etr_frm, text="Manage", width=10, height=28)

        # The entry itself
        self.add_prompt = Ch.CstEntry(master=self.etr_frm)

        # Delete Prompt for deleting tasks
        self.delete_prompt = Ch.CstEntry(master=self.etr_frm)

        self.manage_prompt = Ch.CstEntry(master=self.etr_frm)

        # The label that displays the tasks

        self.lbl_frame = ctk.CTkFrame(self.main_frame, border_width=2, width=100, height=200)
        self.lbl_frame["relief"] = "sunken"
        self.lbl_frame.pack(side=ctk.RIGHT)

        self.labl_title = ctk.CTkLabel(self.lbl_frame, text="Uncompleted Tasks", font=("Sunny Spells Basic", 50))
        self.labl_title.pack()

        self.timed_lbl_frame = ctk.CTkFrame(self.main_frame)
        self.timed_lbl = ctk.CTkLabel(self.timed_lbl_frame, font=("Sunny Spells Basic", 18))

        self.labl = ctk.CTkLabel(self.lbl_frame, text="", font=("Sunny Spells Basic", 20))
        self.labl.pack()

        # button frame and buttons
        self.btnfrm = ctk.CTkFrame(self.main_frame, height= 100, width=100)

        self.btn_add = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Add Task",
                                     font=("Sunny Spells Basic", 25),
                                     command=self.add_task_prompt)
        self.btn_add.pack(pady=2)

        self.btn_del = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Delete Task",
                                     font=("Sunny Spells Basic", 25),
                                     command=self.delete_task_prompt)
        self.btn_del.pack(pady=2)

        self.btn_manage = ctk.CTkButton(self.btnfrm, height=35, width=150, text="Manage Tasks",
                                        font=("Sunny Spells Basic", 25), command=self.manage_task_prompt)
        self.btn_manage.pack(pady=2)

        self.btnfrm.pack(padx=5, pady=10)

        self.main_frame.pack()

        # self.ui_settings.pack(side=ctk.BOTTOM)

    # Displays the prompt to add tasks
    def add_task_prompt(self):
        if self.task_process != Process.ADD and not self.other_process:
            self.etr_frm.pack()
            self.add_prompt.pack()
            self.etr_add_btn.pack()
            self.add_prompt.enter_bind(self.add_task)
            self.task_process = Process.ADD
            self.other_process = True

    def dict_count_add(self):
        self.count += 1

    def dict_count_minus(self):
        self.count -= 1

    # Adds the task the user enters into the prompt
    def add_task(self):
        task = self.add_prompt.get()
        task = task.lower()

        if task not in self.tdo_lst:
            self.dict_count_add()
            self.tdo_lst[self.count] = task

            self.labl.configure(text=str(self.tdo_lst)[1:-1])

            self.etr_frm.pack_forget()
            self.etr_add_btn.pack_forget()
            self.add_prompt.pack_forget()
            self.add_prompt.delete(0, ctk.END)
            self.task_process = Process.BLANK
            self.other_process = False

    # Deletes the task the user prompts
    def delete_task_prompt(self):
        if self.task_process != Process.DEL and not self.other_process:
            self.etr_frm.pack()
            self.delete_prompt.pack()
            self.etr_del_btn.pack()
            self.task_process = Process.DEL
            self.other_process = True

    def delete_task(self):
        task_to_delete = None
        for task_num, task in self.tdo_lst.items():
            if task in self.tdo_lst.values():
                task_to_delete = task_num
                break

        if task_to_delete is not None:
            self.dict_count_minus()
            del_tsk = self.tdo_lst.pop(task_to_delete)
            self.labl.configure(text=str(self.tdo_lst_del)[1:-1])
            self.timed_lbl.configure(text=del_tsk)
            self.show_message(del_tsk)

        self.etr_frm.pack_forget()
        self.delete_prompt.pack_forget()
        self.delete_prompt.delete(0, ctk.END)
        self.etr_del_btn.pack_forget()
        self.task_process = Process.BLANK
        self.other_process = False

    def manage_task_prompt(self):
        if self.task_process != Process.MAN and not self.other_process:
            self.etr_frm.pack()
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
        self.timed_lbl_frame.pack(side=ctk.BOTTOM)
        self.timed_lbl.pack()
        self.timed_lbl_frame.after(2000, self.timed_lbl_frame.destroy)

    def ui_change(self):
        pass


if __name__ == "__main__":
    window = ctk.CTk()
    window.title("Todo List")

    width = 650
    height = 550

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    Todo(window)

    window.mainloop()
