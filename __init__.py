bl_info ={
    "name": "Pizza Tool",
    "author": "Gingeros",
    "description": "Useful multi tool for Blender",
    "blender": (3, 6, 0),
    "version": (1, 0, 2),
    "location": "",
    "warning": "",
    "category": "Tool"
}
import bpy
from .CScriptUI import *
import inspect

UI_Classes = inspect.getmembers(CScriptUI, inspect.isclass)
reversed = UI_Classes[::-1]

def register():
    for class_type in reversed:
        bpy.utils.register_class(class_type[1])

def unregister():
    for class_type in reversed:
        bpy.utils.unregister_class(class_type[1])

if __name__ == "__main__":
    register()

