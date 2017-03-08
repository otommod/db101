import tkinter as tk
from tkinter import ttk

import psycopg2

import db101

conn = psycopg2.connect(dbname="db101")
sql_mapper = db101.mapper.sql.SQLMapper(conn)
db101.models.NamedTable.mapper_factory = sql_mapper

pharmacy = db101.models.Pharmacy(1, sql_mapper)
patients = db101.models.NamedTable.lookup("patient")


root = tk.Tk()
root.title("BaseMasteRX 3000")
root.geometry("683x384")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# s = ttk.Style()
# s.configure("Main.TFrame", background="green")

# mainframe = ttk.Frame(root)
# mainframe.grid(row=0, column=0, sticky="nsew")
# mainframe.rowconfigure(0, weight=1)
# mainframe.columnconfigure(0, weight=1)
# mainframe.configure(style="Main.TFrame")

# table_view = db101.views.EditableTableView(mainframe, patients)
# search_view = db101.views.MultiSearchView(root, pharmacy)

# table_view.grid(in_=mainframe, row=0, column=0, sticky="nsew")
# search_view.grid(in_=mainframe, row=0, column=0, sticky="nsew")

view = db101.views.MainView(root, pharmacy)
view.grid(sticky="nsew")

root.mainloop()
