from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
#from classes.game.game import Game

class Menu(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        playButton = QPushButton("Play")
        loadButton = QPushButton("Load Game")
        exitButton = QPushButton("Exit")
        scoreButton = QPushButton("High Scores")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(playButton)
        hbox.addWidget(loadButton)
        hbox.addWidget(scoreButton)
        hbox.addWidget(exitButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Hotline Clone')
        self.show()
