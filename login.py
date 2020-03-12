#!/usr/bin/env python
# coding: utf-8

# In[7]:


from DW_Minor_Project import *
from tkinter import *
import SignUp


# In[8]:
class login:
    def __init__(self):
        self.build=build()
        self.generate_login()

    def signup(self):
        win2 = Toplevel(self.win)
        SignUp.SignUp(win2,self.build)

    def validate_login(self):
        Id=self.UserId_entry.get()
        password=self.password_entry.get()
        mycursor=self.build.pr.mydb.cursor()
        mycursor.execute("Select Password from Validation where CustomerID = "+Id+";")
        for i in mycursor:
            real_password=i[0]
        if password == real_password:
            print("It works!!")
            self.headlabel['text']="Welcome!"
            #call homepage here
        else:
            self.headlabel['text']="Wrong credentials!"

    def generate_login(self) :
        self.win=Tk()
        self.win.configure(background="light blue")
        self.win.title("Welcome!")
        self.win.geometry("500x100")
        self.headlabel = Label(self.win, text = 'Welcome to Hotel Booking App',fg = 'black', bg = "orange") 
        self.headlabel.grid(row = 0, column = 1)
        self.loginlabel = Label(self.win, text = 'Login!',fg = 'black', bg = "orange")
        self.loginlabel.grid(row = 1, column = 1)
        self.UserId_entry = Entry(self.win)
        self.password_entry = Entry(self.win,show="*")
        self.UserId_entry.grid(row = 2, column = 1, ipadx ="100")
        self.password_entry.grid(row = 3, column = 1, ipadx ="100")
        self.Idlabel=Label(self.win, text = 'UserID',fg = 'black', bg = "orange")
        self.Passlabel=Label(self.win, text = 'Password',fg = 'black', bg = "orange")
        self.Idlabel.grid(row = 2, column = 0)
        self.Passlabel.grid(row = 3, column = 0)
        self.loginbutton = Button(self.win, text = "LOGIN", bg = "orange", fg = "black",command=self.validate_login)
        self.signupbutton = Button(self.win, text = "SIGN UP", bg = "orange", fg = "black",command=self.signup)
        self.loginbutton.grid(row = 4, column = 0)
        self.signupbutton.grid(row = 4, column = 1)
        self.win.mainloop()