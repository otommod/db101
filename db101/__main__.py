import tkinter as tk
from tkinter import ttk

import psycopg2

import db101

conn = psycopg2.connect(dbname="db101")
model = db101.SQLModel(conn)

root = tk.Tk()
root.title("Databaser 3000")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky="nsew")
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

s = ttk.Style()
s.configure("Main.TFrame", background="green")
mainframe.configure(style="Main.TFrame")

view = db101.TableView(mainframe, model.tables["patient"])
view.tree.grid(row=0, column=0, sticky="nsew",  padx=2, pady=2)

root.mainloop()
