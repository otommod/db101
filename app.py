import wx
import psycopg2


STATEMENT = """
SELECT Drug.name, BigPharma.name AS maker, Drug.formula, Sell.price FROM
  Drug
  JOIN BigPharma ON Drug.bigpharma_id = BigPharma.id
  JOIN Sell ON Drug.id = Sell.drug_id
WHERE Sell.pharmacy_id = %s;
"""

STATEMENT2 = """
SELECT Doctor.*, Patient.name FROM
  Doctor
  LEFT JOIN Patient ON Doctor.id = Patient.doctor_id;
"""

STATEMENT3 = """
SELECT Patient.name AS patient,
       Doctor.name AS doctor,
       Drug.name AS drug,
       date,
       dosage
FROM
  Prescription
  JOIN Patient ON Patient.id = Prescription.patient_id
  JOIN Doctor ON Doctor.id = Prescription.doctor_id
  JOIN Drug ON Drug.id = Prescription.drug_id
  JOIN Sell ON Sell.drug_id = Prescription.drug_id AND Sell.pharmacy_id = %s;
"""

AGGREGATE = """
SELECT COUNT(id) FROM Patient;
"""

GROUP_BY = """
SELECT COUNT(pharmacy_id)
FROM Sells
GROUP BY drug_id;
"""

ORDER_BY = """
SELECT *
FROM Contract
ORDER BY end_date;
"""

conn = psycopg2.connect("dbname=db101 user=otto")
cur = conn.cursor()



# Window classes
class MainWindow(wx.Frame):
    TITLE = "The Databaser 3000"
    SIZE = (380, 380)

    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent,
                                         title=MainWindow.TITLE,
                                         size=MainWindow.SIZE)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Input
        # input_vbox = wx.BoxSizer(wx.VERTICAL)
        # input_hbox = wx.BoxSizer(wx.HORIZONTAL)

        # input_header = wx.StaticText(panel, label='Insert number')
        # input_vbox.Add(input_header,
        #                flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        # self.input_box = FlashingTextCtrl(panel)
        # input_hbox.Add(self.input_box,
        #                flag=wx.RIGHT, border=10, proportion=1)

        # self.from_base_button = BaseSelectButton(panel)
        # input_hbox.Add(self.from_base_button)

        # input_vbox.Add(input_hbox,
        #                flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=80)
        # vbox.Add(input_vbox,
        #          flag=wx.EXPAND)


        line = wx.StaticLine(panel)
        vbox.Add(line,
                 flag=wx.EXPAND | wx.ALL, border=50)


        # Output
        # output_vbox = wx.BoxSizer(wx.VERTICAL)
        # output_hbox = wx.BoxSizer(wx.HORIZONTAL)

        # output_header = wx.StaticText(panel, label='Output')
        # output_vbox.Add(output_header,
        #                 flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)

        # self.output_box = wx.TextCtrl(panel)
        # self.output_box.SetEditable(False)
        # output_hbox.Add(self.output_box,
        #                 flag=wx.RIGHT, border=10, proportion=1)

        # self.to_base_button = BaseSelectButton(panel)
        # output_hbox.Add(self.to_base_button)

        # output_vbox.Add(output_hbox,
        #                 flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=80)
        # vbox.Add(output_vbox,
        #          flag=wx.EXPAND)


        # Buttons
        buttons_vbox = wx.BoxSizer(wx.VERTICAL)
        buttons_hbox = wx.BoxSizer(wx.HORIZONTAL)

        exit_button = wx.Button(panel, label='Exit')
        exit_button.Bind(wx.EVT_BUTTON, self.exit)
        buttons_hbox.Add(exit_button,
                         flag=wx.ALIGN_LEFT)

        buttons_hbox.AddStretchSpacer()

        # convert_button = wx.Button(panel, label='Convert')
        # convert_button.SetBackgroundColour('#4ebc06')
        # convert_button.Bind(wx.EVT_BUTTON, self.convert)
        # buttons_hbox.Add(convert_button,
        #                  flag=wx.ALIGN_RIGHT, proportion=1)

        # buttons_vbox.Add(buttons_hbox,
        #                  flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=80)
        # vbox.Add(buttons_vbox,
        #          flag=wx.EXPAND | wx.TOP, border=50)
        # panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    # exit_button callback
    def exit(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    main_win = MainWindow(None)

    app.MainLoop()
