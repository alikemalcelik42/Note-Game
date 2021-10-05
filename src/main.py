from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os, random


class Window(QWidget):
    def __init__(self, title, shape, icon):
        super().__init__()
        self.title = title
        self.x, self.y, self.w, self.h = shape
        self.icon = QIcon(icon)
        self.vbox = QVBoxLayout()
        self.notesPath = ".\\img\\notes\\"
        self.notes = {
            "{}1.png".format(self.notesPath): "mi",
            "{}2.png".format(self.notesPath): "fa",
            "{}3.png".format(self.notesPath): "sol",
            "{}4.png".format(self.notesPath): "la",
            "{}5.png".format(self.notesPath): "si",
            "{}6.png".format(self.notesPath): "do",
            "{}7.png".format(self.notesPath): "re",
            "{}8.png".format(self.notesPath): "mi",
            "{}9.png".format(self.notesPath): "fa",
        }
        self.initUI()
        self.setLayout(self.vbox)
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.fileLabel = QLabel()
        self.fileLabel.setAlignment(Qt.AlignCenter)
        self.file = self.LoadFile()

        self.vbox.addWidget(self.fileLabel)

        self.noteNameText = QLineEdit()
        self.vbox.addWidget(self.noteNameText)

        self.sendBtn = QPushButton("Gönder", clicked = lambda : self.CheckNote(self.file))
        self.vbox.addWidget(self.sendBtn)

    def LoadFile(self, beforeFile=""):
        file = self.GetRandomNote(beforeFile)
        self.filePixmap = QPixmap(file)
        self.fileLabel.setPixmap(self.filePixmap)
        return file

    def CheckNote(self, file):
        answer = self.noteNameText.text().strip()
        result = self.notes[file]
        if answer == result:
            QMessageBox.information(self, "Doğru", "Cevabınız doğru!")
            self.file = self.LoadFile(file)
        else:
            QMessageBox.warning(self, "Yanlış", "Cevabınız yanlış!")

    def GetRandomNote(self, beforeFile=""):
        files = []

        for file in os.listdir(self.notesPath):
            if file == beforeFile:
                continue
            files.append(file)

        randomFile = random.choice(files)
        return os.path.join(self.notesPath, randomFile)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window("Note Game", (100, 100, 0, 0), "./img/icon.jpg")
    app.exec_()