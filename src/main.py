from ast import NodeTransformer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random

class Window(QWidget):
    def __init__(self, title, shape, icon):
        super().__init__()
        self.title = title
        self.x, self.y, self.w, self.h = shape
        self.icon = QIcon(icon)
        self.vbox = QVBoxLayout()
        self.notesPath = ".\\img\\notes\\"
        self.notes = {
            "{}1.png".format(self.notesPath): "kalın mi",
            "{}2.png".format(self.notesPath): "kalın fa",
            "{}3.png".format(self.notesPath): "sol",
            "{}4.png".format(self.notesPath): "la",
            "{}5.png".format(self.notesPath): "si",
            "{}6.png".format(self.notesPath): "do",
            "{}7.png".format(self.notesPath): "re",
            "{}8.png".format(self.notesPath): "ince mi",
            "{}9.png".format(self.notesPath): "ince fa",
        }
        self.initUI()
        self.setLayout(self.vbox)
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.firstChoiceBtn = QPushButton()
        self.secondChoiceBtn = QPushButton()
        self.thirdChoiceBtn = QPushButton()
        self.fourthChoiceBtn = QPushButton()
        self.choiceBtns = [self.firstChoiceBtn, self.secondChoiceBtn, self.thirdChoiceBtn, self.fourthChoiceBtn]

        self.firstChoiceBtn.clicked.connect(lambda : self.CheckNote(self.file, self.firstChoiceBtn.text()))
        self.secondChoiceBtn.clicked.connect(lambda : self.CheckNote(self.file, self.secondChoiceBtn.text()))
        self.thirdChoiceBtn.clicked.connect(lambda : self.CheckNote(self.file, self.thirdChoiceBtn.text()))
        self.fourthChoiceBtn.clicked.connect(lambda : self.CheckNote(self.file, self.fourthChoiceBtn.text()))

        self.fileLabel = QLabel()
        self.fileLabel.setAlignment(Qt.AlignCenter)
        self.file = self.LoadFile()
        self.vbox.addWidget(self.fileLabel)

        for choiceBtn in self.choiceBtns:
            self.vbox.addWidget(choiceBtn)

    def SetChoices(self, file):
        choices = []
        result = self.notes[file]
        choices.append(result)

        while len(choices) < 4:
            randomNote = random.choice(list(self.notes.values()))
            if randomNote not in choices and randomNote != result:
                choices.append(randomNote)
        random.shuffle(choices)

        self.firstChoiceBtn.setText(choices[0])
        self.secondChoiceBtn.setText(choices[1])
        self.thirdChoiceBtn.setText(choices[2])
        self.fourthChoiceBtn.setText(choices[3])


    def LoadFile(self, beforeFile=""):
        file = self.GetRandomNote(beforeFile)
        self.filePixmap = QPixmap(file)
        self.fileLabel.setPixmap(self.filePixmap)
        self.SetChoices(file)
        return file

    def CheckNote(self, file, answer):
        result = self.notes[file]
        if answer == result:
            QMessageBox.information(self, "Doğru", "Cevabınız doğru!")
            self.file = self.LoadFile(file)
        else:
            QMessageBox.warning(self, "Yanlış", "Cevabınız yanlış!")

    def GetRandomNote(self, beforeFile=""):
        files = []

        for file in self.notes:
            if file != beforeFile:
                files.append(file)

        randomFile = random.choice(files)
        return randomFile

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window("Note Game", (100, 100, 0, 0), "./img/icon.jpg")
    app.exec_()