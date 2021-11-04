from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random

from PyQt5.sip import simplewrapper


class Window(QWidget):
    def __init__(self, title, shape, icon, style):
        super().__init__()
        self.title = title
        self.x, self.y, self.w, self.h = shape
        self.icon = QIcon(icon)
        self.styleFile = style
        self.vbox = QVBoxLayout()
        self.notesPath = ".\\img\\notes\\"
        self.notes = {
            "{}1.png".format(self.notesPath): "kalın mi",
            "{}2.png".format(self.notesPath): "ince fa",
            "{}3.png".format(self.notesPath): "ince mi",
            "{}4.png".format(self.notesPath): "re",
            "{}5.png".format(self.notesPath): "do",
            "{}6.png".format(self.notesPath): "si",
            "{}7.png".format(self.notesPath): "la",
            "{}8.png".format(self.notesPath): "sol",
            "{}9.png".format(self.notesPath): "kalın fa",
        }
        self.initUI()
        self.SetStyle()
        self.setLayout(self.vbox)
        self.show()

    def SetStyle(self):
        with open(self.styleFile, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.firstChoiceBtn = QPushButton(clicked=lambda : self.CheckNote(self.file, self.firstChoiceBtn))
        self.secondChoiceBtn = QPushButton(clicked=lambda : self.CheckNote(self.file, self.secondChoiceBtn))
        self.thirdChoiceBtn = QPushButton(clicked=lambda : self.CheckNote(self.file, self.thirdChoiceBtn))
        self.fourthChoiceBtn = QPushButton(clicked=lambda : self.CheckNote(self.file, self.fourthChoiceBtn))

        self.choiceBtns = [self.firstChoiceBtn, self.secondChoiceBtn, self.thirdChoiceBtn, self.fourthChoiceBtn]

        self.fileLabel = QLabel()
        self.fileLabel.setStyleSheet("background-color: #fff;")
        self.fileLabel.setAlignment(Qt.AlignCenter)
        self.file = self.LoadFile()

        self.results = QHBoxLayout()
        self.totalCorrectLabel = QLabel(text="0")
        self.totalWrongLabel = QLabel(text="0")
        self.totalCorrectLabel.setAlignment(Qt.AlignCenter)
        self.totalWrongLabel.setAlignment(Qt.AlignCenter)
        self.totalCorrectLabel.setStyleSheet("color: #3ca81b;")
        self.totalWrongLabel.setStyleSheet("color: #a12727;")
        self.results.addWidget(self.totalCorrectLabel)
        self.results.addWidget(self.totalWrongLabel)

        self.nextBtn = QPushButton(text=">>>", clicked=lambda : self.NextQuestion(self.file))
        self.nextBtn.setVisible(False)

        self.resetBtn = QPushButton(text="Sıfırla", clicked=lambda : self.Reset(self.file))

        self.vbox.addWidget(self.resetBtn)
        self.vbox.addLayout(self.results)
        self.vbox.addWidget(self.fileLabel)
        for choiceBtn in self.choiceBtns:
            self.vbox.addWidget(choiceBtn)
        self.vbox.addStretch()
        self.vbox.addWidget(self.nextBtn)

    def SetChoices(self, file):
        choices = []
        result = self.notes[file]
        choices.append(result)

        while len(choices) < 4:
            randomNote = random.choice(list(self.notes.values()))
            if randomNote not in choices and randomNote != result:
                choices.append(randomNote)
        random.shuffle(choices)

        i = 0
        while i < 4:
            self.choiceBtns[i].setText(choices[i])
            i += 1

    def LoadFile(self, beforeFile=""):
        file = self.GetRandomNote(beforeFile)
        self.filePixmap = QPixmap(file)
        self.fileLabel.setPixmap(self.filePixmap)
        self.SetChoices(file)
        return file

    def Reset(self, beforeFile=""):
        self.NextQuestion(beforeFile)
        self.totalCorrectLabel.setText("0")
        self.totalWrongLabel.setText("0")
    
    def NextQuestion(self, beforeFile):
        self.file = self.LoadFile(beforeFile)
        for choiceBtn in self.choiceBtns:
            choiceBtn.setDisabled(False)
            choiceBtn.setStyleSheet("background-color: #1c0a5f;")
        self.nextBtn.setVisible(False)

    def CheckNote(self, file, btn:QPushButton):
        result = self.notes[file]
        if btn.text() == result:
            btn.setStyleSheet("background-color: green;")
            self.totalCorrectLabel.setText(str(int(self.totalCorrectLabel.text()) + 1))
        else:
            btn.setStyleSheet("background-color: red;")
            self.totalWrongLabel.setText(str(int(self.totalWrongLabel.text()) + 1))
            for choiceBtn in self.choiceBtns:
                if choiceBtn.text() == result:
                    choiceBtn.setStyleSheet("background-color: green;")

        for choiceBtn in self.choiceBtns:
            choiceBtn.setDisabled(True)
        
        self.nextBtn.setVisible(True)

    def GetRandomNote(self, beforeFile=""):
        files = []

        for file in self.notes:
            if file != beforeFile:
                files.append(file)

        randomFile = random.choice(files)
        return randomFile

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window("Note Game", (100, 100, 0, 700), "./img/icon.jpg", ".\\style\\style.css")
    app.exec_()