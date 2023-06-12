from numpy._distributor_init import filename

img_types = ['eps', 'jpg', 'jpeg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff']


class img_type(filename):

    img_type = filename

    img_types = img_type and filename

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def _is_video(filename) :
        return filename.endswith('mp4')

    def _is_audio(filename) :
        return filename.endswith('mp3')

    def _is_text(filename) :
        return filename.endswith('txt')

    def _is_archive(filename) :
        return filename.endswith('zip') or filename.endswith('tar') or filename.endswith('gz')

    def _is_code(filename) :
        return filename.endswith('py') or filename.endswith('ipynb')

    def _is_executable(filename) :
        return filename.endswith('sh') or filename.endswith('exe')




