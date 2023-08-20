import customtkinter as ctk
import datetime as dt
import calendar
import Notes
import Todo_List


class Calender:

    def __init__(self, window):
        self.window = window

        self.calendar_edit_window = None

        self.current_date = dt.datetime.today()

        self.current_month = self.current_date.month
        self.current_year = self.current_date.year

        self.month = self.current_month
        self.year = self.current_year
        self.day_numbers = None

        self.month_name = calendar.month_name[self.current_month]

        self.number_of_days = calendar.monthrange(self.year, self.month)[1]

        self.day_frames = []

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.font = "Alice Yotsuba Inc."

        self.main_frame = ctk.CTkFrame(self.window)

        self.menu_frame = ctk.CTkFrame(self.window, height=40, width=150)
        self.menu_frame.pack_propagate(False)

        self.todo_btn = ctk.CTkButton(self.menu_frame, text="Todo List", font=(self.font, 14), height=20, width=50,
                                      command=self.todo)
        self.notes_btn = ctk.CTkButton(self.menu_frame, text="Notes", font=(self.font, 14), height=20, width=50, command=self.notes)

        self.menu_frame.pack()
        self.todo_btn.pack(side=ctk.LEFT)
        self.notes_btn.pack(side=ctk.RIGHT)

        self.time_label = ctk.CTkLabel(self.main_frame, padx=2, pady=2, font=(self.font, 14))
        self.month_display = ctk.CTkLabel(self.main_frame, text=self.month_name, font=(self.font, 18))

        self.update_time()
        self.month_display.pack()
        self.time_label.pack()

        self.calender_frame = ctk.CTkFrame(self.main_frame)
        self.calender_frame.pack()

        self.month_tracker(self.number_of_days)

        self.main_frame.pack()

    def frame_clicked(self, event):
        clicked_frame = event.widget.master
        clicked_index = None

        for frames in self.day_frames:

            if frames == clicked_frame:
                print("We clicked this frame")
                clicked_index = self.day_frames.index(frames)
                print(self.day_frames[clicked_index])
                self.open_calendar_window()

    def open_calendar_window(self):
        self.calendar_edit_window = ctk.CTkToplevel(self.window)
        self.calendar_edit_window.title("Edit Calendar Day")

    def month_tracker(self, days):
        num_of_days = 0
        row = 0
        col = 0
        while num_of_days != days:
            num_of_days += 1
            day_frame = ctk.CTkFrame(self.calender_frame)
            self.day_frames.append(day_frame)
            for frames in self.day_frames:
                frames.configure(height=100, width=150)
                frames.pack_propagate(False)
                frames.grid(row=row, column=col, padx=3, pady=3)
                col += 1
                if col > 4:
                    col = 0
                    row += 1
                self.day_numbers = ctk.CTkLabel(frames, text=str(num_of_days))
            self.day_numbers.place(anchor=ctk.NW, x=5)
        for day_frame in self.day_frames:
            day_frame.bind("<Button-1>", self.frame_clicked)

    def update_time(self):
        current_time = dt.datetime.now().strftime("%I:%M:%S %p")
        self.time_label.configure(text=current_time)
        self.window.after(1000, self.update_time)  # Update every 1000ms (1 second)

    def todo(self):
        self.main_frame.pack_forget()
        Todo_List.Todo(self.window)
        self.menu_frame.pack_forget()

    def notes(self):
        self.main_frame.pack_forget()
        Notes.Notes(self.window)
        self.menu_frame.pack_forget()


if __name__ == "__main__":
    root = ctk.CTk()
    Calender(root)
    root.title("Calendar")

    root.mainloop()
