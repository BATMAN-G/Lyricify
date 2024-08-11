import sqlite3
from tkinter import *
from customtkinter import CTkEntry, CTkButton, CTkLabel
from subprocess import Popen
from tkinter import messagebox


def on_button_click():
    username_text = username.get()
    email_text = email.get()
    password_text = password.get()
    cpassword_text = Cpassword.get()

    # Check if all fields are filled
    if not username_text or not email_text or not password_text or not cpassword_text:
        messagebox.showerror("Error", "All fields are required!")
        return
    if password_text != cpassword_text:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    # Check if username and password meet the minimum length requirement
    if  len(password_text) <= 7:
        messagebox.showerror("Error", "Password must be more than 8 characters long!")
        return

    # Check if passwords match


    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Create table with UNIQUE constraints for username and email
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 email TEXT UNIQUE,
                 password TEXT)''')

    try:
        # Check if username or email already exists
        c.execute('SELECT * FROM users WHERE username=? OR email=?', (username_text, email_text))
        if c.fetchone():
            print("Username or email already exists!")
            return

        # Insert new user
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                  (username_text, email_text, password_text))
        conn.commit()
        print("Sign up successful!")
        root.destroy()
        Popen('python login.py')
        show_table_contents()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

    root.destroy()

def show_table_contents():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users')
    rows = c.fetchall()

    print("\nTable contents:")
    for row in rows:
        print(row)

    conn.close()

def hide_password():
    if password.cget('show') == '*':
        password.configure(show='')
        Cpassword.configure(show='')
    else:
        password.configure(show='*')
        Cpassword.configure(show='*')

root = Tk()
root.title('Sign Up')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 512
window_height = 712
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y - 40}')
root.resizable(False, False)

background = PhotoImage(file='Frame 2.png')
label = Label(root, image=background)
label.pack()
root.iconbitmap('icon.ico')

username = CTkEntry(root, width=175, height=13, fg_color='#fff', text_color='black', border_width=0,font=("Roboto", 13, "normal"))
username.place(x=174, y=342)

email = CTkEntry(root, width=175, height=13, fg_color='#fff', text_color='black', border_width=0,font=("Roboto", 13, "normal"))
email.place(x=174, y=394)

password = CTkEntry(root, width=175, height=13, fg_color='#fff', text_color='black', border_width=0,font=("Roboto", 13, "normal"), show='*')
password.place(x=174, y=446)

hide_image=PhotoImage(file='hide.png')
hide_btn = Button(root, image=hide_image, bg='#fff', border=0, command=hide_password)
hide_btn.place(x=358, y=446)

Cpassword = CTkEntry(root, width=175, height=13, fg_color='#fff', text_color='black', border_width=0,font=("Roboto", 13, "normal"), show='*')
Cpassword.place(x=174, y=498)

btn_image = PhotoImage(file='Button 2.png')
bt_login = CTkButton(root, image=btn_image, width=0, height=0, border_color='#fff', border_width=0, state="normal",bg_color='#fff', fg_color="#fff", text="", corner_radius=32, hover=0, command=on_button_click)
bt_login.place(x=193, y=550)

root.mainloop()
