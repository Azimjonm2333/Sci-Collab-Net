from io import BytesIO
from urllib.request import urlopen
from PIL import Image as PILImage
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile


def validate_image_url(url: str):
    try:
        response = urlopen(url)
        if response.headers.get('Content-Type', '').startswith('image'):
            return True
    except Exception:
        pass
    raise ValidationError("Ваш url не имеет отношения к изображения")


def create_thumbnail(image):
    if image:
        # Открываем оригинальное изображение
        img = PILImage.open(image)

        # Создаем миниатюру
        thumbnail_size = (100, 100)  # Размер миниатюры (в пикселях)
        img.thumbnail(thumbnail_size)

        # Создаем буфер для временного хранения миниатюры
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG')

        # Создаем файл для миниатюры и сохраняем его
        thumb_file = InMemoryUploadedFile(
            thumb_io, None, f'{image.name.split(".")[0]}_thumbnail.jpg', 'image/jpeg',
            thumb_io.tell(), None
        )
        return thumb_file
    return None
