from tkinter import *
from tkinter import messagebox
import os
import lyricsgenius

def get_lyrics(api_token, song):
    genius = lyricsgenius.Genius(api_token)
    try:
        song_lyrics = genius.search_song(song)
        if song_lyrics:
            return song_lyrics.lyrics
        else:
            return "Lyrics not found."
    except Exception as e:
        return f"Error: {e}"

def extract_lyrics(event=None):
    api_token = "df2f8ddac6mshbd84ccac41377b5p1f774ejsn0c1d3b890b5f"
    song = song_entry.get()
    if not api_token or not song:
        messagebox.showinfo("Error", "Please provide a valid API token and song name.")
        return
    lyrics = get_lyrics(api_token, song)
    result_text.delete(1.0, END)
    result_text.insert(END, lyrics)

def on_entry_click(event):
    if song_entry.get() == "Search for a song":
        song_entry.delete(0, "end")
        song_entry.insert(0, '')
        song_entry.config(fg='black')

def on_focus_out(event):
    if song_entry.get() == '':
        song_entry.insert(0, "Search for a song")
        song_entry.config(fg='grey')

root = Tk()
root.title('Home')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1002
window_height = 712
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y - 40}')
root.resizable(False, False)

background = PhotoImage(file='Home.png')
label = Label(root, image=background)
label.pack()
root.iconbitmap('icon.ico')

if os.path.exists('username.txt'):
    with open("username.txt", "r") as f:
        username = f.read()
else:
    username="Unknown user"

username_label=Label(root,bg="#fff",width=9,text=username,font=('Roboto',13))
username_label.place(x=85,y=48)

song_entry = Entry(root, width=40, font=('Roboto', 16), bg='#fff', border=0)
song_entry.place(x=282, y=262)
song_entry.insert(0,"Search for a song")
song_entry.bind('<FocusIn>', on_entry_click)
song_entry.bind('<FocusOut>', on_focus_out)
song_entry.bind("<Return>", extract_lyrics)

result_text = Text(root, height=18, width=64, bg='#fff', border=0)
result_text.place(x=244, y=329)

# Start the GUI main loop
root.mainloop()
