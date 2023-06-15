from src.image import image_data


def sort_values(by) :
    pass


class database_images(image_data) :
    def __init__(self, image, file_path=(512, 512)) :
        super().__init__(image, file_path)
        self.db_images = None

    def db_images(self) :
        self.db_images = {
            'image_id' : sort_values(by=['id']),
            'image_name' : 'image_name',
            'image_path' : 'image_path',
            'image_type' : 'image_type',
            'image_size' : 'image_size',
            'image_width' : 'image_width',
            'image_height' : 'image_height'
        }
        return self.db_images
