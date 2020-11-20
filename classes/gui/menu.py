from message import Message, MessageDecorator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from classes.db.database import Database
from classes.game.game import Game
from config import *

class Menu(QMainWindow):

    def __init__(self):
        super(Menu,self).__init__()
        self.setGeometry(328,140,1024,768)
        self.setWindowTitle(TITLE)
        self.setStyleSheet("background-color: rgb(0,24,26)")
        self.initUI()

        # do dekoratora
        self.msg = Message(200, MENU_MSG)



    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(50,25)
        self.textbox.setText("Player Name")
        self.textbox.setStyleSheet("background-color : rgb(0,230,230)")
        self.textbox.setAlignment(Qt.AlignCenter)
        self.playbutton = QPushButton("PLAY",self)
        self.playbutton.move(50,100)
        self.playbutton.setStyleSheet("background-color : rgb(0,157,166)")
        self.playbutton.clicked.connect(self.playbuttonclicked)
        self.testbutton = QPushButton("TEST",self)
        self.testbutton.move(50,200)
        self.testbutton.setStyleSheet("background-color : rgb(0,157,166)")
        self.testbutton.clicked.connect(self.testbuttonclicked)
        self.scorebutton = QPushButton("SCORE",self)
        self.scorebutton.setStyleSheet("background-color : rgb(0,157,166)")
        self.scorebutton.clicked.connect(self.scorebuttonclicked)
        self.scorebutton.move(50,150)
        self.backbutton = QPushButton("BACK",self)
        self.backbutton.move(50, 250)
        self.backbutton.hide()
        self.backbutton.setStyleSheet("background-color : rgb(0,157,166)")
        self.exitbutton = QPushButton("EXIT",self)
        self.exitbutton.clicked.connect(self.exitbuttonclicked)
        self.exitbutton.move(50,250)
        self.exitbutton.setStyleSheet("background-color : rgb(0,157,166)")
        self.createTable()
        self.scoretable.move(358,140)

    def playbuttonclicked(self):
        self.gn = self.gamename()
        test=0
        g = Game(test)     # 0 gracz 1 tester
        # dekorator
        print(MessageDecorator(g))
        g.name(self.gn)
        g.set_up()
        g.mainloop()
        QApplication.quit()

    def testbuttonclicked(self):
        self.gn = self.gamename()
        test = 1
        g = Game(test)  # 0 gracz 1 tester
        g.name(self.gn)
        g.set_up()
        g.mainloop()
        QApplication.quit()

    def exitbuttonclicked(self):
        QApplication.quit()
    def scorebuttonclicked(self):
        self.textbox.hide()
        self.scorebutton.hide()
        self.exitbutton.hide()
        self.playbutton.hide()
        self.testbutton.hide()
        self.scoretable.show()
        self.backbutton.show()
        self.backbutton.clicked.connect(self.backbuttonclicked)


    def backbuttonclicked(self):
        self.textbox.show()
        self.scorebutton.show()
        self.exitbutton.show()
        self.playbutton.show()
        self.testbutton.show()
        self.backbutton.hide()
        self.scoretable.hide()

    def createTable(self):
        self.scoretable = QTableWidget()
        self.scoretable.setColumnCount(2)
        self.scoretable.setRowCount(10)
        self.scoretable.setColumnWidth(0,150)
        self.scoretable.setColumnWidth(1,100)
        self.scoretable.setItem(0,0,QTableWidgetItem("Name"))
        self.scoretable.setItem(0, 1, QTableWidgetItem("Score"))
        self.scoretable.horizontalHeader().setStretchLastSection(True)
        self.scoretable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.fillTableMongo()

    def fillTableMongo(self):
        data = Database()
        data.findAllScores()
        dane=[]
        dane = data.loopfor10()
        counter=9
        for i in dane:
            self.scoretable.setItem(counter,0,QTableWidgetItem(i['Player_name']))
            self.scoretable.setItem(counter, 1, QTableWidgetItem(str(i['score'])))
            counter+=-1
    def gamename(self):
        textboxValue=self.textbox.text()
        return textboxValue