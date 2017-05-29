import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QAction, QToolBar, QToolTip, QMessageBox, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QCoreApplication

class fraktal(QMainWindow):

    def __init__(self, x=300, y=300, h=500, w=500):
        super().__init__() #returns the parent object of the Example class and we call its constructor
        self.initUI()


#If we close a QWidget, the QCloseEvent is generated. To modify the widget behaviour we need to reimplement the closeEvent() event handler.
    def closeEvent(self,event):
        mess1=QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mess1 == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def helpGetter(self):
        print('Calm down, help is on its way here')

    def exito(self):
        print('exito: klose')
        sys.exit()


    def initUI(self, x=300, y=300, h=500, w=500):
        self.setGeometry(x,y,h,w)
        self.setWindowIcon(QIcon('icon.jpg'))

        self.setToolTip("tip: This is window")

        yb1=0.1*h
        bnt1=QPushButton("Press",self)
        bnt1.setToolTip("If you want to press a button - just press it")
        bnt1.setGeometry(10,yb1,50,30)
        bnt1.pressed.connect(lambda: print('press!'))

        bnt2=QPushButton('Quit',self)
        bnt2.setGeometry(w - 70, h - 70, 50, 30)
        #bnt2.clicked.connect(QCoreApplication.instance().quit)
        bnt2.clicked.connect(QCoreApplication.instance().quit)


        stat=self.statusBar()


        ea1=QAction('&Hello', self)
        ea1.setShortcut('Ctrl+Q')
        ea1.setStatusTip("Be greated oh mighty lord")
        ea1.setToolTip('Press it - tip')
        ea1.triggered.connect(lambda: print('file fire'))

        ea2=QAction('Bye',self)
        ea2.setIcon(QIcon('icon.jpg'))
        ea2.setShortcut('Alt+a')
        ea2.setToolTip('A Nice Tip')
        ea2.triggered.connect(lambda: self.exito())

        ea3=QAction('HEEEEELP',self)
        ea3.setToolTip('get some help pls')
        ea3.setStatusTip('You are about to get some help')
        ea3.setShortcut("SHIFT+h")
        ea3.triggered.connect(lambda: self.helpGetter())

        menu=self.menuBar()
        fileMenu=menu.addMenu("File")
        fileMenu.addAction(ea1)
        fileMenu.addAction(ea2)

        helpMenu=menu.addMenu('Help')
        helpMenu.addAction(ea3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = fraktal()

    ex.show()
    sys.exit(app.exec_())

