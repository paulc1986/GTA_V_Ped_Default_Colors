bl_info = {
    "name": "GTA V Colour Attributes",
    "blender": (2, 80, 0),
    "category": "Object",
    "version": (1, 0, 0),
    "author": "Your Name",
    "description": "Adds GTA V colour attributes to selected objects.",
    "location": "View3D > Tool",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY"
}

import bpy
from mathutils import Color

# Define the operator
class OBJECT_OT_add_ped_colours(bpy.types.Operator):
    bl_idname = "object.add_ped_colours"
    bl_label = "Set Default Ped Colours"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.object
        
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "No mesh object selected")
            return {'CANCELLED'}
        
        # Remove existing color attributes
        while obj.data.color_attributes:
            obj.data.color_attributes.remove(obj.data.color_attributes[0])
        
        # Adding color0 attribute
        color0 = obj.data.color_attributes.new(name="colour0", type='BYTE_COLOR', domain='CORNER')
        for poly in obj.data.polygons:
            for loop_index in poly.loop_indices:
                color0.data[loop_index].color = [1.0, 0.50196, 0.0, 1.0]  # Equivalent to hex color FF8000 and alpha 1.0

        # Adding color1 attribute
        color1 = obj.data.color_attributes.new(name="colour1", type='BYTE_COLOR', domain='CORNER')
        for poly in obj.data.polygons:
            for loop_index in poly.loop_indices:
                color1.data[loop_index].color = [0.0, 0.0, 0.0, 0.0]  # Equivalent to hex color 000000 and alpha 0.0

        self.report({'INFO'}, "Color attributes added")
        return {'FINISHED'}

# Panel to contain the button
class VIEW3D_PT_ped_colours(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_ped_colours"
    bl_label = "GTA V Colour Attributes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'  # Default category

    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_ped_colours")

# Register and Unregister the classes
def register():
    bpy.utils.register_class(OBJECT_OT_add_ped_colours)
    bpy.utils.register_class(VIEW3D_PT_ped_colours)

    # Place in the Sollumz Tools tab if it exists
    if 'Sollumz_Tools' in dir(bpy.types):
        VIEW3D_PT_ped_colours.bl_category = 'Sollumz Tools'

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_ped_colours)
    bpy.utils.unregister_class(VIEW3D_PT_ped_colours)

if __name__ == "__main__":
    register()
