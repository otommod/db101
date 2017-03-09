import tkinter as tk
from tkinter import ttk

import psycopg2

import db101
from db101.schema import QUERIES

conn = psycopg2.connect(dbname="db101")
sql_mapper = db101.mapper.sql.SQLMapper(conn)
db101.models.NamedTable.mapper_factory = sql_mapper

General = sql_mapper.create_model("General", QUERIES["general"])
Pharmacy = sql_mapper.create_model("Pharmacy", QUERIES["pharmacy"])

general = General(sql_mapper)
pharmacy = Pharmacy(sql_mapper, {"our_pharmacy": 1})
patients = db101.models.NamedTable.lookup("patient")


root = tk.Tk()
root.title("BaseMasteRX 3000")
root.geometry("683x384")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

view = db101.views.MainView(root, general, pharmacy)
view.grid(sticky="nsew")

root.mainloop()
