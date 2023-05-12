import os
import numpy as np
import argparse
import matplotlib.pyplot as plt

MAX_FILE_SIZE_BYTES = 10000000


def generate_image(input_filename, output_filename, image_width):
    file_size = os.path.getsize(input_filename)
    if file_size > MAX_FILE_SIZE_BYTES:
        raise ValueError(
            "Better leave big file for now...I do not want to choke your memory"
        )

    data = None
    image_width = (
        int(image_width)
        if image_width is not None
        else int(np.ceil(np.sqrt(file_size)))
    )
    image_len = int(np.ceil(file_size / image_width))
    np_data = np.zeros((image_len * image_width, 1))
    with open(input_filename, "rb") as ifile:
        data = ifile.read()
        for i, byte in enumerate(data):
            np_data[i] = int(byte)

    np_data = np.reshape(np_data, (image_len, image_width))
    plt.figure()
    plt.imshow(np_data, cmap="hot_r")
    plt.savefig(output_filename)
    print(f"Picture has width {image_width} and length {image_len}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="convert-bytes-to-image",
        description="Brutally convert a small file into colorful image",
        epilog="Quick and dirty, use for small files!",
    )
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    parser.add_argument("-iw", "--image-width", default=None)
    args = parser.parse_args()
    generate_image(
        input_filename=args.input,
        output_filename=args.output,
        image_width=args.image_width,
    )
