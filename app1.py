from tkinter import *

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("MalaGUIes vol 2")

        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        find = Menu(menu)
        find.add_command(label='Oldest People Drugs', command=self.client_exit)
        find.add_command(label='Drugs Capacity', command=self.client_exit)
        find.add_command(label='Last telephone calls', command=self.client_exit)
        find.add_command(label='Our Drug Companies', command=self.client_exit)
        find.add_command(label='Other Drug Companies', command=self.client_exit)
        find.add_command(label='New Drugs From Partners', command=self.client_exit)
        find.add_command(label='New Drugs From Other Companies', command=self.client_exit)
        find.add_command(label='Drugs For A Patient', command=self.client_exit)
        find.add_command(label='Number Of Contracts Order By Start Date', command=self.client_exit)
        find.add_command(label='Number Of Contracts Order By End Date', command=self.client_exit)
        find.add_command(label='Doctors With Average Patients Over 50', command=self.client_exit)
        find.add_command(label='Number Of Contracts Order By Start Date', command=self.client_exit)
        menu.add_cascade(label='Find', menu=find)


        smart_find = Menu(menu)
        smart_find.add_command(label='Ta sun8eta queries edw kai na mas petaei apo katw ape8eias ta tab tous mazi me tous pinakes')
        smart_find.add_command(label='Doctor', command=self.client_exit)
        smart_find.add_command(label='Patient', command=self.client_exit)
        smart_find.add_command(label='Drug', command=self.client_exit)
        smart_find.add_command(label='BigPharma', command=self.client_exit)
        smart_find.add_command(label='Prescription', command=self.client_exit)
        menu.add_cascade(label='Smart Find', menu=smart_find)

        table = Menu(menu)
        table.add_command(label='Instert', command=self.client_exit)
        table.add_command(label='Delete', command=self.client_exit)
        table.add_command(label='Update', command=self.client_exit)
        menu.add_cascade(label='Table', menu=table)

        exit = Menu(menu)
        exit.add_command(label='Are you sure you want to exit?', command=self.client_exit)
        menu.add_cascade(label='Exit', menu=exit)
    
    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
