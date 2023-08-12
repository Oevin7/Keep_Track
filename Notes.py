import tkinter
import customtkinter as ctk


class Notes:

    def __init__(self, window):
        self.window = window

        self.saved_note = None

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.font = "Alice Yotsuba Inc."

        self.notes_window = ctk.CTkToplevel(self.window)

        self.labels = {}
        self.label_count = 0

        self.main_frame = ctk.CTkFrame(self.window, height=700, width=500)

        self.btn_frame = ctk.CTkFrame(self.main_frame)

        self.add_btn = ctk.CTkButton(self.btn_frame, text="Add Note", font=(self.font, 14), command=self.add_prompt)
        self.add_btn.grid(row=0, column=0)
        self.add_btn.pack()

        self.note_container = ctk.CTkFrame(self.main_frame)

        self.btn_frame.pack(pady=10)

        self.note_frame = ctk.CTkFrame(self.main_frame)
        self.note_box = ctk.CTkTextbox(self.note_frame)

        self.note_add = ctk.CTkButton(self.note_frame, text="Add", font=(self.font, 10), command=self.add_note)

        self.note_box.pack()
        self.note_add.pack()

        # self.note_frame.place(x=150)
        # self.note_box.place(x=0)

        self.main_frame.pack()
        self.main_frame.pack()

    def count_up(self):
        self.label_count += 1

    def count_down(self):
        self.label_count -= 1

    def add_prompt(self):
        self.note_frame.pack()

    def label_clicked(self, event):
        self.notes_window.title("Edit Notes")

        notes_text = tkinter.Text(self.notes_window)
        notes_text.pack()

        save_button = ctk.CTkButton(self.notes_window, text="Save",
                                    command=lambda: self.add_note(notes_text.get("1.0", "end-1c")))
        save_button.pack()

        cancel_button = tkinter.Button(self.notes_window, text="Cancel", command=self.notes_window.destroy)
        cancel_button.pack()

    def add_note(self, new_note=None):
        self.note_frame.pack_forget()

        self.count_up()
        if new_note is None:
            new_note = self.note_box.get("1.0", ctk.END)
        self.saved_note = new_note
        new_label = ctk.CTkLabel(self.window, text=new_note)
        new_label.bind("<Button-1>", self.label_clicked)
        new_label.pack()
        self.labels[self.label_count] = new_label

        if hasattr(self, 'notes_window') and isinstance(self.notes_window, ctk.CTkToplevel):
            self.notes_window.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Notes")
    root.geometry("500x700")

    Notes(root)

    root.mainloop()
