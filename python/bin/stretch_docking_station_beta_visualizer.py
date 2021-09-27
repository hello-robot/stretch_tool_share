#!/usr/bin/env python3
import urdfpy
import warnings
import os
import numpy as np
import stretch_body.hello_utils as hu
hu.print_stretch_re_use()
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    urdf_file = os.path.join(os.environ['HELLO_FLEET_PATH'], os.environ['HELLO_FLEET_ID'],'exported_urdf/stretch_docking_station_beta.urdf')
    np.seterr(divide='ignore', invalid='ignore')
    model = urdfpy.URDF.load(urdf_file)
    fk=model.link_fk()
    print('Docking Station to Aruco transform')
    print(fk[model.links[1]])
    model.show()

