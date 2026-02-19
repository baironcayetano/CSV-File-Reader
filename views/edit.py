from tkinter import Toplevel, Label, Entry,Button, END

def Render_Edit(tree, value, title):
    """This function renders a new window able to edit a column of the treevier"""
    edit_window = Toplevel(tree.master)
    header = f"Element: {title}"
    title = f"Cell Content | {title}"
    edit_window.title(title)

    label = Label(edit_window, text=header)
    label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
   
    entry  = Entry(edit_window,width=40)
    entry.insert(0, value)
    entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    entry.select_range(0, END)
    entry.focus()
    entry.bind("<Return>", lambda e: on_save())

    result = {"value":None, "cancelled":True}

    def on_save():
        result["value"] = entry.get()
        result["cancelled"] = False
        edit_window.destroy()

    def on_cancel():
        edit_window.destroy()

    button_save = Button(edit_window, width=20, text="Save", command=on_save)
    button_save.grid(row=2, column=0, padx=10, pady=10)

    button_cancel = Button(edit_window, width=20, text="Cancel", command=on_cancel)
    button_cancel.grid(row=2, column=1, padx=10, pady=10)

    edit_window.wait_window()
    return result