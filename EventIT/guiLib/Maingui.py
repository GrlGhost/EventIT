import tkinter as tk


from logAdmin import LogAdmin
from logSensor import LogSensor
from logUser import LogUser



class App(tk.Tk):
    def __init__(self, regDeUsuarios):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.Create_Widgets()
        self.regDeUsuarios = regDeUsuarios 
        


    def OpenWindow(self, NewWindow):
        if NewWindow == LogUser:
            LogUser(self.regDeUsuarios)
        elif NewWindow == LogAdmin:
            LogAdmin(self.regDeUsuarios)
        elif NewWindow == LogSensor:
            LogSensor()
        self.withdraw()


    
    def Create_Widgets(self):

        #Creacion de widgets
        self.name = tk.Label(self, text="EventIT")
        self.citizendLogBtn = tk.Button(self, text="Log as citizen", command = lambda: self.OpenWindow(LogUser))
        self.adminLogBtn = tk.Button(self, text="Log as admin", command = lambda: self.OpenWindow(LogAdmin))
        self.sensorLogBtn = tk.Button(self, text="sensor", command = lambda: self.OpenWindow(LogSensor))

        #Impresion de widgets
        centerW = 150

        self.name.grid(row=1, column= centerW)
        self.citizendLogBtn.grid(row= 2, column= centerW)
        self.adminLogBtn.grid(row= 3, column= centerW)
        self.sensorLogBtn.grid(row= 4,column= centerW)

    






