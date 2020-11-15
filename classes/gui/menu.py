from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from classes.db.database import Database
from classes.game.game import Game


class Menu(QMainWindow):

    def __init__(self):
        super(Menu,self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Zombie Rush")
        self.setStyleSheet("background-color: rgba(206,235,251,100)")
        self.initUI()
        self.db = Database()


    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(100,25)
        self.textbox.setText("Player Name")
        self.textbox.setStyleSheet("background-color : rgba(247,140,104,150)")
        self.textbox.setAlignment(Qt.AlignCenter)
        self.playbutton = QPushButton("PLAY",self)
        self.playbutton.move(100,100)
        self.playbutton.setStyleSheet("background-color : rgba(102,167,197,200)")
        self.playbutton.clicked.connect(self.playbuttonclicked)
        self.scorebutton = QPushButton("SCORE",self)
        self.scorebutton.setStyleSheet("background-color : rgba(102,167,197,200)")
        self.scorebutton.clicked.connect(self.scorebuttonclicked)
        self.scorebutton.move(100,150)
        self.backbutton = QPushButton("BACK",self)
        self.backbutton.move(100, 250)
        self.backbutton.hide()
        self.backbutton.setStyleSheet("background-color : rgba(102,167,197,200)")
        self.exitbutton = QPushButton("EXIT",self)
        self.exitbutton.clicked.connect(self.exitbuttonclicked)
        self.exitbutton.move(100,250)
        self.exitbutton.setStyleSheet("background-color : rgba(102,167,197,200)")
        self.createTable()
        self.scoretable.move(50,100)

    def playbuttonclicked(self):
        self.gn = self.gamename()
        g = Game()
        g.name(self.gn)
        g.set_up()
        g.mainloop()
        QApplication.quit()
        
    def exitbuttonclicked(self):
        QApplication.quit()
    def scorebuttonclicked(self):

        self.scorebutton.hide()
        self.exitbutton.hide()
        self.playbutton.hide()
        self.scoretable.show()
        self.backbutton.show()
        self.backbutton.clicked.connect(self.backbuttonclicked)

        #mongo zostało

    def backbuttonclicked(self):
        self.scorebutton.show()
        self.exitbutton.show()
        self.playbutton.show()
        self.backbutton.hide()
        self.scoretable.hide()

    def createTable(self):
        self.scoretable = QTableWidget()
        self.scoretable.setColumnCount(2)
        self.scoretable.setRowCount(8)
        self.scoretable.setColumnWidth(0,150)
        self.scoretable.setColumnWidth(1,100)
        self.scoretable.setItem(0,0,QTableWidgetItem("Name"))
        self.scoretable.setItem(0, 1, QTableWidgetItem("Score"))
        self.scoretable.horizontalHeader().setStretchLastSection(True)
        self.scoretable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.fillTableMongo()

    def fillTableMongo(self):
        self.db.findAllScores()

    def gamename(self):
        textboxValue=self.textbox.text()
        return textboxValue