import bpy

from .CProps import *

class OBJECT_OT_pizza_tool_copy(bpy.types.Operator):
    """Copy the location of an object to the memory"""
    bl_idname = "object.pizza_tool_copy"
    bl_label = ""
    def execute(self, context):
        print("Execute Copying")
        location = bpy.context.selected_objects[0].location
        context.scene.saved_location = location
        self.report(
            {'INFO'}, "Location copied: {:.6f}, {:.6f}, {:.6f}".format(location[0],location[1],location[2]))
        return {'FINISHED'}

class OBJECT_OT_pizza_tool_paste(bpy.types.Operator):
    """Paste the location from memory to selected object """
    bl_idname = "object.pizza_tool_paste"
    bl_label = ""
    def execute(self, context):
        if (hasattr(bpy.context.scene, 'saved_location')):
            print("Location found, passing it to the object")
            bpy.context.selected_objects[0].location = bpy.context.scene.saved_location
            self.report(
                {'INFO'}, "Location was pasted to the selected object.")
        return {'FINISHED'}

class OBJECT_OT_pizza_tool_select_material(bpy.types.Operator):
    """Select all objects with the same material"""
    bl_idname = "object.pizza_tool_select_material"
    bl_label = ""

    def execute(self, context):
        active_material_name = context.active_object.active_material.name
        all_objects = context.selectable_objects
        selected_object_count = 0
        for object in all_objects:
            if(object.material_slots.find(active_material_name)!=-1):
                object.select_set(True)
                selected_object_count +=1
            else:
                pass
        if(selected_object_count > 1):
            self.report(
                {'INFO'}, "Succesfully selected all objects by material: {}".format(active_material_name))
        else:
            self.report(
                {'INFO'}, "No objects with the same material.")           
        return {'FINISHED'}

