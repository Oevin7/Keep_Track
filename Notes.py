import tkinter
import customtkinter as ctk
import Todo_List
import Calender


# import ttkthemes


class Notes:

    def __init__(self, window):
        self.window = window

        self.saved_note = None

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.font = "Alice Yotsuba Inc."

        self.notes_window = None

        self.label_key = None

        self.opened_note_text = None

        self.labels = {}
        self.label_count = 0

        self.new_label = None
        self.edited_label = None

        self.main_frame = ctk.CTkFrame(self.window, height=700, width=500)

        self.menu_frame = ctk.CTkFrame(self.window, height=40, width=180)
        self.menu_frame.pack_propagate(False)

        self.todo_btn = ctk.CTkButton(self.menu_frame, text="Todo List", font=(self.font, 14), height=20, width=50, command=self.todo)
        self.calendar_btn = ctk.CTkButton(self.menu_frame, text="Calendar", font=(self.font, 14), height=20, width=50, command=self.calendar)

        self.menu_frame.pack()
        self.todo_btn.pack(side=ctk.LEFT)
        self.calendar_btn.pack(side=ctk.RIGHT)

        self.btn_frame = ctk.CTkFrame(self.main_frame)

        self.add_btn = ctk.CTkButton(self.btn_frame, text="Add Note", font=(self.font, 14), command=self.add_prompt)
        self.add_btn.grid(row=0, column=0)
        self.add_btn.pack()

        self.note_container_frame = ctk.CTkFrame(self.main_frame)

        self.btn_frame.pack(pady=10)

        self.note_frame = ctk.CTkFrame(self.main_frame)
        self.note_box = ctk.CTkTextbox(self.note_frame, height=100, width=200)

        self.note_add = ctk.CTkButton(self.note_frame, text="Add", font=(self.font, 10), command=self.add_note)

        self.note_box.pack()
        self.note_add.pack()

        # self.note_frame.place(x=150)
        # self.note_box.place(x=0)
        self.note_container_frame.pack(side=ctk.BOTTOM)
        self.main_frame.pack()

    def count_up(self):
        self.label_count += 1

    def count_down(self):
        self.label_count -= 1

    def add_prompt(self):
        self.note_frame.pack(side=ctk.TOP)

    def label_clicked(self, event):
        clicked_label = event.widget.master
        clicked_key = None

        for key, label in self.labels.items():
            if label == clicked_label:
                clicked_key = key
                break

        if clicked_key is not None:
            self.edited_label = self.labels[clicked_key]  # Store the clicked label
            self.opened_note_text = self.labels[clicked_key]

            # Open the notes window and update label text
            self.open_notes_window()

    def open_notes_window(self):
        self.notes_window = ctk.CTkToplevel(self.window)
        self.notes_window.title("Edit Notes")

        notes_text = tkinter.Text(self.notes_window)
        note_content = self.opened_note_text.cget("text")
        notes_text.pack()
        notes_text.insert("1.0", note_content)

        save_button = ctk.CTkButton(self.notes_window, text="Save",
                                    command=lambda: self.update_label_text(notes_text.get("1.0", "end-1c")))
        save_button.pack()

        cancel_button = tkinter.Button(self.notes_window, text="Cancel", command=self.notes_window.destroy)
        cancel_button.pack()

    def update_label_text(self, new_text):
        self.edited_label.configure(text=new_text)
        self.notes_window.destroy()

    def add_note(self, new_note=None):
        self.note_frame.pack_forget()

        self.count_up()
        if new_note is None:
            new_note = self.note_box.get("1.0", ctk.END)
            self.saved_note = new_note
            self.new_label = ctk.CTkLabel(self.note_container_frame, text=new_note)
            self.new_label.bind("<Button-1>", self.label_clicked)
            self.new_label.pack()
            self.labels[self.label_count] = self.new_label

        if hasattr(self, 'notes_window') and isinstance(self.notes_window, ctk.CTkToplevel):
            self.notes_window.destroy()

        self.note_box.delete("1.0", ctk.END)
        self.label_update()

    def label_update(self):
        for label_key, label_widget in self.labels.items():
            label_widget.configure(font=(self.font, 12), padx=10, pady=10, wraplength=200, justify=ctk.LEFT)

    def todo(self):
        self.main_frame.pack_forget()
        Todo_List.Todo(self.window)
        self.menu_frame.pack_forget()

    def calendar(self):
        self.main_frame.pack_forget()
        Calender.Calender(self.window)
        self.menu_frame.pack_forget()


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Notes")
    root.geometry("500x700")

    Notes(root)

    root.mainloop()
