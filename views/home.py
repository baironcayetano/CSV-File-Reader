import tkinter as tk
from tkinter import ttk, Label, Button
from utils.actions import Open_File_Dialog
from views.table import Render_Table

def Render_Home(root):
    frame = ttk.Frame(root)
    frame.pack(fill='both', padx=5, pady=5, expand=True)

    label = Label(frame, text="Select a CSV file to display")
    button = Button(frame, text="Browse", command=lambda:Open_File_Dialog(root, frame, Render_Table))
    
    label.pack(pady=5, anchor="center")
    button.pack(pady=5, anchor="center")
    return 