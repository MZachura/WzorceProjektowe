import sys
from classes.game.game import Game
from classes.gui.menu import Menu
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

def main():
    #g = Game()
    #g.set_up()
    #g.mainloop()
    app = QApplication(sys.argv)
    m = Menu()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
