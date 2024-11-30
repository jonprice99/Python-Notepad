import os

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from PIL import Image, ImageTk

from datetime import datetime

UNTITLED_STRING = "Untitled - Notepad"
WINDOW_SIZE = "650x500"
DEFAULT_FONT = "Consolas"
DEFAULT_FONT_SIZE = 11
RESIZE_SETTING = 1

root = Tk()
frame = Frame(root)
frame.pack(expand = True, fill = 'both')
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
menu_bar = Menu(root)
text_area = Text(frame, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), undo = True, wrap = "word")

# Function to build the app's menu system
def build_menu():
    # Add the File Menu and its components to create Python Text Editor
    file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
    file_menu.add_command(label="New (Ctrl + N)", command=open_new_file)
    file_menu.add_command(label="Open File (Ctrl + O)", command=open_file)
    file_menu.add_command(label="Save As (Ctrl + S)", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit (Ctrl + Q)", command=quit_app)
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    # Add the Edit Menu and its components
    edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
    edit_menu.add_command(label='Copy (Ctrl + C)', command=copy_text)
    edit_menu.add_command(label='Cut (Ctrl + X)', command=cut_text)
    edit_menu.add_command(label='Paste (Ctrl + V)', command=paste_text)
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo (Ctrl + Z)", command=undo_text)
    edit_menu.add_command(label="Redo (Ctrl + Y)", command=redo_text)
    edit_menu.add_separator()
    edit_menu.add_command(label='Select All (Ctrl + A)', command=select_all)
    edit_menu.add_separator()
    edit_menu.add_command(label="Insert Date (F5)", command=insert_date)
    edit_menu.add_command(label="Insert Date & Time (F6)", command=insert_date_and_time)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    
    # Add the Help Menu and its components
    help_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
    help_menu.add_command(label='About Notepad', command=about_notepad)
    help_menu.add_command(label='About Commands', command=about_commands)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menu_bar)
    
    # Add the keyboard shortcuts
    root.bind(sequence = '<Control-o>', func = open_file)
    root.bind(sequence = "<Control-n>", func = open_new_file)
    root.bind(sequence = "<Control-s>", func = save_file)
    root.bind(sequence = "<Control-q>", func = quit_app)
    root.bind(sequence = "<F1>", func=about_commands)
    root.bind(sequence = "<F5>", func=insert_date)
    root.bind(sequence = "<F6>", func=insert_date_and_time)

def build_text_area():
    text_area.grid(row=0, column=0, sticky="nsew")
    scroller = Scrollbar(frame, orient=VERTICAL)
    scroller.config(command=text_area.yview)
    scroller.grid(row=0, column=1, sticky="ns")
    text_area.config(yscrollcommand=scroller.set)

# Initialize the text editor window
def initialize(): 
    root.title(UNTITLED_STRING)
    root.geometry(WINDOW_SIZE)
    root.resizable(RESIZE_SETTING, RESIZE_SETTING)
    root.columnconfigure(index = 0, weight = 1)
    root.rowconfigure(index = 0, weight = 1)

    icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
    root.iconphoto(False, icon)
    
    # Build the menu
    build_menu()
    
    # Build the text area
    build_text_area()

    # Finalize the window
    root.update()
    root.mainloop()

# Function to create a new file
def open_new_file():
    root.title(UNTITLED_STRING)
    text_area.delete(1.0, END)

# Function to open an existing file
def open_file(event=None):
    file = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")]) 
    # Check if the file exists 
    if file: 
        root.title(f"{os.path.basename(file)} ({file}) - Notepad") 
        text_area.delete(1.0, END) 
        
        # Load the existing file contents into the window 
        with open(file, mode='r') as file_temp: 
            text_area.insert(1.0, file_temp.read()) 
    else: 
        file = None

# Function to save a file
def save_file(event=None):
    global text_area
    file_content = text_area.get(1.0, END) 
    
    file_path = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[("Text File", "*.txt"), ("Word Document", "*.docx"), ("PDF", "*.pdf")]) 
    
    if file_path: 
        with open(file_path, "w") as file: 
            file.write(file_content) 
            root.title(f"{os.path.basename(file_path)} ({file_path}) - Notepad")

# Function to select all text
def select_all():
    text_area.event_generate("<<Control-Keypress-A>>")

# Function to cut text
def cut_text():
    text_area.event_generate("<<Cut>>")

# Function to copy text
def copy_text():
    text_area.event_generate("<<Copy>>")

# Function to paste text
def paste_text():
    text_area.event_generate("<<Paste>>")

# Function to undo text
def undo_text():
    mb.showerror("Cannot Undo", "This feature is currently in development.")

# Function to redo text
def redo_text():
    mb.showerror("Cannot Redo", "This feature is currently in development.")

# Function to display app information
def about_notepad():
    mb.showinfo("About Notepad", "A basic Notepad written in Python without pesky, unwanted features.")

# Function to quit the app
def quit_app(event=None):
    root.destroy()

# Function to insert the current date into the document
def insert_date(event=None):
    curr_date = datetime.now()
    formatted_date = curr_date.strftime("%B %d, %Y \n")
    text_area.insert(END, formatted_date)

# Function to insert the current date into the document
def insert_date_and_time(event=None):
    curr_date = datetime.now()
    formatted_date = curr_date.strftime("%B %d, %Y %I:%M:%S %p \n")
    text_area.insert(END, formatted_date)

# Function to display info about app features/commands
def about_commands(event=None):
   commands = """
    Under the File Menu:
    - 'New' clears the entire Text Area
    - 'Open' clears text & opens another file
    - 'Save As' saves your file in the same / another extension
    
    Under the Edit Menu:
    - 'Copy' copies the selected text to your clipboard
    - 'Cut' cuts the selected text & removes it from the text area
    - 'Paste' pastes the copied/cut text
    - 'Select All' selects the entire text
    - 'Delete' deletes the last character
    - 'Insert Date' puts the date on the current line
    - 'Insert Date & Time' same as 'Insert Date' but with time
    """
   mb.showinfo(title="All Commands", message=commands)

initialize()