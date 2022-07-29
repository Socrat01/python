#подключаем библиотеки
from aifc import Error

from PIL import Image
import PIL
import os
import glob
#сканируем все файлы в директории
files = glob.glob("/Users/macbook/PycharmProjects/petsproject/final/*/*")
#выводим все файлы
print(f"Все файлы в директории {files}")
#отсеиваем только в формате jpg и png
images = [file for file in files if file.endswith('webp')]
print(f"Все файлы с форматом jpg и png {images}")

def convert_image(image_path, image_type):
    # сам процесс конвертации
    im = Image.open(image_path)
    im = im.convert('RGB')
    #здесь мы можем указать приписку к имени файла в кавычках
    image_name = image_path.split('.')[0]
    print(f"Это имя нового файла: {image_name}")

    #сохраняем в новый формат webp
    if image_type == 'webp':
        im.save(f"{image_name}.png", 'png')
    else:
        #если не нашел файлов нужного нам формата - выдаст ошибку
        raise Error
for image in images:
    if image.endswith('webp'):
        convert_image(image, image_type='webp')
    else:
        raise Error
print(f"Finish🟢")