import trimesh
import numpy as np
from PIL import Image

def depth_to_3d(depth_map_path, output_path="static/model.obj"):
    img = Image.open(depth_map_path).convert("L")
    img = img.resize((128, 128))
    depth_array = np.array(img) / 255.0  # Normalize depth

    verts = []
    faces = []
    
    for y in range(128):
        for x in range(128):
            z = depth_array[y, x]
            verts.append((x, y, z))

    # Make sure face indices stay within bounds
    for y in range(127):
        for x in range(127):
            i = y * 128 + x
            if i + 128 + 1 < len(verts):  # Ensure index exists
                faces.append((i, i + 128, i + 1))
                faces.append((i + 128, i + 128 + 1, i + 1))

    mesh = trimesh.Trimesh(vertices=verts, faces=faces, process=False)
    mesh.export(output_path)
    print(f"✅ 3D Model Saved: {output_path}")

# Example usage
depth_to_3d("static/depth_map.png")
