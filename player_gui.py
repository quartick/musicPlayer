# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("other_files/music.png"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playlistLabel = QtWidgets.QLabel(self.centralwidget)
        self.playlistLabel.setGeometry(QtCore.QRect(10, 44, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.playlistLabel.setFont(font)
        self.playlistLabel.setObjectName("playlistLabel")
        self.tracksLabel = QtWidgets.QLabel(self.centralwidget)
        self.tracksLabel.setGeometry(QtCore.QRect(10, 190, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tracksLabel.setFont(font)
        self.tracksLabel.setObjectName("tracksLabel")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(10, 10, 21, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setIcon(QIcon("other_files/play-prev.png"))
        self.previousButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.previousButton.setText("")
        self.previousButton.setObjectName("previousButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setGeometry(QtCore.QRect(40, 10, 21, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pauseButton.setAutoFillBackground(False)
        self.pauseButton.setIcon(QIcon("other_files/375.png"))
        self.pauseButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.pauseButton.setText("")
        self.pauseButton.setShortcut("")
        self.pauseButton.setCheckable(True)
        self.pauseButton.setChecked(False)
        self.pauseButton.setObjectName("pauseButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(70, 10, 21, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setIcon(QIcon("other_files/play-next-icon.png"))
        self.nextButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        self.songSlider.setGeometry(QtCore.QRect(100, 20, 611, 16))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setStyleSheet(
            """
            QSlider::groove:horizontal {
                border: 1px solid #565a5e;
                height: 10px;
                background: #eee;
                margin: 0px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: dark-grey;
                width: 24px;
                height: 8px;
                border-radius: 4px;
            }
            """
        )
        self.songSlider.setObjectName("songSlider")
        self.currentTrackLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentTrackLabel.setGeometry(QtCore.QRect(100, 6, 581, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTrackLabel.sizePolicy().hasHeightForWidth())
        self.currentTrackLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.currentTrackLabel.setFont(font)
        self.currentTrackLabel.setObjectName("currentTrackLabel")
        self.addTracksButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTracksButton.setGeometry(QtCore.QRect(10, 560, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.addTracksButton.setFont(font)
        self.addTracksButton.setText("")
        self.addTracksButton.setIcon(QIcon("other_files/add-music.png"))
        self.addTracksButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.addTracksButton.setObjectName("addTracksButton")
        self.trackTimerLabel = QtWidgets.QLabel(self.centralwidget)
        self.trackTimerLabel.setGeometry(QtCore.QRect(680, 6, 60, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackTimerLabel.sizePolicy().hasHeightForWidth())
        self.trackTimerLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.trackTimerLabel.setFont(font)
        self.trackTimerLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.trackTimerLabel.setObjectName("trackTimerLabel")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(740, 20, 41, 16))
        self.volumeSlider.setProperty("value", 99)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setStyleSheet(
            """
            QSlider::groove:horizontal {
                border: 1px solid #565a5e;
                height: 10px;
                background: #eee;
                margin: 0px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: dark-grey;
                width: 10px;
                height: 8px;
                border-radius: 4px;
            }
            """
        )
        self.volumeSlider.setObjectName("volumeSlider")
        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setGeometry(QtCore.QRect(720, 17, 21, 21))
        self.muteButton.setIcon(QIcon("other_files/Speaker3.png"))
        self.muteButton.setStyleSheet(
            '''
            QPushButton:hover {
            color: #002756;
            border-width: 0px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 0px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.muteButton.setText("")
        self.muteButton.setObjectName("muteButton")
        self.playlistListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.playlistListWidget.setGeometry(QtCore.QRect(10, 70, 781, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistListWidget.sizePolicy().hasHeightForWidth())
        self.playlistListWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.playlistListWidget.setFont(font)
        self.playlistListWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.playlistListWidget.setDragEnabled(True)
        self.playlistListWidget.setDragDropOverwriteMode(False)
        self.playlistListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.playlistListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.playlistListWidget.setIconSize(QtCore.QSize(0, 0))
        self.playlistListWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.playlistListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.playlistListWidget.setSelectionRectVisible(False)
        self.playlistListWidget.setObjectName("playlistListWidget")
        self.tracksListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.tracksListWidget.setGeometry(QtCore.QRect(10, 219, 780, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracksListWidget.sizePolicy().hasHeightForWidth())
        self.tracksListWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tracksListWidget.setFont(font)
        self.tracksListWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tracksListWidget.setAutoFillBackground(False)
        self.tracksListWidget.setDragEnabled(True)
        self.tracksListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tracksListWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tracksListWidget.setProperty("isWrapping", False)
        self.tracksListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.tracksListWidget.setWordWrap(False)
        self.tracksListWidget.setSelectionRectVisible(False)
        self.tracksListWidget.setObjectName("tracksListWidget")
        self.addPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPlaylistButton.setGeometry(QtCore.QRect(10, 160, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.addPlaylistButton.setFont(font)
        self.addPlaylistButton.setText("")
        self.addPlaylistButton.setIcon(QIcon("other_files/addPlaylist.png"))
        self.addPlaylistButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.addPlaylistButton.setObjectName("addPlaylistButton")
        self.deleteTrackButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteTrackButton.setGeometry(QtCore.QRect(40, 560, 21, 23))
        self.deleteTrackButton.setText("")
        self.deleteTrackButton.setIcon(QIcon("other_files/TrashIcon.png"))
        self.deleteTrackButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.deleteTrackButton.setObjectName("deleteTrackButton")
        self.deletePlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.deletePlaylistButton.setGeometry(QtCore.QRect(40, 160, 21, 23))
        self.deletePlaylistButton.setText("")
        self.deletePlaylistButton.setIcon(QIcon("other_files/TrashIcon.png"))
        self.deletePlaylistButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.deletePlaylistButton.setObjectName("deletePlaylistButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.playlistLabel.setText(_translate("MainWindow", "Плейлисты"))
        self.tracksLabel.setText(_translate("MainWindow", "Аудиозаписи"))
        self.pauseButton.setShortcut(_translate("MainWindow", "Space"))
        self.currentTrackLabel.setText(_translate("MainWindow", ""))
        self.trackTimerLabel.setText(_translate("MainWindow", ""))
        self.muteButton.setShortcut(_translate("MainWindow", "M"))


class Modal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowModality(Qt.WindowModal)
        # self.setModal(True)
        self.setObjectName("modalWindow")
        self.setWindowIcon(QIcon("other_files/music.png"))
        self.setWindowTitle("Playlist")
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(400, 600)
        self.setFixedSize(400, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tracksListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.tracksListWidget.setGeometry(QtCore.QRect(10, 30, 381, 531))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tracksListWidget.setFont(font)
        self.tracksListWidget.setAcceptDrops(True)
        self.tracksListWidget.setDragEnabled(True)
        self.tracksListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tracksListWidget.setObjectName("tracksListWidget")
        self.addTracksButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTracksButton.setGeometry(QtCore.QRect(10, 570, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.addTracksButton.setFont(font)
        self.addTracksButton.setText("")
        self.addTracksButton.setIcon(QIcon("other_files/add-music.png"))
        self.addTracksButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.addTracksButton.setObjectName("addTracksButton")
        self.deleteTrackButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteTrackButton.setGeometry(QtCore.QRect(40, 570, 21, 23))
        self.deleteTrackButton.setText("")
        self.deleteTrackButton.setIcon(QIcon("other_files/TrashIcon.png"))
        self.deleteTrackButton.setStyleSheet(
            '''
            QPushButton:hover {background-color: white;
            color: #002756;
            border-width: 1px;
            border-style: solid;}
            QPushButton:!hover {background-color: rgba(0, 0, 0, 00);
            border-width: 1px;
            border-style: solid;
            color: #000000;}
            '''
        )
        self.deleteTrackButton.setObjectName("deleteTrackButton")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 4, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(270, 4, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.countLabel.setFont(font)
        self.countLabel.setObjectName("countLabel")
