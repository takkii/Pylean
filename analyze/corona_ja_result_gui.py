import os
import threading
import tkinter as tk

class CoronaJaResult(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        cwd = os.path.expanduser("~")
        root = tk.Tk()
        root.title("Coronavirus Tracker")
        root.geometry("1466x499")
        corosuke = tk.PhotoImage(file=cwd + "/GitHub/Pylean/analyze/image/corona_effect.gif")
        canvas = tk.Canvas(bg="black", width=1466, height=499)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, image=corosuke, anchor=tk.NW)
        root.mainloop()

thread = CoronaJaResult()
thread.run()
