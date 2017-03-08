import tkinter as tk
from tkinter import ttk

import psycopg2

import db101

conn = psycopg2.connect(dbname="db101")
sql_mapper = db101.mapper.sql.SQLMapper(conn)
db101.models.NamedTable.mapper_factory = sql_mapper

pharmacy = db101.models.Pharmacy(1, sql_mapper)
patients = db101.models.NamedTable.loopup("patient")

main_controller = db101.controller.MainController(pharmacy)

# root = tk.Tk()
# root.title("Databaser 3000")
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# mainframe = ttk.Frame(root)
# mainframe.grid(row=0, column=0, sticky="nsew")
# mainframe.rowconfigure(0, weight=1)
# mainframe.columnconfigure(0, weight=1)

# s = ttk.Style()
# s.configure("Main.TFrame", background="green")
# mainframe.configure(style="Main.TFrame")

# table_view = db101.views.EditableTableView(mainframe, patients)
# table = db101.controller.TableController(table_m, table_view)

# search_view = db101.views.SearchView(root)
# search = db101.controller.SearchController(pharmacy, search_view)

# app_view = db101.views.AppView(root)
# app = db101.controller.AppController(app_view, pharmacy)

# app_view.grid(row=0, column=0)
# search_view.grid(row=1, column=0)
# table_view.grid(row=2, column=0, sticky="nsew")
# root.mainloop()
