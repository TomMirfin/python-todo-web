def get_todos(filepath='todos.txt' ):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def add_todo(todo):
    with open('todos.txt', 'w') as file:
       todos = file.writelines(todo)
    return todos

if __name__ == "__gui__":
    get_todos()
    add_todo()