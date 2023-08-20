import customtkinter as ctk
import datetime as dt
import calendar


class Calender:

    def __init__(self, window):
        self.window = window

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

        self.time_label = ctk.CTkLabel(self.main_frame, padx=2, pady=2, font=(self.font, 14))
        self.month_display = ctk.CTkLabel(self.main_frame, text=self.month_name, font=(self.font, 18))

        self.update_time()
        self.month_display.pack()
        self.time_label.pack()

        self.calender_frame = ctk.CTkFrame(self.main_frame)
        self.calender_frame.pack()

        self.month_tracker(self.number_of_days)

        self.main_frame.pack()

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
            self.day_numbers.place(anchor=ctk.NW)

    def update_time(self):
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.window.after(1000, self.update_time)  # Update every 1000ms (1 second)


if __name__ == "__main__":
    root = ctk.CTk()
    Calender(root)
    root.title("Calendar")

    root.mainloop()
