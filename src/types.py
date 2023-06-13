from numpy._distributor_init import filename

img_types = ['eps', 'jpg', 'jpeg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff']


class img_type(filename):

    img_type = filename

    img_types = img_type and filename

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def _is_jpg(filename) :
        return filename.endswith('jpg')

    def _is_png(filename) :
        return filename.endswith('png')

    def _is_svg(filename) :
        return filename.endswith('svg')

    def _is_archive(filename) :
        return filename.endswith('zip') or filename.endswith('tar') or filename.endswith('gz')




