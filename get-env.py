import tkinter, boto3, os, os.path
from tkinter import Tk, Label, Button

genv  = tkinter.Tk()
genv.title("ENV maker")
genv.geometry('600x350')

def click_action():
    os.environ['access_key_env'] = akebox.get(1.0, "end-1c")
    os.environ['secret_env'] = skbox.get(1.0, "end-1c")
    os.environ['region_env'] = rebox.get(1.0, "end-1c")

label = Label(genv, text="Add required env information data:", font=('helvetica', 22), fg="Black")
label.place(y=12, x=300, anchor="center")

labelake = Label(genv, text="Put your access key below", font=('helvetica', 10), fg="Black")
labelake.place(y=60, x=300, anchor="center")
akebox = tkinter.Text(genv,
                   height = 2,
                   width = 40)
akebox.place(y=90, x=300, anchor="center")

labelsk = Label(genv, text="Put your secret key below", font=('helvetica', 10), fg="Black")
labelsk.place(y=150, x=300, anchor="center")
skbox = tkinter.Text(genv,
                   height = 2,
                   width = 40)
skbox.place(y=180, x=300, anchor="center")

labelre = Label(genv, text="Put region info (like: eu-central-1) below", font=('helvetica', 10), fg="Black")
labelre.place(y=240, x=300, anchor="center")
rebox = tkinter.Text(genv,
                   height = 2,
                   width = 40)
rebox.place(y=270, x=300, anchor="center")

click_button = Button(genv, text="SAVE", width=8, command=click_action)
click_button.place(y=320, x=300, anchor="center")

genv.mainloop()