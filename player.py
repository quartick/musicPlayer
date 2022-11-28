"""
Модуль плеера, связывающего графическую и
функицональную состоявляющие воедино.

"""

import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from pathlib import Path
import os
import shutil
import json
from player_gui import Ui_MainWindow, Modal
from PyQt5.QtCore import QTimer

from PyQt5 import QtWidgets

from pygame import mixer

from playlist import Playlist

mixer.init()


class Player(Ui_MainWindow):
    """
    Класс, позвооляющий взаимодействовать с графическим интерфейсом
    """

    def __init__(self):
        """
        Конструктор класс
        """

        self.playlist_array: list = list()
        self.playlist = None
        self.playing_track = None
        self.playing_playlist = None
        self.is_music_playing: bool = False
        self.is_track_initialized: bool = False
        self.is_track_muted: bool = False
        self.temp_volume: int = 99

        self.app = QtWidgets.QApplication(sys.argv)
        self.GenerateWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.modal = Modal()
        self.ui.setupUi(self.GenerateWindow)
        self.GenerateWindow.show()

        self.ui.pauseButton.clicked.connect(self.start_stop_song)
        self.ui.previousButton.clicked.connect(self.previous)
        self.ui.nextButton.clicked.connect(self.next)
        self.ui.addTracksButton.clicked.connect(self.add_track)
        self.modal.addTracksButton.clicked.connect(self.add_track)
        self.ui.tracksListWidget.itemClicked.connect(self.set_clicked_track_as_current_track)
        self.ui.tracksListWidget.itemDoubleClicked.connect(self.track_init)
        self.modal.tracksListWidget.itemClicked.connect(self.set_clicked_track_as_current_track_for_modal)
        self.modal.tracksListWidget.itemDoubleClicked.connect(self.track_init)
        self.modal.tracksListWidget.dropEvent = self.modalDropEvent
        self.ui.tracksListWidget.dropEvent = self.dropEvent
        self.ui.deleteTrackButton.clicked.connect(self.delete_track)
        self.modal.deleteTrackButton.clicked.connect(self.delete_track)
        self.ui.addPlaylistButton.clicked.connect(self.add_playlist)
        self.ui.deletePlaylistButton.clicked.connect(self.delete_playlist)
        self.ui.playlistListWidget.itemClicked.connect(self.set_clicked_playlist_as_current_playlist)
        self.ui.playlistListWidget.itemDoubleClicked.connect(self.open)
        self.ui.volumeSlider.sliderMoved.connect(self.volume_change)
        self.ui.muteButton.clicked.connect(self.mute)

        self.make_playlist_with_existing_data()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_track_progress)

        self.app.exec_()
        self.save_data()
        sys.exit()

    def start_stop_song(self):
        """
        Проигрывание трека при инициализации. Пауза, если трек проинициализирован
        """
        if not self.is_music_playing and self.is_track_initialized:
            self.unpause()
        elif not self.is_music_playing and not self.is_track_initialized:
            self.track_init()
            self.is_track_initialized = True
        else:
            self.pause()

    def dropEvent(self, event):
        """
        Переопределение метода dropEvent для корректной работы перемещения треков
        :param event: Перемещение
        """
        self.playlist = self.playlist_array[0]
        self.modal.close()
        insert_pos = event.pos()
        from_list = event.source()
        insert_index = from_list.row(self.ui.tracksListWidget.itemAt(insert_pos))
        drop_index = self.ui.tracksListWidget.currentRow()
        self.playlist[insert_index].data, self.playlist[drop_index].data = \
            self.playlist[drop_index].data, self.playlist[insert_index].data
        if self.playing_track == self.playlist[insert_index]:
            self.playlist.current_track = self.playlist[drop_index]
            self.playing_track = self.playlist[drop_index]
        elif self.playing_track == self.playlist[drop_index]:
            self.playlist.current_track = self.playlist[insert_index]
            self.playing_track = self.playlist[insert_index]
        self.update_track_list()
        self.set_current_row()

    def modalDropEvent(self, event):
        """
        Переопределение метода dropEvent для корректной работы перемещения треков
        :param event: Перемещение
        """
        insert_pos = event.pos()
        from_list = event.source()
        insert_index = from_list.row(self.modal.tracksListWidget.itemAt(insert_pos))
        drop_index = self.modal.tracksListWidget.currentRow()
        self.playlist[insert_index].data, self.playlist[drop_index].data = \
            self.playlist[drop_index].data, self.playlist[insert_index].data
        if self.playing_track == self.playlist[insert_index]:
            self.playlist.current_track = self.playlist[drop_index]
            self.playing_track = self.playlist[drop_index]
        elif self.playing_track == self.playlist[drop_index]:
            self.playlist.current_track = self.playlist[insert_index]
            self.playing_track = self.playlist[insert_index]
        self.update_track_list()
        self.set_current_row()

    def open(self):
        """
        Метод открытие модального окна плейлиста
        """
        self.modal.close()
        self.modal.nameLabel.setText('%s' % self.playlist.name)
        self.modal.countLabel.setText('%d треков' % self.playlist.length)
        self.update_track_list()
        self.modal.show()

    def track_init(self):
        """
        Инициализация трека
        """
        if self.is_current_track_not_none("Не удается воспроизвести текущий трек"):
            self.set_current_row()
            self.timer.start()
            self.playing_track = self.playlist.current_track
            self.playing_playlist = self.playlist
            if self.playing_track.data.image:
                self.ui.imageLabel.setPixmap(QPixmap(self.playing_track.data.image).scaled(28, 28))
            else:
                self.ui.imageLabel.setPixmap(QPixmap("other_files/unnamed.png").scaled(28, 28))
            if self.playing_track.data.title:
                self.ui.currentTrackLabel.setText(self.playing_track.data.title)
            else:
                self.ui.currentTrackLabel.setText(self.playing_track.data.name)
            if self.playing_track.data.artist:
                self.ui.authorLabel.setText(self.playing_track.data.artist)
            else:
                self.ui.authorLabel.setText("Неизвестен")
            # self.ui.currentTrackLabel.setText(self.playlist.current_track.data.name)
            self.ui.songSlider.setRange(0, self.playlist.current_track.data.duration)
            audio_path: str = self.playlist.current_track.data.path
            self.playlist.play_all(audio_path)
            self.is_music_playing: bool = True
            self.is_track_initialized: bool = True
            self.ui.pauseButton.setIcon(QIcon("other_files/16427.png"))

    def previous(self):
        """
        Обработчик нажатия кнопки previous
        Переключает на предыдущий трек
        """
        if self.is_current_track_not_none("Не удается воспроизвести предыдущий трек"):
            self.playlist.previous_track()
            # self.set_current_row()
            self.track_init()

    def next(self):
        """
        Обработчик нажатия кнопки next
        Переключает на следующий трек
        """
        if self.is_current_track_not_none("Не удается воспроизвести следующий трек"):
            self.playlist.next_track()
            # self.set_current_row()
            self.track_init()

    def set_current_row(self):
        """
        Установка нынешней строки для отображения на пользовательском интерфейсе
        """
        for i in range(self.ui.tracksListWidget.count()):
            if self.playlist.current_track.data.name == self.ui.tracksListWidget.item(i).text():
                self.ui.tracksListWidget.setCurrentRow(i)

    def pause(self):
        """
        Остановка трека
        """
        if self.is_current_track_not_none("Не удается воспроизвести текущий трек"):
            mixer.music.pause()
            self.is_music_playing = False
            self.ui.pauseButton.setIcon(QIcon("other_files/375.png"))

    @staticmethod
    def get_time(time: int) -> str:
        """
        Получение времени трека
        :param time: Полное время трека в секундах
        :return: Время трека (минуты:секунды)
        """
        minutes = str(time // 60)
        seconds = str(round(time % 60))
        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(seconds) == 1:
            seconds = "0" + seconds
        return minutes + ":" + seconds

    def update_track_progress(self):
        """
        Вывод на интерфейс времни
        """
        if self.playing_playlist.current_track is not None:
            seconds = mixer.music.get_pos() // 1000
            self.ui.trackTimerLabel.setText(self.get_time(seconds))
            self.ui.songSlider.setValue(seconds)
            if seconds >= self.playing_playlist.current_track.data.duration:
                self.next()

    def mute(self):
        """
        Заглушить/разглушить звук трека
        """
        if not self.is_track_muted:
            self.temp_volume = self.ui.volumeSlider.value()
            self.ui.volumeSlider.setValue(0)
            mixer.music.set_volume(0)
            self.ui.muteButton.setIcon(QIcon("other_files/mute.png"))
            self.is_track_muted = True
        else:
            self.ui.volumeSlider.setValue(self.temp_volume)
            self.volume_change(self.temp_volume)
            self.is_track_muted = False

    def volume_change(self, volume):
        """
        Изменение громкости трека
        :param volume: изменяемое значение громкости
        """
        if 67 <= volume < 100:
            self.ui.muteButton.setIcon(QIcon("other_files/Speaker3.png"))
            self.is_track_muted = False
        elif 33 <= volume < 67:
            self.ui.muteButton.setIcon(QIcon("other_files/Speaker2.png"))
            self.is_track_muted = False
        elif 1 <= volume < 33:
            self.ui.muteButton.setIcon(QIcon("other_files/Speaker1.png"))
            self.is_track_muted = False
        elif volume == 0:
            self.ui.muteButton.setIcon(QIcon("other_files/mute.png"))
            self.is_track_muted = True
        mixer.music.set_volume(volume)

    def unpause(self):
        """
        Снятие трека с паузы
        """
        if self.is_current_track_not_none("Не удается воспроизвести текущий трек"):
            mixer.music.unpause()
            self.is_music_playing = True
            self.ui.pauseButton.setIcon(QIcon("other_files/16427.png"))

    def add_track(self):
        """
        Добавление трека
        """
        directory_path = "../musicPlayer/music/"
        file_path = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл", ".", "Sound Files (*.mp3)")[0]
        if file_path != '':
            if directory_path[2:] not in file_path:
                shutil.copy(file_path, directory_path)
            file_path = directory_path + file_path.split('/')[-1]
            if self.playlist is not None:
                if file_path not in self.playlist.__str__():
                    self.playlist.add_track(file_path)
                else:
                    self.message_box("Такой файл уже есть", "Выберите другой")
            else:
                self.playlist = Playlist(name='')
                self.playlist_array.append(self.playlist)
                self.playlist.add_track(file_path)
            self.update_track_list()

    def update_track_list(self):
        """
        Обновление списка песен
        """
        if self.playlist.name == '':
            self.ui.tracksListWidget.clear()
            for track in self.playlist:
                self.ui.tracksListWidget.addItem(track.data.name)
        else:
            self.modal.tracksListWidget.clear()
            for track in self.playlist:
                self.modal.tracksListWidget.addItem(track.data.name)
                self.modal.countLabel.setText('%d треков' % self.playlist.length)

    def set_clicked_track_as_current_track(self, item: object):
        """
        Установка выбранного трека как нанешнего
        :param item: Выбранный трек
        """
        self.playlist = self.playlist_array[0]
        self.modal.close()
        for track in self.playlist:
            if track.data.name == item.text():
                self.playlist.current_track = track
                self.is_track_initialized = False

    def set_clicked_track_as_current_track_for_modal(self, item: object):
        """
        Установка выбранного трека как нанешнего
        :param item: Выбранный трек
        """
        for track in self.playlist:
            if track.data.name == item.text():
                self.playlist.current_track = track
                self.is_track_initialized = False

    def delete_track(self):
        """
        Удаление трека
        """
        if self.is_current_track_not_none("Нечего удалять"):
            if self.playlist.current_track == self.playing_track:
                self.playlist.delete_track()
                if self.playlist.length > 0:
                    self.track_init()
                else:
                    self.playlist.current_track = None
                    self.ui.pauseButton.setIcon(QIcon("other_files/375.png"))
                    self.ui.currentTrackLabel.setText('')
                    self.ui.authorLabel.setText('')
                    self.ui.imageLabel.setPixmap(QPixmap(''))
                    self.ui.trackTimerLabel.setText('')
                    self.ui.songSlider.setValue(0)
                    self.is_track_initialized = False
                    mixer.music.stop()
            else:
                if self.playlist.length > 0:
                    self.playlist.delete_track()
                if self.playlist.length == 0:
                    self.playlist.current_track = None
                    self.ui.currentTrackLabel.setText('')
                    self.ui.authorLabel.setText('')
                    self.ui.imageLabel.setPixmap(QPixmap(''))
                    self.ui.trackTimerLabel.setText('')
                    self.ui.songSlider.setValue(0)
                    self.is_track_initialized = False
                    mixer.music.stop()
            self.update_track_list()
            self.set_current_row()

    @staticmethod
    def message_box(text: str, informative_text: str):
        """
        Сообщение об ошибке
        :param text: Заголовок
        :param informative_text: Сообщение, описывающее ошибку
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setWindowTitle("Music Player")
        msg.setWindowIcon(QIcon("other_files/music.png"))
        msg.exec_()

    @staticmethod
    def input_box():
        """
        Окно ввода
        """
        msg = QInputDialog()
        msg.setWindowIcon(QIcon("other_files/music.png"))
        text, ok = QInputDialog.getText(msg, 'Music Player', 'Введите название плейлиста:')
        if ok:
            # msg.exec_()
            return text

    def add_playlist(self):
        """
        Добавление плейлиста
        """
        playlist_name = self.input_box()
        if playlist_name:
            if not (playlist_name in [playlist.name for playlist in self.playlist_array]):
                new_playlist = Playlist(name=playlist_name)
                self.playlist_array.append(new_playlist)
                self.update_playlist_menu()
                # self.playlist = new_playlist
            else:
                self.message_box("Плейлист с таким названием уже есть", "Введите другое название")
        else:
            self.message_box("Введена пустая строка", "Напишите название плейлиста")

    def update_playlist_menu(self):
        """
        Обновление списка плейлистов
        """
        self.ui.playlistListWidget.clear()
        for i in self.playlist_array[1:]:
            self.ui.playlistListWidget.addItem(i.name)

    def delete_playlist(self):
        """
        Удаление плейлиста
        """
        if self.playlist_array[1:]:
            if self.playlist is not None and self.playlist.name != '':
                if self.playlist.name == self.modal.nameLabel.text():
                    self.modal.close()
                self.playlist_array.remove(self.playlist)
                if self.playing_playlist is not None:
                    self.playlist = self.playing_playlist
                else:
                    self.playlist = None

                self.update_playlist_menu()
            else:
                self.message_box("Нечего удалять", "Не выбран плейлист")
        else:
            self.message_box("Нечего удалять", "Список плейлистов пустой")

    def set_clicked_playlist_as_current_playlist(self, item: object):
        """
        Установка выбранного плейлиста как нынешнего
        :param item: Выбранный плейлист
        """
        for playlist in self.playlist_array:
            if playlist.name == item.text():
                self.playlist = playlist
                if not self.is_music_playing:
                    self.is_track_initialized = False

    def is_current_track_not_none(self, text: str) -> bool:
        """
        Проверка наличия нынешнего трека
        :param text: Сообщение описывающее ошибку
        :return: Наличие ошибки
        """
        if self.playlist.current_track is None:
            self.message_box(text, "Добавьте песню")
            return False
        return True

    def make_playlist_with_existing_data(self):
        """
        Создание плейлистов с существующими данными
        """
        data = self.read_data_from_json()
        for playlist in data:
            name = playlist['name']
            new_playlist = Playlist(name=name)
            for song in playlist['tracks']:
                new_playlist.add_track(song)
            if name != '':
                self.playlist_array.append(new_playlist)
            else:
                self.playlist = new_playlist
                self.playlist_array.append(new_playlist)
                self.update_track_list()
        self.update_playlist_menu()
        self.ui.tracksListWidget.setCurrentRow(0)

    def write_data_in_json(self):
        """
        Запись данных в файл json
        """
        data = []
        if len(self.playlist_array) > 0:
            for item in self.playlist_array:
                tracks = []
                current_track = item.head
                for i in range(item.length):
                    tracks.append(current_track.data.path)
                    current_track = current_track.next_item

                data.append({
                    'name': item.name,
                    'tracks': tracks
                })
        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

    def save_data(self):
        """
        Сохранение данных перед выходом
        """
        self.write_data_in_json()

    @staticmethod
    def read_data_from_json() -> list:
        """
        Чтение данных из файла json
        :return:
        """
        data = None
        if not os.stat('data.json').st_size == 0:
            dir_path = Path.cwd()
            path = Path(dir_path, 'data.json')
            with open(path, encoding="utf-8") as outfile:
                data = json.load(outfile)
        return data
