#!/usr/bin/env python
# coding: utf-8

# In[1]:


from DW_Minor_Project import *
from tkinter import *


# In[3]:


class SignUp:
    def __init__(self,win):
        generate_signup(win)


# In[5]:


def update_signup():
    if (password_entry.get()==reconfirm_entry.get()):
        pr = project("DW_MINOR_PROJECT")
        mycursor=pr.mydb.cursor()
        mycursor.execute("Select max(CustomerID) from Validation;")
        for i in mycursor:
            if i[0] == None:
                print("Empty list")
                val = 1
                email =UserId_entry.get()
                password = password_entry.get()
                mycursor.execute("Insert into Validation (CustomerID, Password, EmailID) Values ("+str(val)+","+password+","+email+");")
            else:
                print(i[0])
                val = i[0]+1
                email =UserId_entry.get()
                password = password_entry.get()
                mycursor.execute("Insert into Validation (CustomerID, Password, EmailID) Values ("+str(val)+","+password+","+email+");")
        headlabel['text']="sign up successful"
    else:
        headlabel['text']="Passwords do not match"


# In[4]:


def generate_signup(win) :
    win.configure(background="light blue")
    win.title("Welcome!")
    win.geometry("500x110")
    headlabel = Label(win, text = 'Welcome to Hotel Booking App',fg = 'black', bg = "orange") 
    headlabel.grid(row = 0, column = 1)
    loginlabel = Label(win, text = 'Sign Up!',fg = 'black', bg = "orange")
    loginlabel.grid(row = 1, column = 1)
    UserId_entry = Entry(win,width=15)
    password_entry = Entry(win,show="*", width=15)
    reconfirm_entry = Entry(win, show="*", width=15)
    UserId_entry.grid(row = 2, column = 1, ipadx ="100")
    password_entry.grid(row = 3, column = 1, ipadx ="100")
    reconfirm_entry.grid(row = 4, column = 1, ipadx ="100")
    Idlabel=Label(win, text = 'EmailID',fg = 'black', bg = "orange")
    Passlabel=Label(win, text = 'Password',fg = 'black', bg = "orange")
    reconflabel=Label(win, text = 'Confirm Password',fg = 'black', bg = "orange")
    Idlabel.grid(row = 2, column = 0)
    Passlabel.grid(row = 3, column = 0)
    reconflabel.grid(row = 4, column = 0)
    signupbutton = Button(win, text = "SIGN UP", bg = "pink", fg = "dark blue",command = update_signup)
    signupbutton.grid(row = 5, column = 1)
    win.mainloop()

