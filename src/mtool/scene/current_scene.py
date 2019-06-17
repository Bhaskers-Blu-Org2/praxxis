"""
This file displays the current scene from the scene history db
"""

def current_scene(scene_root, history_db):
    """calls the scene init, and displays the current scene from the sqlite history db""" 
    from src.mtool.util import sqlite_util
    from src.mtool.scene import scene
    from src.mtool.cli import display

    scene.init_scene(scene_root, history_db)
    display.display_current_scene(sqlite_util.get_current_scene(history_db))
    
    