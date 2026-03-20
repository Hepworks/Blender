import bpy

# --- CONFIGURATION ---
COLLECTION_NAME = "Imported_GPX_Paths"
MATERIAL_NAME = "GPX_Path_Material" # Ensure your material is named exactly this
# ---------------------

def link_material_to_collection():
    # Find the material
    mat = bpy.data.materials.get(MATERIAL_NAME)
    
    if not mat:
        print(f"Error: Material '{MATERIAL_NAME}' not found. Please rename your material first.")
        return

    # Find the collection
    if COLLECTION_NAME in bpy.data.collections:
        target_col = bpy.data.collections[COLLECTION_NAME]
        
        count = 0
        for obj in target_col.objects:
            if obj.type == 'CURVE':
                # Clear existing materials and add the new one
                obj.data.materials.clear()
                obj.data.materials.append(mat)
                count += 1
        
        print(f"Success: Linked '{MATERIAL_NAME}' to {count} paths.")
    else:
        print(f"Error: Collection '{COLLECTION_NAME}' not found.")

link_material_to_collection()