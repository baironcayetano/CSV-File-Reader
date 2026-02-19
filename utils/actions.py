from tkinter import filedialog, messagebox, Toplevel, Label
from utils.files import Open, Save
from views.edit import Render_Edit

def Open_File_Dialog(root, frame, function):
    """This function opens a file dialog and returns the selected file path"""
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if filepath and filepath.endswith('.csv'):
            frame.destroy()
            Open(filepath, root, function)
            return filepath
    else:
            messagebox.showerror("Invalid File", "Please select a valid CSV file.")
            return None
        
def On_double_click(event, tree, cols_excel, filepath):
       """It handles the double click event on the treeview widget and opens a new window with the content of the selected cell"""
       item = tree.identify('item', event.x, event.y)
       column = tree.identify_column(event.x)

       try:
              value = tree.item(item, 'values')[int(column[1:]) - 1]
              column_name = cols_excel[int(column[1:]) - 1]
              row_number = tree.item(item, 'values')[0]
       except IndexError:
              return

       if column_name == "#":
              return 
       
       title = f"{column_name}{row_number}"
       result = Render_Edit(tree, value, title)
       
       if not result["cancelled"]:
              tree.set(item, column=column, value=result["value"])
              Save(filepath, tree, None)
