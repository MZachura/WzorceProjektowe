from PyQt5.QtWidgets import (QWidget,QMainWindow, QPushButton, QVBoxLayout, QApplication)
from classes.game.game import Game
import pygame
import sys

class Menu(QMainWindow):

    def __init__(self):
        super(Menu,self).__init__()
        
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Zombie Rush")
        self.initUI()

    def initUI(self):
        self.playbutton = QPushButton(self)
        self.playbutton.setText("PLAY")
        self.playbutton.move(100,50)
        self.playbutton.clicked.connect(self.playbuttonclicked)
        self.scorebutton = QPushButton(self)
        self.scorebutton.setText("SCORE")
        self.scorebutton.clicked.connect(self.scorebuttonclicked)
        self.scorebutton.move(100,100)        
        self.exitbutton = QPushButton(self)
        self.exitbutton.setText("EXIT")
        self.exitbutton.clicked.connect(self.exitbuttonclicked)
        self.exitbutton.move(100,200) 
        
    def playbuttonclicked(self):
        g = Game()
        g.set_up()
        g.mainloop()
        QApplication.quit()
        
    def exitbuttonclicked(self):
        QApplication.quit()
    def scorebuttonclicked(self):
        print("score")


        