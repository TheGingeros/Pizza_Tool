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
    
class OBJECT_OT_pizza_tool_assign_material(bpy.types.Operator):
    """Assign active material to all selected objects"""
    bl_idname = "object.pizza_tool_assign_material"
    bl_label = ""

    def execute(self,context):
        active_material = context.active_object.active_material
        all_objects = context.selected_objects
        active_object = context.active_object.name

        for obj in all_objects:
            #Check if object has material slot, if not, we create one
            if(len(obj.material_slots)<1):
                #Create material slot and assign the active_material
                obj.select_set(True)
                obj.data.materials.append(active_material)
            else:
                materialAlreadyUsed = False
                for material in obj.material_slots:
                    #Check if the material isnt already assigned, if yes, we skip to next object
                    if(material.name == active_material.name):
                        materialAlreadyUsed = True
                        break
                if(materialAlreadyUsed == False):
                    #The object doesnt have the material, so we assign it
                    obj.select_set(True)
                    obj.data.materials.append(active_material)
                    materialAlreadyUsed = False

        return {'FINISHED'}    

