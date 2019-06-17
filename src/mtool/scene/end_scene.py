"""
This file ends the specified scene
"""

def end_scene(args, scene_root, history_db, current_scene_db):
    """Ends a scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.scene import scene

    scene.init_scene(scene_root, history_db)
    
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    allow_end_scene = sqlite_util.mark_ended_scene(history_db, name)

    if allow_end_scene == -1:
        display.scene_does_not_exist_error(name)
    elif allow_end_scene:
        sqlite_util.end_scene(current_scene_db, name)
        display.display_end_scene_success(name)
    else:
        display.last_active_scene_error(name)

        
    