"""
Author: Bairon Cayetano
Proyect Name: CSV File Editor
"""
import tkinter as tk
from tkinter import ttk
from views.home import Render_Home

def config():
    root = tk.Tk()
    root.option_add("*Font", "Helvetica 16")
    root.title("CSV File Editor")
    root.geometry("1200x800")

    style = ttk.Style()
    style.theme_use('clam') 

    style.configure("Treeview", 
                background="white", 
                foreground="black", 
                fieldbackground="white", 
                font=("Segoe UI", 11),
                rowheight=30)

    style.configure("Treeview.Heading", 
                background="green", 
                foreground="white", 
                font=("Segoe UI", 12, "bold"),
                relief="flat")
    
    style.map("Treeview.Heading",  background=[('active', "#50BF34")])
    Render_Home(root)
    root.mainloop()

def main():
     config()

if __name__ == "__main__":
    main()