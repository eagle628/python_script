#!python3.6
import tkinter as tk
import test_py
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="right")

    def say_hi(self):
        print("hi there, everyone!")
        y = test_py.generate_plant_response()

root = tk.Tk()
root.title("Test_GUI")
root.geometry("300x300")
root.title("Status bar")
status = tk.Label(root, text="Now processing..",
                           borderwidth=2, relief="groove")
status.pack(side=tk.BOTTOM, fill=tk.X)
app = Application(master=root)
app.mainloop()
