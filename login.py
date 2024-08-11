from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from subprocess import Popen
from customtkinter import CTkEntry, CTkButton


def signin():

    username_text = user.get()
    password_text = password.get()

    if not username_text or not password_text:
        messagebox.showerror("Error", "Username and password are required!")
        return

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username_text, password_text))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        with open("username.txt", "w") as f:
            f.write(username_text)
        lyrics_window()


    else:
        messagebox.showerror("Error", "Invalid username or password!")

    conn.close()


def lyrics_window():
    Popen('python Home.py')

def signup_window():
    Popen('python signup.py')
    root.destroy()

def hide_password():
    if password.cget('show') == '*':
        password.configure(show='')
    else:
        password.configure(show='*')

root = Tk()
root.title('Login')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 512
window_height = 712
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y - 40}')
root.resizable(False, False)

background = PhotoImage(file='Frame 1.png')
label = Label(root, image=background)
label.pack()
root.iconbitmap('icon.ico')

signIn_lbl = Label(root, text="Sign In", fg='#000', bg='white', font=('Roboto', 16))
signIn_lbl.place(x=220, y=250)

user_lbl = Label(root, text="Username", font=('Roboto', 16), width=0, height=0, bg='#fff')

user = CTkEntry(root, width=160, height=13, fg_color='#fff', text_color='black', border_width=0,font=("Roboto", 13, "normal"))
user.place(x=176, y=321)

pass_lbl = Label(root, text="Password", font=('Roboto', 14), width=0, height=0, bg='#fff')

password = CTkEntry(root, width=160, height=13, fg_color='#fff', show='*', text_color='black', border_width=0,font=("Roboto", 13, "normal"))
password.place(x=176, y=384)

hide_image=PhotoImage(file='hide.png')
hide_btn = Button(root, image=hide_image, bg='#fff', border=0, command=hide_password)
hide_btn.place(x=348, y=384)

btn_image = PhotoImage(file='Button.png')
bt_login = CTkButton(root, image=btn_image, width=0, height=0, border_color='#fff', border_width=0, state="normal",bg_color='#fff', fg_color="#fff", text="", corner_radius=32, hover=0, command=signin)
bt_login.place(x=193, y=430)

btn_signup = Button(root, text="Sign up", font=('Roboto', 7), bg='white', fg='purple', border=0, command=signup_window)
btn_signup.place(x=295, y=498)

root.mainloop()
