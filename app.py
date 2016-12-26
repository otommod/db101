import wx


STATEMENT1 = """
SELECT Drug.name,Sell.price,Drug.formula FROM
  Sell
  JOIN Drug ON Sell.pharmacy_id=Drug.id;"""

STATEMENT2 = """
SELECT Doctor.*, Patient.name FROM
  Doctor
  LEFT JOIN Patient ON Doctor.id=Patient.id;"""
