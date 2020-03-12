#!/usr/bin/env python
# coding: utf-8

# In[7]:


from DW_Minor_Project import *
from tkinter import *
import SignUp


# In[8]:


def signup():
    win2 = Toplevel(win)
    SignUp.SignUp(win2)


# In[ ]:


#def validate_login():
    


if __name__ == "__main__" :
    win=Tk()
    win.configure(background="light blue")
    win.title("Welcome!")
    win.geometry("500x100")
    headlabel = Label(win, text = 'Welcome to Hotel Booking App',fg = 'black', bg = "orange") 
    headlabel.grid(row = 0, column = 1)
    loginlabel = Label(win, text = 'Login!',fg = 'black', bg = "orange")
    loginlabel.grid(row = 1, column = 1)
    UserId_entry = Entry(win)
    password_entry = Entry(win)
    UserId_entry.grid(row = 2, column = 1, ipadx ="100")
    password_entry.grid(row = 3, column = 1, ipadx ="100")
    Idlabel=Label(win, text = 'UserID',fg = 'black', bg = "orange")
    Passlabel=Label(win, text = 'Password',fg = 'black', bg = "orange")
    Idlabel.grid(row = 2, column = 0)
    Passlabel.grid(row = 3, column = 0)
    loginbutton = Button(win, text = "LOGIN", bg = "orange", fg = "black")
    signupbutton = Button(win, text = "SIGN UP", bg = "orange", fg = "black",command=signup)
    loginbutton.grid(row = 4, column = 0)
    signupbutton.grid(row = 4, column = 1)
    win.mainloop()

