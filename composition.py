"""
Модуль, представляющий собой класс композиции (трека)
"""

from pygame import mixer
# Модуль для сбора метаданных трека
from tinytag import TinyTag


class Composition:
    """
    Класс музыкальная композиция
    """
    def __init__(self, path: str):
        """
        Конструктор класса
        :param path: Путь до файла
        """

        tinytag = TinyTag.get(path, image=True)
        self.path: str = path
        self.artist = tinytag.artist
        self.album = tinytag.album
        self.title = tinytag.title
        # self.duration: int = int(mixer.Sound(path).get_length())
        self.duration = int(tinytag.duration)
        self.image = tinytag.get_image()
        self.name: str = path.split('/')[-1][0:-4]
        if not self.artist:
            self.artist = "Неизвестен"
        if not self.title:
            self.title = self.name


        if self.image:
            if self.title and self.artist:
                with open(f"other_files/tracks_images/{self.artist.replace('/', ' ')}"
                          f" - {self.title.replace('/', ' ')}.jpeg", "wb") as image_file:
                    image_file.write(self.image)
                    self.image = f"other_files/tracks_images/" \
                                 f"{self.artist.replace('/', ' ')} - {self.title.replace('/', ' ')}.jpeg"
            else:
                with open(f"other_files/tracks_images/{self.name}.jpeg", "wb") as image_file:
                    image_file.write(self.image)
                    self.image = f"other_files/tracks_images/{self.name}.jpeg"

    def __str__(self) -> str:
        """
        Информация об объекте класса
        :return: Строка с информацией
        """
        return f"Название: {self.name}; Путь: {self.path}; Длительность: {self.duration}"

    def __repr__(self) -> str:
        """
        Информация об объекте класса
        :return: Строка с информацией
        """
        return f"Название: {self.name}; Путь: {self.path}; Длительность: {self.duration}"
