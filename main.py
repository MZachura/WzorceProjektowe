from message import MessageDecorator
import sys
from classes.gui.menu import Menu
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    print(MessageDecorator(menu))
    menu.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
              