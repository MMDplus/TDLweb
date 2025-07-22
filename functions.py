FILEPATH = "TDLsave.txt"


def get_todos(filepath=FILEPATH):
    """ the funsction get the todos from file and 
    return the list of todos
        """
    
    with open(filepath, 'r', encoding='utf-8') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_local, filepath=FILEPATH):
    with open(filepath, 'w',encoding='utf-8') as file:
        file.writelines(todos_local)


