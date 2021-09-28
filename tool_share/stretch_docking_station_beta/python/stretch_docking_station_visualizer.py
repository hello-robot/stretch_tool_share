#!/usr/bin/env python3
import warnings
import os
import numpy as np
import stretch_body.hello_utils as hu
hu.print_stretch_re_use()
warnings.filterwarnings("ignore")
import urdfpy
import pyrender

def show(urdf):
    """
        Hack to color Aruco. Need to create DAE to apply texture/color.
    """
    fk = urdf.visual_trimesh_fk(cfg=None)
    scene = pyrender.Scene()
    nodes = []
    idx=0
    for tm in fk:
        pose = fk[tm]
        if (idx==1):
            tm.visual.vertex_colors = np.random.uniform(size=tm.vertices.shape)
            tm.visual.face_colors = np.random.uniform(size=tm.faces.shape)
        idx=idx+1
        mesh = pyrender.Mesh.from_trimesh(tm, smooth=False)
        mesh_node = scene.add(mesh, pose=pose)
        nodes.append(mesh_node)
    viewer = pyrender.Viewer(scene, run_in_thread=True, use_raymond_lighting=True)


if __name__ == "__main__":
    urdf_file = os.path.join(os.environ['HELLO_FLEET_PATH'], os.environ['HELLO_FLEET_ID'],'exported_urdf/stretch_docking_station_description.urdf')
    np.seterr(divide='ignore', invalid='ignore')
    model = urdfpy.URDF.load(urdf_file)
    fk=model.link_fk()
    print('Docking Station to Aruco transform')
    print(fk[model.links[1]])
    show(model)

