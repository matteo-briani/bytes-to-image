import os
import numpy as np
import argparse
import matplotlib.pyplot as plt

MAX_FILE_SIZE_BYTES = 10000

def generate_image(input_filename, output_filename):

    file_size = os.path.getsize(input_filename)
    if file_size > MAX_FILE_SIZE_BYTES:
        raise ValueError("Better leave big file for now...I do not want to choke your memory")

    data = None
    image_len = int(np.ceil(np.sqrt(file_size)))
    np_data = np.zeros( image_len ** 2)
    with open(input_filename,'rb') as ifile:
        data = ifile.read()
        for i, byte in enumerate(data):
            np_data[i] = int(byte)

    np_data.reshape((image_len, image_len))

    pixel_plot = plt.figure()
    pixel_plot.add_axes()
    pixel_plot = plt.imshow(np_data)
    plt.savefig(output_filename) 
    plt.show(pixel_plot)
    
    print(np_data)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='convert-bytes-to-image',
                    description='Brutally convert a small file into colorful image',
                    epilog='Quick and dirty, use for small files!')
    parser.add_argument('input_filename')
    parser.add_argument('output_filename')
    args = parser.parse_args()
    generate_image(input_filename=args.input_filename, output_filename=args.output_filename)
