from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
import sys


class Main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        self.widget = QWidget()
        self.testBtn = QtWidgets.QPushButton(self.widget)
        self.testBtn.setText("Test")
        self.testBtn.clicked.connect(self.open)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.widget)
        self.setLayout(self.vbox)

    def open(self):
        self.app2 = Modal()
        self.app2.show()


class Modal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowModality(Qt.WindowModal)
        # self.setModal(True)
        self.setObjectName("MainWindow")
        self.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 381, 531))
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setObjectName("tracksListWidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 570, 21, 23))
        self.addButton.setObjectName("addTracksButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(40, 570, 21, 23))
        self.deleteButton.setObjectName("deleteTrackButton")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 4, 251, 21))
        self.nameLabel.setObjectName("nameLabel")
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(270, 4, 121, 21))
        self.countLabel.setObjectName("countLabel")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()

    sys.exit(app.exec_())