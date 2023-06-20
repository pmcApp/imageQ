from typing import Dict, Union, Any, Optional, Type

from sqlalchemy.testing import db

from src.image import image_data


def sort_values(by) :
    pass


class database_images(image_data) :
    db_images: Type[image_data.get('db_images')]

    def __init__(self, image, image_data=db.ImageData) :
        super().__init__(image, image_data)
        self.db_images = database_images

    def __repr__(self) :
        return f"{self.__class__.__name__}({self.image_data}, {self.image}, {self.file_path})"

    def db_images(self) -> dict[str, Union[Optional[str], Any]] :
        self.db_images = {
            'image_id': sort_values(by=['id']),
            'image_name': 'image_%s' % self.db_images[self.db_name],
            'image_path': 'image_%s' % self.db_images[self.db_path],
            'image_type': 'image_%s' % self.db_images[self.db_type],
            'image_size': 'image_%s' % self.db_images[self.db_size],
            'image_width': 'image_%s' % self.db_images[self.db_width],
            'image_height': 'image_%s' % self.db_images[self.db_height]
        }
        return self.db_images
