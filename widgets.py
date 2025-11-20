import tkinter as tk

class Label:
    def __init__(self, text):
        self.text = text

    def render(self, parent):
        lbl = tk.Label(parent, text=self.text)
        lbl.pack(pady=5)

class Button:
    def __init__(self, text, on_click=None):
        self.text = text
        self.on_click = on_click

    def render(self, parent):
        btn = tk.Button(parent, text=self.text, command=self.on_click)
        btn.pack(pady=5)

class TextBox:
    def __init__(self, width=20):
        self.width = width
        self.entry = None

    def render(self, parent):
        self.entry = tk.Entry(parent, width=self.width)
        self.entry.pack(pady=5)

    def get_text(self):
        return self.entry.get()

class Dropdown:
    def __init__(self, options):
        self.options = options
        self.var = None

    def render(self, parent):
        self.var = tk.StringVar(parent)
        self.var.set(self.options[0])
        dropdown = tk.OptionMenu(parent, self.var, *self.options)
        dropdown.pack(pady=5)

    def get_selected(self):
        return self.var.get()