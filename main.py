from re import S
import tkinter, boto3, os, os.path
from tkinter import Tk, Label, Button, messagebox
from dotenv import load_dotenv
from pathlib import Path

# Create the default window
root = tkinter.Tk()
root.title("SMS Sender")
root.geometry('900x500')
root.configure(background='#255373')
button_env_color="gray"

#checkenv function!
def env_button():
    if os.path.isfile('.env'):
        print(" You are good with .env :) \n")
    else:
        os.system('python get-env.py')
        print(" You need to add .env file first! \n Restart main program after adding! \n")

#Sender function
def click_action():
    if os.path.isfile('.env'):
        load_dotenv()

        access_key = os.getenv('access_key_env')
        secret = os.getenv('secret_env')
        region = os.getenv('region_env')

        number = '+48'+numberbox.get(1.0, "end-1c")
        sms_message = sms_messagebox.get(1.0, "end-1c")
        sender_id = sender_idbox.get(1.0, "end-1c")

        sns = boto3.client('sns', aws_access_key_id=access_key, aws_secret_access_key=secret, region_name=region)
        sns.publish(PhoneNumber=number, Message=sms_message, MessageAttributes={'AWS.SNS.SMS.SenderID': {'DataType': 'String', 'StringValue': sender_id}, 'AWS.SNS.SMS.SMSType': {'DataType': 'String', 'StringValue': 'Promotional'}})
        
        messagebox.showinfo(title="INFO", message="Message sent!")
    else:
        messagebox.showerror(title="Error", message="Set .ENV before using!")

#Program start
label = Label(root, text="Put data in boxes below", font=('helvetica', 22), fg="Black")
label.pack()

#Box
label1 = Label(root, text="Put destination phone number in the box", font=('helvetica', 10), fg="Black")
label1.pack()
numberbox = tkinter.Text(root,
                   height = 2,
                   width = 40)
  
numberbox.place(y=30, x=250)

label2 = Label(root, text="Put your text message", font=('helvetica', 10), fg="Black")
label2.pack()
sms_messagebox = tkinter.Text(root,
                   height = 5,
                   width = 40)
  
sms_messagebox.pack()

label3 = Label(root, text="Add sginature (alphanumeric only <11)", font=('helvetica', 10), fg="Black")
label3.pack()
sender_idbox = tkinter.Text(root,
                   height = 1,
                   width = 20)
  
sender_idbox.pack()

#.env file button
env_button = Button(root, text="Check .env", font=('helvetica', 8), fg="Black", command=env_button)
env_button.place(x=2, y=2)

#Sending button
click_button = Button(root, text="Send SMS", width=8, command=click_action)
click_button.pack()

root.mainloop()