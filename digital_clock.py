import tkinter as tk
import time
from tkinter.font import BOLD

main = tk.Tk()
main.geometry("300x200")
main.config(bg="#F4F9C3")
main.title("Digital Clock")

def timing():
    time_format = time.strftime("%H:%M:%S")
    time_label.config(text=time_format)
    time_label.after(1000, timing)

time_label = tk.Label(bg="#F9C3C3", font=("Ink Free",45, BOLD), fg="#F4F9C3")
time_label.place(x=25,y=45, width=260, height=100)
timing()

main.mainloop()