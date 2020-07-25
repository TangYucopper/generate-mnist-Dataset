import cv2 as cv
import numpy as np

if __name__ == '__main__':
    # Open the file
    file_name, folder_name = 'train-images.idx3-ubyte', './mnist_training/'
    file_name, folder_name = 't10k-images.idx3-ubyte', './mnist_test/'
    with open(file_name, 'rb') as file:
        # Get the first four fields
        file.read(4)
        num_images = int.from_bytes(file.read(4), byteorder='big', signed=False)
        num_rows = int.from_bytes(file.read(4), byteorder='big', signed=False)
        num_cols = int.from_bytes(file.read(4), byteorder='big', signed=False)
        
        # Generate the corresponding image
        gen_image = np.empty((num_rows, num_cols), dtype=np.uint8)

        # Generate num_images images
        for image_index in range(num_images):
            for row in range(num_rows):
                for col in range(num_cols):
                    gen_image[row][col] = int.from_bytes(file.read(1), byteorder='big', signed=False)
                    # finish generating gen_image here
            # store the gen_image
            cv.imwrite(folder_name + '{:0>5d}.png'.format(image_index), gen_image)