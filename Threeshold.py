import numpy as np
import imageio

def binarize_images(image_paths, threshold):
   
    binary_images = {}

    for image_path in image_paths:
        
        image = imageio.imread(image_path)

        gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

        binary = (gray > threshold).astype(float)

        binary_images[image_path] = binary

    return binary_images

image_paths = [
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Pepaya.jpg",
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Singkong.jpg", 
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Kenikir.jpg"
]

binary_images = binarize_images(image_paths, threshold=128)
for image_path, binary_image in binary_images.items():
    print(f"Gambar biner untuk {image_path}:")
    print(binary_image)