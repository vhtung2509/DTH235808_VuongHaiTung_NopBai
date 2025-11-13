# màn hình đăng nhập

import tkinter as tk
from tkinter import *

root=Tk()
root.title("Enter New Password")
root.minsize(height=150,width=250)
root.resizable(height=True,width=True)

Label(root,text="Old Password:").grid(row=0,column=0)
Entry(root,width=30).grid(row=0,column=1)
Label(root,text="New Password:").grid(row=1,column=0)
Entry(root,width=30).grid(row=1,column=1)
Label(root,text="Enter New Password Again:").grid(row=2,column=0)
Entry(root,width=30).grid(row=2,column=1)

Button(root,text="OK").grid(row=3,column=0)
Button(root,text="Cancel").grid(row=3,column=1)
root.mainloop()
