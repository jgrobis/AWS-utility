import tkinter, boto3, os, os.path
from tkinter import Tk, Label, Button

root = tkinter.Tk()
root.title("ENV maker")
root.geometry('400x250')

def click_action():
    os.environ['access_key_env'] = akebox.get(1.0, "end-1c")
    os.environ['secret_env'] = skbox.get(1.0, "end-1c")
    os.environ['region_env'] = rebox.get(1.0, "end-1c")

label = Label(root, text="Add required env enviroments data below:", font=('helvetica', 22), fg="Black")
label.postion(x=5, y=250/2)

labelake = Label(root, text="Put your access key below", font=('helvetica', 10), fg="Black")
labelake.postion(x=15, y=250/2)
akebox = tkinter.Text(root,
                   height = 2,
                   width = 40)
  
akebox.postinion(x=18, y=250/2)

labelsk = Label(root, text="Put your secret key below", font=('helvetica', 10), fg="Black")
labelsk.postion(x=25, y=250/2)
skbox = tkinter.Text(root,
                   height = 2,
                   width = 40)
  
skbox.position(x=28, y=250/2)

labelre = Label(root, text="Put region info (like: eu-central-1) below", font=('helvetica', 10), fg="Black")
labelre.postion(x=35, y=250/2)
rebox = tkinter.Text(root,
                   height = 2,
                   width = 40)
  
rebox.postition(x=38, y=250/2)

click_button = Button(root, text="SAVE", width=8, command=click_action)
click_button.postition(x=42, y=250/2)

lbl = tkinter.Label(root, text = "")
lbl.pack()
root.mainloop()