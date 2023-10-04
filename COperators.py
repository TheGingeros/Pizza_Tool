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

class OBJECT_OT_pizza_tool_copyrot(bpy.types.Operator):
    """Copy the rotation of an object to the memory"""
    bl_idname = "object.pizza_tool_copyrot"
    bl_label = ""
    def execute(self, context):
        print("Execute Copying")
        rotation = bpy.context.selected_objects[0].rotation_euler
        context.scene.saved_rotation = rotation
        self.report(
            {'INFO'}, "Rotation copied: {:.6f}, {:.6f}, {:.6f}".format(rotation[0],rotation[1],rotation[2]))
        return {'FINISHED'}

class OBJECT_OT_pizza_tool_pasterot(bpy.types.Operator):
    """Paste the rotation from memory to selected object """
    bl_idname = "object.pizza_tool_pasterot"
    bl_label = ""
    def execute(self, context):
        if (hasattr(bpy.context.scene, 'saved_rotation')):
            print("Rotation found, passing it to the object")
            bpy.context.selected_objects[0].rotation_euler = bpy.context.scene.saved_rotation
            self.report(
                {'INFO'}, "Rotation was pasted to the selected object.")
        return {'FINISHED'}
    
class OBJECT_OT_pizza_tool_copyscale(bpy.types.Operator):
    """Copy the scale of an object to the memory"""
    bl_idname = "object.pizza_tool_copyscale"
    bl_label = ""
    def execute(self, context):
        print("Execute Copying")
        scale = bpy.context.selected_objects[0].scale
        context.scene.saved_scale = scale
        self.report(
            {'INFO'}, "Scale copied: {:.6f}, {:.6f}, {:.6f}".format(scale[0],scale[1],scale[2]))
        return {'FINISHED'}

class OBJECT_OT_pizza_tool_pastescale(bpy.types.Operator):
    """Paste the scale from memory to selected object """
    bl_idname = "object.pizza_tool_pastescale"
    bl_label = ""
    def execute(self, context):
        if (hasattr(bpy.context.scene, 'saved_scale')):
            print("Scale found, passing it to the object")
            bpy.context.selected_objects[0].scale = bpy.context.scene.saved_scale
            self.report(
                {'INFO'}, "Scale was pasted to the selected object.")
        return {'FINISHED'}

class OBJECT_OT_pizza_tool_select_material(bpy.types.Operator):
    """Select all objects with the same material"""
    bl_idname = "object.pizza_tool_select_material"
    bl_label = ""

    def execute(self, context):
        active_material_name = context.scene.allmaterials
        all_objects = context.selectable_objects
        selected_object_count = 0
        for object in all_objects:
            if(object.material_slots.find(active_material_name)!=-1):
                object.select_set(True)
                selected_object_count +=1
            else:
                pass
        if(selected_object_count >= 1):
            self.report(
                {'INFO'}, "Succesfully selected all objects by material: {}".format(active_material_name))
        else:
            self.report(
                {'INFO'}, "No objects found with the selected material.")           
        return {'FINISHED'}
    
class OBJECT_OT_pizza_tool_assign_material(bpy.types.Operator):
    """Assign Selected Material to All Selected Objects"""
    bl_idname = "object.pizza_tool_assign_material"
    bl_label = ""

    def execute(self,context):
        selected_material = context.scene.assign_material_allmaterials
        all_objects = context.selected_objects

        for obj in all_objects:
            #Check if object has material slot, if not, we create one
            if(len(obj.material_slots)<1):
                #Create material slot and assign the active_material
                obj.select_set(True)
                mat_index = bpy.data.materials.find(selected_material)
                obj.data.materials.append(bpy.data.materials[mat_index])
            else:
                #Check if the selected material isnt already in the object's material slots. If not, we add it
                if selected_material not in obj.material_slots:
                    obj.select_set(True)
                    mat_index = bpy.data.materials.find(selected_material)
                    obj.data.materials.append(bpy.data.materials[mat_index])
        self.report(
        {'INFO'}, "Succesfully added Material to All Selected Objects.")
        return {'FINISHED'}    

