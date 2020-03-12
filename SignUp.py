#!/usr/bin/env python
# coding: utf-8

# In[1]:


from DW_Minor_Project import *
from tkinter import *


# In[3]:


class SignUp:
    def __init__(self,win,build):
        self.b=build
        self.generate_signup(win)
    def update_signup(self):
        if (self.password_entry.get()==self.reconfirm_entry.get()):
            mycursor=self.b.pr.mydb.cursor()
            mycursor.execute("Select max(CustomerID) from Validation;")
            for i in mycursor:
                maxval=i[0]    
            if maxval == None:
                print("Empty list")
                val = 1
                email =self.UserId_entry.get()
                password = self.password_entry.get()
                mycursor.execute("Insert into Validation (CustomerID, Password, EmailID) Values ("+str(val)+",\'"+password+"\',\'"+email+"\');")
                mycursor.execute("Select * from Validation;")
                for i in mycursor:
                    print(i)
            else:
                print(maxval)
                val = maxval+1
                email =self.UserId_entry.get()
                password = self.password_entry.get()
                mycursor.execute("Insert into Validation (CustomerID, Password, EmailID) Values ("+str(val)+",\'"+password+"\',\'"+email+"\');")
                mycursor.execute("Select * from Validation;")
                for i in mycursor:
                    print(i)
            self.headlabel['text']="sign up successful"
            self.b.pr.mydb.commit()
        else:
            self.headlabel['text']="Passwords do not match"



    def generate_signup(self,win) :
        win.configure(background="light blue")
        win.title("Welcome!")
        win.geometry("500x110")
        self.headlabel = Label(win, text = 'Welcome to Hotel Booking App',fg = 'black', bg = "orange") 
        self.headlabel.grid(row = 0, column = 1)
        self.loginlabel = Label(win, text = 'Sign Up!',fg = 'black', bg = "orange")
        self.loginlabel.grid(row = 1, column = 1)
        self.UserId_entry = Entry(win,width=15)
        self.password_entry = Entry(win,show="*", width=15)
        self.reconfirm_entry = Entry(win, show="*", width=15)
        self.UserId_entry.grid(row = 2, column = 1, ipadx ="100")
        self.password_entry.grid(row = 3, column = 1, ipadx ="100")
        self.reconfirm_entry.grid(row = 4, column = 1, ipadx ="100")
        self.Idlabel=Label(win, text = 'EmailID',fg = 'black', bg = "orange")
        self.Passlabel=Label(win, text = 'Password',fg = 'black', bg = "orange")
        self.reconflabel=Label(win, text = 'Confirm Password',fg = 'black', bg = "orange")
        self.Idlabel.grid(row = 2, column = 0)
        self.Passlabel.grid(row = 3, column = 0)
        self.reconflabel.grid(row = 4, column = 0)
        self.signupbutton = Button(win, text = "SIGN UP", bg = "pink", fg = "dark blue",command = self.update_signup)
        self.signupbutton.grid(row = 5, column = 1)
        win.mainloop()

