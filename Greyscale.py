import numpy as np
import imageio

def convert_to_grayscale(image_paths):
    grayscale_images = {}
    for image_path in image_paths:
        image = imageio.imread(image_path)
        grayscale = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        grayscale_images[image_path] = grayscale
    return grayscale_images


image_paths = [
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Pepaya.jpg",
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Singkong.jpg", 
    "C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Kenikir.jpg"
]

grayscale_images = convert_to_grayscale(image_paths)
for image_path, grayscale_image in grayscale_images.items():
    print(f"Gambar grayscale untuk {image_path}:")
    print(grayscale_image)