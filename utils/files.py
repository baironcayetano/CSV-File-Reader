import csv

def Open(filepath, root, function=None):
    """ This function opens a .csv file and if a functions is given, 
         it will execute the function with the file as an argument, 
         passing the optional arguments to the function as well."""

    with open(filepath) as file:
            reader = csv.reader(file)
            if function:
                filename = filepath.split('/')[-1].split('.')[0]
                return function(filename,filepath, reader, root)
            else:
                return None

def Save(filepath, tree, function):
    """This function saves the content of the treeview widget in a .csv file"""
    try:
        with open(filepath, 'w') as file:
            writer = csv.writer(file)
            for row_id in tree.get_children():
                row = tree.item(row_id)['values']
                writer.writerow(row[1:]) 
            if function:
                return function(filepath, tree)
            else:
                return None 
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")