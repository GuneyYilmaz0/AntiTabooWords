import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox, QGridLayout, QWidget, QLabel, \
    QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox, QTextEdit

import main


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.level_selecting = False
        self.how_to_play1 = False
        self.setWindowTitle("Anti Taboo Words")
        self.resize(270, 110)
        self.start_game = QPushButton("Start Game")
        self.how_to_play_button = QPushButton("How to Play")
        self.layout = QGridLayout()

        self.layout.addWidget(self.start_game)
        self.layout.addWidget(self.how_to_play_button)

        self.how_to_play_button.clicked.connect(self.how_to_play)
        self.start_game.clicked.connect(self.select_level)
        self.setLayout(self.layout)
        self.dialogs = list()

    def select_level(self):
        if not self.level_selecting:
            dialog = SelectLevel(self)
            self.dialogs.append(dialog)
            dialog.show()

    def how_to_play(self):
        if not self.how_to_play1:
            dialog = HowToPlay(self)
            self.dialogs.append(dialog)
            dialog.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, "Quit Game", "Are you sure want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class HowToPlay(QMainWindow):
    def __init__(self, parent=None):
        super(HowToPlay, self).__init__(parent)
        self.setWindowTitle("How to Play")
        self.label = QLabel()

        self.label.setText("How to play asdasdas ")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


class SelectLevel(QMainWindow):
    def __init__(self, parent=None):
        super(SelectLevel, self).__init__(parent)
        self.setWindowTitle("Select Level")
        self.resize(270, 110)
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("Select difficulty:")
        self.easy = QPushButton("Easy")
        self.normal = QPushButton("Normal")
        self.hard = QPushButton("Hard")
        layout.addWidget(self.label)
        layout.addWidget(self.easy)
        layout.addWidget(self.normal)
        layout.addWidget(self.hard)
        self.easy.clicked.connect(self.easyw)
        self.normal.clicked.connect(self.normalw)
        self.hard.clicked.connect(self.hardw)
        layout.addStretch()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.dialogs = list()

    def easyw(self):
        self.close()
        dialog = GameWindow(self, 1)
        self.dialogs.append(dialog)
        dialog.show()

    def normalw(self):
        self.close()
        dialog = GameWindow(self, 2)
        self.dialogs.append(dialog)
        dialog.show()

    def hardw(self):
        self.close()
        dialog = GameWindow(self, 3)
        self.dialogs.append(dialog)
        dialog.show()


class GameWindow(QMainWindow):
    def __init__(self, parent=None, gamemode=0, points=0):
        super(GameWindow, self).__init__(parent)
        self.setWindowTitle("Anti Taboo Game")
        self.mode = QLabel()
        self.label = QLabel()
        self.resize(1080, 720)
        self.mode.setText(f"Selected difficulty: {gamemode}")
        self.points = points
        self.label.setText(f"Points: {self.points}")

        self.word = QLabel()
        selected_word = main.selecting(gamemode)
        miktar = len(selected_word[0]) -1
        self.word.setText(selected_word[0][0] + (" _ " * miktar))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mode)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.word)
        self.keywordslabel = QLabel()
        self.keywordslabel.setText("Keywords:")
        self.layout.addWidget(self.keywordslabel)

        if len(selected_word) == 3:
            self.keyword1 = QLabel()
            self.keyword1.setText(selected_word[1])
            self.keyword2 = QLabel()
            self.keyword2.setText(selected_word[2])
            self.layout.addWidget(self.keyword1)
            self.layout.addWidget(self.keyword2)
        elif len(selected_word) == 4:
            self.keyword1 = QLabel()
            self.keyword1.setText(selected_word[1])
            self.keyword2 = QLabel()
            self.keyword2.setText(selected_word[2])
            self.keyword3 = QLabel()
            self.keyword3.setText(selected_word[3])
            self.layout.addWidget(self.keyword1)
            self.layout.addWidget(self.keyword2)
            self.layout.addWidget(self.keyword3)
        elif len(selected_word) == 5:
            self.keyword1 = QLabel()
            self.keyword1.setText(selected_word[1])
            self.keyword2 = QLabel()
            self.keyword2.setText(selected_word[2])
            self.keyword3 = QLabel()
            self.keyword3.setText(selected_word[3])
            self.keyword4 = QLabel()
            self.keyword4.setText(selected_word[4])
            self.layout.addWidget(self.keyword1)
            self.layout.addWidget(self.keyword2)
            self.layout.addWidget(self.keyword3)
            self.layout.addWidget(self.keyword4)

        self.uncorrect = QLabel()
        self.uncorrect.setText("")
        self.layout.addWidget(self.uncorrect)
        self.textbox = QTextEdit()
        enter_b = QPushButton("Enter")
        clear_b = QPushButton("Clear")

        enter_b.clicked.connect(lambda: self.click(selected_word[0], self.textbox.toPlainText(), gamemode, self.points))
        clear_b.clicked.connect(lambda: self.textbox.setText(""))
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(enter_b)
        self.layout.addWidget(clear_b)
        self.layout.addStretch()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.dialogs = list()

    def click(self, word1, word2, gamemode, points):
        a = check(word1, word2)
        if a:
            self.correct(gamemode, points)
        else:
            self.uncorrect.setText("Wrong answer, try again.")


    def correct(self, gamemode, points):
        self.close()
        dialog = GameWindow(self, gamemode, points+1)
        self.dialogs.append(dialog)
        dialog.show()


def check(word1, word2):
    return check_answer(word1, word2)


def check_answer(word1, answer):
    if word1 != answer:
        return False
    else:
        return True

def setup():
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
