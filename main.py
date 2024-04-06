import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
    filter = np.asarray(Image.open("data/filter.png"))
    img = np.asarray(Image.open("data/dog.jpg"))

    print(filter)

    blurred = cv2.filter2D(img, -1, filter / filter.sum())

    plt.imshow(blurred)
    plt.show()
    # plt.imshow(filter)
    # plt.show()

if __name__ == '__main__':
    main()