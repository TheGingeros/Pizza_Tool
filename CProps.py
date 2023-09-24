import bpy

bpy.types.Scene.saved_location = bpy.props.FloatVectorProperty(
    name="Pizza_Tool_Saved_Location",
    description="Saved location of the selected object",
    size=3,  # 3D vector (X, Y, Z)
)

#bpy.types.Scene.selected_object_materials = bpy.props.EnumProperty()
