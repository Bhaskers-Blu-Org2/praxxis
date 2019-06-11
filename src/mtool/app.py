import sys

def run_notebook(arg):
    from src.mtool.notebook import run_notebook
    run_notebook.run_notebook(arg)
    return
 
def open_notebook(arg):
    from src.mtool.notebook import open_notebook
    open_notebook.open_notebook(arg)
    return
 
def search_notebook(arg):
    from src.mtool.notebook import search_notebook
    search_notebook.search_notebook(arg)
    return

def list_notebook(arg):
    from src.mtool.notebook import list_notebook
    list_notebook.list_notebook(arg)
    return

def history(arg):
    from src.mtool.cli import history
    history.history(arg)
    return

def next_notebook(arg):
    ##TODO  implement this
    return "coming soon"

def new_scene(arg):
    from src.mtool.scene import new_scene
    new_scene.new_scene(arg)
    return
 
def end_scene(arg):
    from src.mtool.scene import end_scene
    end_scene.end_scene(arg)
    return
 
def change_scene(arg):
    from src.mtool.scene import change_scene
    change_scene.change_scene(arg)
    return
 
def resume_scene(arg):
    from src.mtool.scene import resume_scene
    resume_scene.resume_scene(arg)
    return
 
def delete_scene(arg):
    from src.mtool.scene import delete_scene
    delete_scene.delete_scene(arg)
    return

def list_scene(arg):
    from src.mtool.scene import list_scene
    list_scene.list_scene(arg)
    return

def add_library(arg):
    ##TODO: implement this
    return "coming soon"

def list_library(arg):
    from src.mtool.library import list_library
    list_library.list_library(arg)
    return

def set_env(arg):
    from src.mtool.environment import set_env
    set_env.set_env(arg)
    return

def delete_env(arg):
    from src.mtool.environment import delete_env
    delete_env.delete_env(arg)
    return

def default(arg):
    from src.mtool.scene import current_scene
    current_scene.current_scene(arg)
    return
 
def command(argument):
    argument.pop(0)
    switcher = {
        "run_notebook": run_notebook,
        "open_notebook": open_notebook,
        "search_notebook": search_notebook,
        "list_notebook": list_notebook,
        "history": history,
        "next_notebook": next_notebook,
        "new_scene": new_scene,
        "end_scene": end_scene,
        "change_scene": change_scene,
        "resume_scene": resume_scene,
        "delete_scene": delete_scene,
        "list_scene": list_scene,
        "add_library": add_library,
        "list_library": list_library,
        "set_env": set_env,
        "delete_env": delete_env
    }

    if(len(argument)):
        func = switcher.get(argument[0], lambda x: default(x))
    else:
        func = switcher.get(None, lambda x: default(x))

    return func(argument)
    
if __name__ == "__main__":
    command(sys.argv)
