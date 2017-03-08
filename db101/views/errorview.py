import tkinter as tk
from tkinter import ttk


class ErrorView:
    @classmethod
    def _setup_error_styles(cls):
        s = ttk.Style()
        s.configure("Error.TFrame", background="red")
        s.configure("Error.TLabel", background="red")

    def __init__(self, exception):
        self.msg = exception.msg
        self.window = tk.Toplevel()
        self.window.title("Error")

        self._setup_error_styles()

        frame = ttk.Frame(self.window, style="Error.TFrame")
        frame.grid(sticky="nsew")

        ttk.Label(frame,
                  text="Cannot change table because:",
                  style="Error.TLabel").grid(row=0, column=0)
        ttk.Label(frame,
                  text=self.msg,
                  style="Error.TLabel").grid(row=1, column=0)
        ttk.Button(frame,
                   text="OK",
                   command=self.window.destroy)
