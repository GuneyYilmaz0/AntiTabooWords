import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QPushButton("click me")

        self.setCentralWidget(self.pushButton)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialogs = list()

    def on_pushButton_clicked(self):
        dialog = Second(self)
        self.dialogs.append(dialog)
        dialog.show()


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
