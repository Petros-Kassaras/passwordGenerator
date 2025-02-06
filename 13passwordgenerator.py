from tkinter import *
from tkinter.ttk import *
import random
from ttkthemes import ThemedTk
import pyperclip

screen = ThemedTk(theme="black")
screen.configure(themebg="black")
screen.title("Parathyro") #titlos
screen.geometry('450x100')#parathyro megethos
screen.resizable(width=False,height=False)

def Copy ():
    enti = ent_password.get()
    pyperclip.copy(enti)

def Generate ():
    ch = chce.get()
    ent_password.delete(0,END)
    length = int(cmb_length.get())
    password = ''
    if ch == 1 :
        for i in range(length):
            a = random.choice(letters)
            password += a
    elif ch == 2 :
        for i in range(length):
            a = random.choice(ltrnbr)
            password += a
    else :
        print("strong")
        for i in range(length):
            a = random.choice(ltrnbrcr)
            password += a
    ent_password.insert(END,password)

 # Encrypt each character in the password

def encrypt ():
    passw = ent_password.get() # Find the position of the character in the set
    ent_encrypted.delete(0, END) # Shift the position by 3
    key=3
    encryptpassword =''
    for k in passw:
        if k in characters :
            pos = characters.index(k) # Find the position of the character in the set
            newpos = (pos+key)% len(characters) # Shift the position by 3
            encryptpassword += characters[newpos]
        else:
            encryptpassword +=k # Add the encrypted character
    ent_encrypted.insert(END,encryptpassword)

def decrypt ():
    passw = ent_encrypted.get()
    ent_decrypted.delete(0, END)
    key = 3
    decryptpassword = ''
    for k in passw:
        if k in characters:
            pos = characters.index(k)
            newpos = (pos - key) % len(characters)
            decryptpassword += characters[newpos]
        else:
            decryptpassword += k
    ent_decrypted.insert(END, decryptpassword)


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*?"

characters = letters + numbers + symbols  # All possible characters for Strong complexity
ltrnbr = letters + numbers  # Letters and numbers for Medium complexity
ltrnbrcr = letters + numbers + symbols  # Letters, numbers, and symbols for Strong complexity

lbl_password = Label(screen, text="Password")
ent_password = Entry(screen)
btn_copy = Button(screen, text="Copy",command=Copy)
btn_generate = Button(screen, text="Generate",command=Generate)
lbl_lenght = Label(screen, text="Length")
cmb_length = Combobox(screen, state='readonly')
cmb_length ['values']=('8','9','10','11','12','13','14','15','16','17','18','19','20','64')
chce = IntVar()
rb_low = Radiobutton(screen,text="Low",value=1,variable=chce)
rb_medium = Radiobutton(screen,text="Medium",value=2,variable=chce)
rb3_strong = Radiobutton(screen,text="Strong",value=3, variable =chce)
lbl_encrypted = Label(screen,text="Encrypted password")
ent_encrypted = Entry(screen)
btn_encrypt = Button(screen,text="Encrypt",command=encrypt)
lbl_decrypted = Label(screen,text="Decrypted password")
ent_decrypted = Entry(screen)
btn_decrypt = Button(screen,text="Decrypt",command=decrypt)

chce.set(2)
cmb_length.set(8)


lbl_password.grid(row=0,column=0)
ent_password.grid(row=0,column=1)
btn_copy .grid(row=0,column=2)
btn_generate .grid(row=0,column=3)
lbl_lenght .grid(row=1,column=0)
cmb_length .grid(row=1,column=1)
rb_low.grid(row=1,column=2)
rb_medium .grid(row=1,column=3)
rb3_strong .grid(row=1,column=4)
lbl_encrypted .grid(row=2,column=0)
ent_encrypted .grid(row=2,column=1)
btn_encrypt.grid(row=2,column=2)
lbl_decrypted .grid(row=3,column=0)
ent_decrypted .grid(row=3,column=1)
btn_decrypt .grid(row=3,column=2)

screen.mainloop() #kleinei programma