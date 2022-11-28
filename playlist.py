"""
Модуль плелиста, наследуемый от LinkedList для работы с композициями
"""
from linked_list import *
from pygame import mixer
from composition import Composition


class Playlist(LinkedList):
    """
    Класс плейлист
    """
    def __init__(self, current_track: LinkedListItem = None, name: str = None):
        """
        Конструктор класса
        :param current_track: Нынешний трек
        :param name: Название плейлиста
        """
        super().__init__()
        self.name: str = name
        self.current_track: LinkedListItem = current_track

    @staticmethod
    def play_all(path: str):
        """
        Проигрывание музыкальной композиции
        :param path: Путь к файлу
        """
        mixer.music.load(path)
        mixer.music.play()

    def next_track(self):
        """
        Текущий трек принимает ссылку следующего трека
        """
        self.current_track: object = self.current_track.next_item

    def previous_track(self):
        """
        Нынешний трек принимает ссылку предыдущего трека
        """
        self.current_track: object = self.current_track.previous_item

    def add_track(self, path: str):
        """
        Добавление трека
        :param path: Путь к файлу
        """
        self.append(Composition(path))
        self.current_track = self.first_item

    def switch_tracks(self, is_up=False):
        """
        Перестановка треков местами
        :param is_up: Перестановка выше или ниже по порядку
        """
        tmp_track_data: object = self.current_track.data
        if is_up:
            self.current_track.data = self.current_track.previous_item.data
            self.current_track.previous_item.data = tmp_track_data
        else:
            self.current_track.data = self.current_track.next_item.data
            self.current_track.next_item.data = tmp_track_data

    def delete_track(self):
        """
        Удаление трека
        """
        temp = self.current_track
        self.remove(self.current_track.data)
        self.current_track = temp
        self.next_track()

    def find_track(self, num):
        """
        Метод для нахождения узна по померу песни
        @param num: номер песни
        @return: узел с песней
        """
        for temp in self:
            if temp.data.num == str(num):
                return temp
        return self.head

    def current(self):
        """
        Получение текущего трека
        @return: текущий трек
        """
        return self.current_track
