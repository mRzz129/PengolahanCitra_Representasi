import numpy as np
import matplotlib.pyplot as plt
from imageio import imread

def channel_blue(path_gambar1, path_gambar2, path_gambar3):
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))  

    for i, path in enumerate([path_gambar1, path_gambar2, path_gambar3]):
        gambar = imread(path)
        channel_blue = gambar[:, :, 2]
        axes[i].imshow(channel_blue, cmap='gray')
        axes[i].set_title(f"Channel Blue: {path}")

    plt.tight_layout()
    plt.show()

channel_blue('C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Pepaya.jpg', 'C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Singkong.jpg', 'C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\RepresentasiCitra_Mirza\\Gambar\\Kenikir.jpg')