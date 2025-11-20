import tkinter as tk

class App:
    def __init__(self, title="Kigo App", size=(500, 400)):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{size[0]}x{size[1]}")

    def add(self, widget):
        widget.render(self.root)

    def run(self):
        self.root.mainloop()