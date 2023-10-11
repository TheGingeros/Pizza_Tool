import bpy

#Functions for the allmaterials EnumProperty
def mat_update(self, context):
    pass
def getsets(self, context):
    sets = []
    mats = bpy.data.materials

    for mat in mats:
        sets.append((mat.name, mat.name, mat.name))
    if not sets:
        sets = [('None', 'None', 'None')]
    return sets