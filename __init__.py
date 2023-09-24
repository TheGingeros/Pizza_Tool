bl_info ={
    "name": "Pizza Tool",
    "author": "Gingeros",
    "description": "Useful multy tool for Blender",
    "blender": (3, 6, 0),
    "version": (1, 0, 0),
    "location": "",
    "warning": "",
    "category": "Tool"
}
import bpy
from .CScriptUI import *
from .COperators import *

def register():
    bpy.utils.register_class(OBJECT_PT_ObjectTool_UI)
    bpy.utils.register_class(OBJECT_PT_MaterialTool_UI)
    bpy.utils.register_class(OBJECT_PT_MaterialTool_SelectByMaterial_UI)
    bpy.utils.register_class(OBJECT_PT_CopyObjectLocation_UI)
    bpy.utils.register_class(OBJECT_OT_pizza_tool_copy)
    bpy.utils.register_class(OBJECT_OT_pizza_tool_paste)
    bpy.utils.register_class(OBJECT_OT_pizza_tool_select_material)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_ObjectTool_UI)
    bpy.utils.unregister_class(OBJECT_PT_MaterialTool_UI)
    bpy.utils.unregister_class(OBJECT_PT_MaterialTool_SelectByMaterial_UI)
    bpy.utils.unregister_class(OBJECT_PT_CopyObjectLocation_UI)
    bpy.utils.unregister_class(OBJECT_OT_pizza_tool_copy)
    bpy.utils.unregister_class(OBJECT_OT_pizza_tool_paste)
    bpy.utils.unregister_class(OBJECT_OT_pizza_tool_select_material)

if __name__ == "__main__":
    register()

