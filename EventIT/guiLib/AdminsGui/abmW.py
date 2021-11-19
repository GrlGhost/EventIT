import tkinter as tk
from tkinter import messagebox

from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UserManagementLib.CreateProfileClass import CreateProfile

class AbmW(tk.Tk):
    def __init__(self, reg_de_usuarios: RegDeUsuarios, user: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"450x400+{550}+{150}")
        self.wm_resizable(1, 1)
        self.regdeusuarios = reg_de_usuarios
        self.user = user
        self.Create_Widgets()

    def Create_Widgets(self):
        #Creacion de widgets
        self.keynameentry = tk.Entry(self)
        self.nameentry = tk.Entry(self)
        self.phoneentry = tk.Entry(self)
        self.cuilentry = tk.Entry(self)

        self.phone_btn = tk.Button(self, text= "chanege phone", command= lambda: self.modify_profile("phone"))
        self.cuil_btn = tk.Button(self, text= "change cuil", command= lambda: self.modify_profile("cuil"))
        self.name_btn = tk.Button(self, text= "change ame", command= lambda: self.modify_profile("name"))

        self.daralta_btn = tk.Button(self, text= "register user", command= self.register)
        self.darbaja_btn = tk.Button(self, text= "unsubscribe", command= self.dardebaja)

        self.text = tk.Label(self, text= "register use all parameters\nunsubscribe only keyname")




        #Impresion de widgets
        self.keynameentry.insert(0, "keyname user")
        self.keynameentry.grid(row= 0, column=0)
        self.nameentry.insert(0, "new name")
        self.nameentry.grid(row= 1, column= 0)
        self.phoneentry.insert(0, "new phone")
        self.phoneentry.grid(row= 1, column= 1)
        self.cuilentry.insert(0, "new cuil")
        self.cuilentry.grid(row= 1, column= 2)

        self.phone_btn.grid(row= 2, column= 1)
        self.cuil_btn.grid(row= 2, column= 2)
        self.name_btn.grid(row = 2, column= 0)

        self.daralta_btn.grid(row= 3, column= 0)
        self.darbaja_btn.grid(row= 3, column= 1)

        self.text.grid(row= 4, column= 0)


    def modify_profile(self, parameter):
        if parameter == "phone":
            pass


    def register(self):
        key_name = self.keynameentry.get()
        phone = self.phoneentry.get()
        cuil = self.cuilentry.get()
        if (self.regdeusuarios.searchCitizen(int(phone)) != None) or (self.regdeusuarios.searchCitizen(cuil= int(cuil)) != None):
            messagebox.showwarning(title= "Existing account", message= "An acount with this data already exist")
        else:
            if CreateProfile.Create_Profile("user", key_name, phone, cuil, self.regdeusuarios, self.dataanses):
                self.user = self.regdeusuarios.Get_Ciudadanos()[key_name][0]

    def dardebaja(self):
        key_name = self.keynameentry.get()
        self.regdeusuarios.Manage_Ciudadanos(None, False, key_name)







