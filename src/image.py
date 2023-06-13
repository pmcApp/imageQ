import dataclasses
from importlib.resources import Resource
from random import random

import Dataset as Dataset
import Rectangle as Rectangle
import numpy as np
import self as self
import transforms as transforms
from tkinter import Image

from sqlalchemy import true


def ResizeCrop(image_orig: object, image_size: object, div_factor: object) -> object :
    pass

def colorspace(img, val) :
    if val == 0 :
        img.colorspace = transforms.RandomColor(a=1.0)(img)

    elif val == 1 :
        img_a = img.colorspace(ImageCms.createProfile("sRGB"))
        lba_a = img.colorspace(ImageCms.createProfile("lRGB"))


class image_data(Dataset) :
    def __init__(self, image, file_path=(512, 512)) :
        self.image = dataclasses.image_data(image)
        self.file_path = file_path

    def __items__(self, item, idx=type, image_orig=self.image):
        img_name = self.fls.iloc[idx]['File_names'].rstrip()
        image_opened = Image.open(img_name)

        # random cropping
        div_factor = np.random.choice([1, 2], 1)[0]
        assert isinstance(image_orig, object)
        image_2 = ResizeCrop(image_orig, self.image_size, div_factor)
        image = ResizeCrop(image_orig, self.image_size, 3 - div_factor)

        # colorspace
        colorspace_factor = np.random.choice([0 - 179], 1)[0]
        colorspace_saturation = random.choice([0 - 255], 1)[0]

        return image_2, image_opened, div_factor, img_name
