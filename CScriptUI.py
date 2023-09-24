import bpy
from .COperators import *
from .CProps import *

class OBJECT_PT_ObjectTool_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_ObjectTool_UI"
    bl_label = "Object Tool" #Name when tab is open
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_order = 0

    def draw_header(self, context):
        self.layout.label(text="", icon="MODIFIER_DATA")

    def draw(self,context):
        layout = self.layout
        row = layout.row()
        #row.operator("wm.object_tool_Paste") #TODO

class OBJECT_PT_CopyObjectLocation_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_CopyObjectLocation_UI"
    bl_label = "Copy Objects Location" #Name when tab is open
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_parent_id = OBJECT_PT_ObjectTool_UI.bl_idname
    bl_order = 0
    
    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_ORIGIN")
    def draw(self,context):
        layout = self.layout

        #Get location of selected object
        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)>1): layout.label(text="Select only one object!")
        if(len(selected_objects)==0): layout.label(text="No objects selected")
        if(len(selected_objects)==1):
            object = selected_objects[0]
            loc = object.location
            row = layout.row()
            row.label(text="{}: {:.6f}, {:.6f}, {:.6f}".format(object.name, loc[0],loc[1],loc[2]))

            copy_button = row.operator(
            "object.pizza_tool_copy", text="Copy Location", icon='COPYDOWN')
            paste_button = row.operator(
            "object.pizza_tool_paste",text="Paste Location", icon='COPYDOWN')
            
            
class OBJECT_PT_MaterialTool_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_MaterialTool_UI"
    bl_label = "Material Tool" #Name when tab is open
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_order = 0

    def draw_header(self, context):
        self.layout.label(text="", icon="IMAGE")

    def draw(self,context):
        layout = self.layout

class OBJECT_PT_MaterialTool_SelectByMaterial_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_MaterialTool_SelectByMaterial_UI"
    bl_label = "Select Objects by Material"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_parent_id = OBJECT_PT_MaterialTool_UI.bl_idname

    def draw_header(self, context):
        self.layout.label(text="", icon="SHADING_TEXTURE")

    def draw(self,context):
        layout = self.layout

        #Showing of currently selected object and its active material
        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)>1): layout.label(text="Select only one object!")
        if(len(selected_objects)==0): layout.label(text="No objects selected")
        if(len(selected_objects)==1):
            object = selected_objects[0]
            row = layout.row()
            row.label(text="{}      Active Material: {}".format(object.name, object.active_material.name))

            select_button = row.operator(
            "object.pizza_tool_select_material", text="Select Objects by Material", icon='COPYDOWN')





