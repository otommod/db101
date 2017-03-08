from tkinter import ttk


class Spinbox(ttk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, "ttk::spinbox", **kw)

    def current(self, newindex=None):
        return self.tk.call(self._w, "current", newindex)

    def set(self, value):
        return self.tk.call(self._w, "set", value)
