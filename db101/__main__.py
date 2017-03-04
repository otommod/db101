import db101
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Databaser 3000")

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky="nsew")
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)
# mainframe.columnconfigure(0, weight=1)

# app = db101.Controller(root)
etv = db101.EditableTreeview(mainframe, ("foo", "bar"))
etv.grid(row=0, column=0, sticky="nsew")

etv.add_items((i, "item_%d" % i) for i in range(1, 100))
etv.add_item((100, "this is a pretty long text that should stretch the tree"))

root.mainloop()
