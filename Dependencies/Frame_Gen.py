import customtkinter as ctk

def frame_gen(window, row_amt= 0, column_amt= 0, amount= 0):
    while row_amt and column_amt < amount:
        row_amt += 1
        column_amt += 1

    btn_frame = ctk.CTkFrame(window)
    return btn_frame