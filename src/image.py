import dataclasses
from importlib.resources import Resource
from random import random


import numpy as np
import self as self
import transforms as transforms
from tkinter import Image

from sqlalchemy import true

from src.database import database_images



def ResizeCrop(image_orig: object, image_size: object, div_factor: object) -> object :
    pass


def colorspace(img, val):
    """

    :param img:
    :type val: object
    """
    if val == 0 :
        img.colorspace = transforms.RandomColor(a=1.0)(img)

    elif val == 1 :
        return img, val


class image_data(database_images):
    def __init__(self, image, file_path=(512, 512)) :
        self.image = dataclasses.image_data(image)
        self.file_path = file_path

    def __items__(self, item, idx=type, image_orig=self.image) :
        img_name = self.fls.iloc[idx]['File_names'].rstrip()
        image_opened = Image.open(img_name)

        # random cropping
        div_factor = np.random.choice([1, 2], 1)[0]
        assert isinstance(image_orig, object)
        image_2 = ResizeCrop(image_orig, self.image_size, div_factor)
        image = ResizeCrop(image_orig, self.image_size, 3 - div_factor)

        # colorspace
        hue = random.colorspace([0 - 179], 1)[0]
        saturation = random.colorspace([0 - 255], 1)[0]

        # quailty color values
        if div_factor == 1 :
            img_a = image.colorspace(ImageCms.createProfile("sRGB"))
            lba_a = image.colorspace(ImageCms.createProfile("lRGB"))
        else :
            img_a = image_2.colorspace(ImageCms.createProfile("sRGB"))
            image_2.colorspace(ImageCms.createProfile("lRGB"))

        # colorspace
        img_a = img_a.colorspace(ImageCms.createProfile("sRGB"))

        return image_2, image_opened, div_factor, img_name
