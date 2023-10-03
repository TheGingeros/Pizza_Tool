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
            "object.pizza_tool_copy", text="", icon='COPYDOWN')
            paste_button = row.operator(
            "object.pizza_tool_paste",text="", icon='COPYDOWN')

class OBJECT_PT_CopyObjectRotation_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_CopyObjectRotation_UI"
    bl_label = "Copy Objects Rotation" #Name when tab is open
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_parent_id = OBJECT_PT_ObjectTool_UI.bl_idname
    bl_order = 1
    
    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_ORIGIN")
    def draw(self,context):
        layout = self.layout

        #Get rotation of selected object
        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)>1): layout.label(text="Select only one object!")
        if(len(selected_objects)==0): layout.label(text="No objects selected")
        if(len(selected_objects)==1):
            object = selected_objects[0]
            rot = object.rotation_euler
            row = layout.row()
            row.label(text="{}: {:.6f}, {:.6f}, {:.6f}".format(object.name, rot[0],rot[1],rot[2]))

            copy_button = row.operator(
            "object.pizza_tool_copyrot", text="", icon='COPYDOWN')
            paste_button = row.operator(
            "object.pizza_tool_pasterot",text="", icon='COPYDOWN')

class OBJECT_PT_CopyObjectScale_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_CopyObjectScale_UI"
    bl_label = "Copy Objects Scale" #Name when tab is open
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_parent_id = OBJECT_PT_ObjectTool_UI.bl_idname
    bl_order = 2
    
    def draw_header(self, context):
        self.layout.label(text="", icon="OBJECT_ORIGIN")
    def draw(self,context):
        layout = self.layout

        #Get rotation of selected object
        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)>1): layout.label(text="Select only one object!")
        if(len(selected_objects)==0): layout.label(text="No objects selected")
        if(len(selected_objects)==1):
            object = selected_objects[0]
            scale = object.scale
            row = layout.row()
            row.label(text="{}: {:.6f}, {:.6f}, {:.6f}".format(object.name, scale[0],scale[1],scale[2]))

            copy_button = row.operator(
            "object.pizza_tool_copyscale", text="", icon='COPYDOWN')
            paste_button = row.operator(
            "object.pizza_tool_pastescale",text="", icon='COPYDOWN')
            
            
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
    bl_order = 3

    def draw_header(self, context):
        self.layout.label(text="", icon="SHADING_TEXTURE")

    def draw(self,context):
        layout = self.layout
        box = layout.box()
        #Showing of currently selected object and its active material
        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)>1): box.label(text="Select only one object!")
        if(len(selected_objects)==0): box.label(text="No objects selected")
        if(len(selected_objects)==1):
            object = selected_objects[0]
            #box.operator("object.select_all").action = 'TOGGLE'
            if object.active_material == None:
                print("No active material")
                box.label(text="{}      Active Material: None".format(object.name))
            else:
                box.label(text="{}      Active Material: {}".format(object.name, object.active_material.name))
                select_button = box.operator(
                "object.pizza_tool_select_material", text="Select Objects By Material", icon='COPYDOWN')



class OBJECT_PT_MaterialTool_AssignMaterialToObject_UI(bpy.types.Panel):
    bl_idname = "OBJECT_PT_MaterialTool_AssignMaterialToObject_UI"
    bl_label = "Assign Material to Selected Objects"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pizza Tool" #Name of the category in 3d view
    bl_parent_id = OBJECT_PT_MaterialTool_UI.bl_idname
    bl_order = 3

    def draw_header(self, context):
        self.layout.label(text="", icon="SHADING_TEXTURE")

    def draw(self,context):
        layout = self.layout

        selected_objects = bpy.context.selected_objects
        if(len(selected_objects)<1):
            layout.label(text="No objects selected")
        else:
            #print(selected_objects)
            object = bpy.context.active_object
            row = layout.row()
            try:
                row.label(text="Active Object: {}      Active Material: {}".format(object.name, object.active_material.name))
                assign_button = row.operator(
                "object.pizza_tool_assign_material", text="", icon='COPYDOWN'
            )

            except:
                row.label(text="Active Object: {}      Active Material: No Active Material".format(object.name))










