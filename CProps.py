import bpy
from .Funcs import *


bpy.types.Scene.saved_location = bpy.props.FloatVectorProperty(
    name="Pizza_Tool_Saved_Location",
    description="Saved location of the selected object",
    size=3,  # 3D vector (X, Y, Z)
)
bpy.types.Scene.saved_rotation = bpy.props.FloatVectorProperty(
    name="Pizza_Tool_Saved_Rotation",
    description="Saved rotation of the selected object",
    size=3,  # 3D vector (X, Y, Z)
)
bpy.types.Scene.saved_scale = bpy.props.FloatVectorProperty(
    name="Pizza_Tool_Saved_Scale",
    description="Saved scale of the selected object",
    size=3,  # 3D vector (X, Y, Z)
)
bpy.types.Scene.allmaterials = bpy.props.EnumProperty(items=getsets, update=mat_update, name="All Available Materials")
bpy.types.Scene.assign_material_allmaterials = bpy.props.EnumProperty(items=getsets, update=mat_update, name="All Available Materials")
#bpy.types.Scene.selected_object_materials = bpy.props.EnumProperty()
