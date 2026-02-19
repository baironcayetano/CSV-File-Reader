import tkinter as tk
from tkinter import ttk
from utils.actions import On_double_click

def Render_Table(filename, filepath, reader, root):
    """This function renders the content of a .csv file in a treeview widget"""

    tree = ttk.Treeview(root)
    tree.pack(fill='both',padx=2, pady=2, expand=True)
    
    #headers
    csv_headers = next(reader)
    
    # of columns in the csv file       
    cols_excel = ['#', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num_cols = len(csv_headers)
    active_cols = cols_excel[:num_cols + 1] 

    #window title        
    tree.master.title(f"CSV File Editor | {filename}")

    #rendering the headers of the treeview
    tree.config(columns=active_cols, show='headings')
    tree.heading('#', text='#', anchor='center')
    tree.column('#', width=40, anchor='center')
            
    for i in range(num_cols):
         col_id = active_cols[i+1]
         tree.heading(col_id, text=col_id, anchor='center')
         tree.column(col_id, anchor='center', width=100)

    tree.insert('', 'end', values=[1] + csv_headers)
    
    i = 2
    for row in reader:
         tree.insert('', 'end', values=[i]+row)
         i +=1

    tree.bind("<Double-Button-1>", lambda e: On_double_click(e, tree, cols_excel, filepath))
    return tree
