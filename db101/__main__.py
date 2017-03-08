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
table_mapper = db101.mapper.sql.TableMapperFactory(conn)
query_mapper = db101.mapper.sql.QueryMapper(conn)

# table_m = db101.TableModel(table_mapper)
# table_v = db101.EditableTableView(mainframe, table_m.Patient)
# table_c = db101.TableController(table_m.Patient, table_v)

search_m = db101.models.General(query_mapper)
search_v = db101.views.SearchView(root)
search_c = db101.controller.SearchController(1, search_m, search_v)

pharmacy = db101.models.Pharmacy(1, query_mapper)
app_view = db101.views.AppView(root)
app = db101.controller.AppController(app_view, pharmacy)
app_view.grid(row=1, column=0)

search_v.grid(row=0, column=0)
# table_c.v.tree.grid(row=0, column=0, sticky="nsew",  padx=2, pady=2)
root.mainloop()
