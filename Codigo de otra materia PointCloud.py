# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:54:14 2019

@author: John
"""

# examples/Python/Basic/rgbd_redwood.py

from open3d import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
    color_raw = read_image( "C:/Users/John/Downloads/JHON/RGB.png")
    depth_raw = read_image("C:/Users/John/Downloads/JHON/DepthOriginal.png")
    rgbd_image = create_rgbd_image_from_color_and_depth(
        color_raw, depth_raw);
    print(rgbd_image)
    
    pinhole_camera_intrinsic = PinholeCameraIntrinsic(720, 1280, 863.889,463.889,620.0, 240.0)
    
    intrinsic = np.array([[463.889,0,320],[0,463.889,240],[0,0,1]])   
    plt.subplot(1, 2, 1)
    plt.title('grayscale image')
    plt.imshow(rgbd_image.color)
    plt.subplot(1, 2, 2)
    plt.title('depth image')
    plt.imshow(rgbd_image.depth)
    plt.show()
    
    pcd = create_point_cloud_from_rgbd_image(rgbd_image, pinhole_camera_intrinsic)
    create_rgbd_image_from_color_and_depth(rgbd_image.color, rgbd_image.depth,
                convert_rgb_to_intensity = False)
    
    print( camera.PinholeCameraIntrinsic(
            camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault).intrinsic_matrix)
    
    print('mu', intrinsic)
    
    #print(PinholeCameraIntrinsicParameters.PrimeSenseDefault())
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    draw_geometries([pcd])