import bpy

bpy.types.Scene.select_material_list = bpy.props.CollectionProperty(
        type=bpy.types.PropertyGroup,
        name="Pizza_Tool_Select_Material_List",
        description="List that stores active materials in scene",
)
bpy.types.Scene.select_material_list_index = bpy.props.IntProperty(
    name = "Index for material_list",
    default = 0)

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

#bpy.types.Scene.selected_object_materials = bpy.props.EnumProperty()
