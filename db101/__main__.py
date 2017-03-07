import tkinter as tk
from tkinter import ttk

import psycopg2

import db101


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

conn = psycopg2.connect(dbname="db101")
table_mapper = db101.TableMapperFactory(conn)
table_m = db101.TableModel(table_mapper)
# table_v = db101.TableView(mainframe, model.Patient)
table_c = db101.TableController(table_m.Patient, mainframe)

search_mapper = db101.SearchMapperFactory(conn)
search_m = db101.SearchModel(search_mapper)

table_c.v.tree.grid(row=0, column=0, sticky="nsew",  padx=2, pady=2)
root.mainloop()
