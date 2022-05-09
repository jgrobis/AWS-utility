from re import S
import tkinter, boto3, os
from tkinter import Tk, Label, Button
from dotenv import load_dotenv
from pathlib import Path

# Create the default window
root = tkinter.Tk()
root.title("SMS Sender")
root.geometry('700x500')

load_dotenv()

access_key = os.getenv('access_key_env')
secret = os.getenv('secret_env')
region = os.getenv('region_env')

print(access_key, secret)
#Sender function
def click_action():
    load_dotenv()

    access_key = os.getenv('access_key_env')
    secret = os.getenv('secret_env')
    region = os.getenv('region_env')

    number = '+48'+numberbox.get(1.0, "end-1c")

    sms_message = sms_messagebox.get(1.0, "end-1c")

    sender_id = sender_idbox.get(1.0, "end-1c")

    sns = boto3.client('sns', aws_access_key_id=access_key, aws_secret_access_key=secret, region_name=region)
    sns.publish(PhoneNumber=number, Message=sms_message, MessageAttributes={'AWS.SNS.SMS.SenderID': {'DataType': 'String', 'StringValue': sender_id}, 'AWS.SNS.SMS.SMSType': {'DataType': 'String', 'StringValue': 'Promotional'}})
    
    label4 = Label(root, text="Wiadomość wysłana!", font=('helvetica', 10))
    root.create_window(200, 210, window=label3)

#Wiadomosc na gorze sotrny
label = Label(root, text="Uzupełnij pola by wysłać wiadomość", font=('helvetica', 22), fg="Black")
label.pack()

#Boxy
label1 = Label(root, text="Wprowadź numer telefonu bez przedrostka +48", font=('helvetica', 10), fg="Black")
label1.pack()
numberbox = tkinter.Text(root,
                   height = 2,
                   width = 40)
  
numberbox.pack()

label2 = Label(root, text="Wprowadź treść wiadomości", font=('helvetica', 10), fg="Black")
label2.pack()
sms_messagebox = tkinter.Text(root,
                   height = 5,
                   width = 40)
  
sms_messagebox.pack()

label3 = Label(root, text="Dodaj podpis", font=('helvetica', 10), fg="Black")
label3.pack()
sender_idbox = tkinter.Text(root,
                   height = 1,
                   width = 20)
  
sender_idbox.pack()

#Przycisk do wysłania
click_button = Button(root, text="Wyślij SMS", width=8, command=click_action)
click_button.pack()

#Jakes cos XD
lbl = tkinter.Label(root, text = "")
lbl.pack()
root.mainloop()