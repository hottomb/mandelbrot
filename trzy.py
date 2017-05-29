import sys
import random, array, math, numpy
from PyQt5.QtWidgets import QStyleFactory ,QMainWindow, QWidget, QApplication, QPushButton, QAction, QLabel, QToolTip, QMessageBox, qApp, QCheckBox, QProgressBar, QStyle, QComboBox

from PyQt5.QtGui import QIcon, QFont, QPainter
from PyQt5.QtCore import Qt, QTimer

class fraktal(QMainWindow):

    def __init__(self, x=400, y=50, h=700, w=700):
        super().__init__() #returns the parent object of the Example class and we call its constructor
        self.initUI()

    def paintEvent(self, e):
        coords = self.frameGeometry().getRect()
        # h = coords[3]
        h=self.h
        off = self.off
        self.yb1 = 0.1 * h + off
        self.yb2 = 0.2 * h + off
        self.yb3 = 0.3 * h + off
        self.yb4 = 0.4 * h + off
        self.wid = 60

        self.bnt1.setGeometry(10, self.yb1, self.wid, 30)
        self.bnt2.setGeometry(10+self.wid, self.yb1, self.wid, 30)
        self.bnt3.setGeometry(10, self.yb2, self.wid, 30)
        self.bnt4.setGeometry(10+self.wid, self.yb2, self.wid, 30)

        self.combo1.move(10, self.yb3)
        self.lab1.move(10, self.yb3 +100)
        # najpierw ustalanie srodowiska
        qr = QPainter()
        qr.begin(self)
        self.drawRect_(qr)
        qr.end()
        # potem rysowanie
        self.printPoints()



        # print('printing points')

    def timers(self):
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_t1)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_t2)

    def progressBars(self):
        self.pBar1 = QProgressBar(self)
        self.y_pbar1 = 80
        self.x_pbar1 = 250
        self.pBar1.setGeometry(10, self.y_pbar1, self.x_pbar1, 20)
        self.pBar1.setToolTip("Progress Bar 1")

        self.pBar2 = QProgressBar(self)
        self.pBar2.setGeometry(10, self.y_pbar1+30, self.x_pbar1, 20)
        self.pBar2.setToolTip("Progress Bar 2")

    def buttons(self,x,y,h,w):
        self.h = 350
        self.off=100
        h=self.h
        off=self.off
        self.yb1 = 0.1 * h + off
        self.yb2 = 0.2 * h + off
        self.yb3 = 0.3 * h + off
        self.yb4 = 0.4 * h + off
        self.wid=60

        self.bnt1 = QPushButton("Press", self)
        self.bnt1.setToolTip("If you want to press a button - just press it")
        self.bnt1.setGeometry(10, self.yb1, self.wid, 30)
        self.bnt1.pressed.connect(lambda: print('press!'))

        self.bnt2 = QPushButton('Quit', self)
        self.bnt2.setGeometry(10+self.wid, self.yb1, self.wid, 30)
        # bnt2.clicked.connect(QCoreApplication.instance().quit)
        self.bnt2.clicked.connect(self.exito)
        # bnt2.clicked.connect(lambda: self.exito())# czemu szkodzi nawias za funkcja, ze sie ona sama odpala???

        self.bnt3 = QPushButton("Download",self)
        self.bnt3.setGeometry(10,self.yb2, self.wid, 30)
        self.bnt3.clicked.connect(self.start_t1)

        self.bnt4 = QPushButton("Start",self)
        self.bnt4.setGeometry(10+self.wid,self.yb2, self.wid, 30)
        self.bnt4.clicked.connect(self.start_t2)

    def menu(self):
        ea1=QAction('&Hello', self)
        ea1.setShortcut('Ctrl+Q')
        ea1.setStatusTip("Be greated oh mighty lord")
        ea1.setToolTip('Press it - tip')
        ea1.triggered.connect(lambda: print('file fire'))

        ea2=QAction('Bye',self)
        ea2.setIcon(QIcon('icon.jpg'))
        ea2.setShortcut('Alt+a')
        ea2.setToolTip('A Nice Tip')
        ea2.triggered.connect(self.exito)

        ea3=QAction('HEEEEELP',self)
        ea3.setToolTip('get some help pls')
        ea3.setStatusTip('You are about to get some help')
        ea3.setShortcut("SHIFT+h")

        menu=self.menuBar()
        fileMenu=menu.addMenu("File")
        fileMenu.addAction(ea1)
        fileMenu.addAction(ea2)

        helpMenu=menu.addMenu('Help')
        helpMenu.addAction(ea3)

    def toolbar(self):
        ea11=QAction(QIcon('icon.jpg'), 'tool 1 - popup cloud', self)
        ea11.triggered.connect(self.event_)
        toolBar=self.addToolBar('wut this is???')
        toolBar.addAction(ea11)

        ea12 = QAction(QIcon('icon.jpg'), 'tool 2 - popup cloud', self)
        ea12.triggered.connect(self.event_)
        toolBar.addAction(ea12)
        #stworzyles pole klasy self.toolBar, dlatego mozesz sie do niego odwolywac w ten sam sposob, a nie tworzyc kolejny obiekt
        #ewentualnie mozesz stworzyc handler "toolBar" i dodawac opcje w tej samej f-cji, bo handler jest wtedy tylko lokalny

        #alternatively - o co tu chodzi, czemu sie stosuje self.... zamiast handlera i czemu sie wywoluje metode raz z nawiasem pustym a raz bez
        # self.toolBar=self.addToolBar('wut this is???')
        # self.toolBar.addAction(ea11)

    def chkbox(self,x,y,h,w):
        box1 = QCheckBox('Enlarge Window', self)
        box1.stateChanged.connect(self.comp_)
        box1.move(10+2*self.wid,self.yb1)
        # box1.toggle()

    def labels_(self):
        self.lab1 = QLabel("-layout style-",self)
        self.lab1.move(10,self.yb3+100)

    def combox(self):
        self.combo1 = QComboBox(self)
        self.combo1.addItem("motif")
        self.combo1.addItem("Windows")
        self.combo1.addItem("cde")
        self.combo1.addItem("Plastique")
        self.combo1.addItem("Cleanlooks")
        self.combo1.addItem("windowsvista")
        self.combo1.move(10,self.yb3)
        self.combo1.activated[str].connect(self.style_)



    def initUI(self, x=400, y=50, h=700, w=700):
        self.setGeometry(x,y,h,w)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowTitle("Demonstrator")
        self.setToolTip("tip: This is window")
        # init xy var
        self.xy=list()

        z = (random.random(), random.random())
        c = (1, 1)
        re2 = math.pow(z[0], 2) + 0 + math.pow(z[1], 2) - c[0]
        im2 = 2 * z[0] * z[1] - c[1]
        print(re2)
        print(im2)
        # a = self.conv #to jest metoda, typ "a" to method
        a = self.conv(z,c) #to jest wywolanie funkcje, 'a' to wartosc zwracana przez conv

        print(type(a))
        print(type(z))
        print(type(c))
        print(type(re2))

        self.timers()
        # self.timer2.start(10)

        self.progressBars()


        # z=complex(1,1)
        # print(pow(z,2))
        # print(type(z))
        # print("hej hej jo jo")

        # aae=((numpy.linspace(1,5,100)))
        # aae[1]
        self.buttons(x,y,h,w)
        self.labels_()
        self.combox()
        self.menu()
        self.toolbar()
        self.chkbox(x,y,h,w)

        self.statusBar()

        print(max(1,2,102))

        # p=((1,2),(3,4),(5,6))
        # w ,r = zip(*p)
        # print(w)
        # print(r)





    # If we close a QWidget, the QCloseEvent is generated. To modify the widget behaviour we need to reimplement the closeEvent() event handler.
    def closeEvent(self,event):
        pass
        # mess1=QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if mess1 == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def exito(self):
        pass
        # msg = QMessageBox.question(self,"Exit","Are you sure you want to exit?",QMessageBox.YesAll | QMessageBox.Cancel)
        # if msg == QMessageBox.YesAll:
        #     sys.exit()
        # else:
        #     pass

    def helpGetter(self):
        print('Calm down, help is on its way here')

    def update_t1(self):
        self.pBar1.setValue(self.pBar1.value()+1)
        # print("updatino")
        if self.pBar1.value()>=100:
            self.timer1.stop()
            self.pBar1.setValue(0)
        else:
            pass

    def update_t2(self):
        # print("timer2 timeout")
        self.pBar2.setValue(abs(random.random())*100)


    def start_t1(self):
        self.timer1.start(10)
        print("boop! timer1 started: download")

    def start_t2(self):
        self.timer2.start(100)
        #change button text by switching it back and forth

    def printPoints(self):
        # qt=QPainter()
        # qt.setPen(Qt.red)
        # qt.begin()
        # qt.drawPointss(self,qt)
        # qt.end()

        # qr = QPainter()
        qp = QPainter()
        qp.begin(self)
        self.drawPoints_(qp)
        qp.end()

        # print('printing points')


    def comp_(self):
        # self.xy.clear()
        c=(-0.09,0.20)

        self.x=(-1,0.9)
        self.y=(-1,-0.7)
        x=self.x
        y=self.y

        self.lin_res = 200
        lin_res=self.lin_res
        x_range = numpy.linspace(x[0], x[1], lin_res)
        y_range = numpy.linspace(y[0], y[1], lin_res)

        for ii in range(len(x_range)):
            self.pBar1.setValue((1+ii)/len(x_range)*100)

            for jj in range(len(y_range)):
                z=(x_range[ii],y_range[jj])
                t = self.conv(z,c)

                if t != None:
                    self.xy.append(t)

        try:
            x_s, y_s = zip(*self.xy)

            # unikanie abs(), ktory nie dziala na ciagach
            m_x = max(x_s)
            if m_x < min(x_s):
               m_x = -min(x_s)

            m_y = max(y_s)
            if m_y < min(y_s):
                m_y = -min(y_s)

            if m_x ==0:
                m_x=m_x+0.001
            if m_y ==0:
                m_y=m_y+0.001

            max_ = max(m_x, m_y)

            # normalizacja plotna do -1:1

            if max_ == m_x:
                x_s = x_s / m_x
                y_s = y_s / m_x
            else:
                x_s = x_s / m_y
                y_s = y_s / m_y
            # print(x_s)
            # print(y_s)
        except ValueError:
            print("unzip error")

        # enkapsulacja wspolrzednych do tupli xy
        try:
            self.xy = list(zip(x_s, y_s))
        except:
            print("zip error")

        print(self.xy)


    def conv(self,z,c):
        zx = complex(z[0],z[1])
        cx = complex(c[0],z[1])

        for i in range(0,20):
            zx2 = pow(zx,2) + cx
            if abs(zx2) >= 2:
                return None
            zx=zx2

        return (z)

    def drawPoints_(self, qp):
        qp.setPen(Qt.red)
        size = self.frameGeometry().getRect()


        sx = self.rx
        sy = self.ry
        sw = self.rw/2
        sh = self.rh/2

        # print(size)
        # print(sw)
        # print(sh)

        xb = 2
        yb = 2

        # print(xy)
        if 'lin_res' in globals():
            print("globals")
        elif 'lin_res' in locals():
            print("locals")

        s = 100
        for i in range(len(self.xy)):
            Txy=self.xy[i]
            x = round((Txy[0] )*s)+sw+sx
            y = round((Txy[1] )*s)+sh+sy
            # x = random.randint(1, size.width() - 1)
            # y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def drawRect_(self,qr):
        # pass
        try:
            qr.setPen(Qt.darkBlue)
            coords = self.frameGeometry().getRect()
            self.rx = self.x_pbar1 - 23
            self.ry = self.y_pbar1
            self.rw = self.width() - self.rx - 10
            self.rh = self.height() - self.ry - 10
            qr.drawRect(self.rx,self.ry,self.rw,self.rh)
            # qr.drawRect(100, 100, 400, 400)
            # print(self.rx,self.ry)
        except:
            print("rectangle error")

    def style_(self, str):
        print("style acknowledged")
        print(self.style().objectName())
        QApplication.setStyle(QStyleFactory.create(str))
        # self.QApplication.setStyle(QStyleFactory.create(text)) - TO BY BYLO ZLE PRZEZ SELF
        self.lab1.setText(self.style().objectName())

    def enlarge(self, state):

        coords = self.frameGeometry().getRect()
        print(coords)
        if state == Qt.Checked:
            print('ENGAGE')
            self.setGeometry(coords[0] + 8, coords[1] + 31, round(5 / 4 * coords[2]), coords[3])
        else:
            print('degage')
            # self.setGeometry(x,y,h,w)
            self.setGeometry(coords[0] + 8, coords[1] + 31, round(4 / 5 * coords[2]), coords[3])

    def event_(self):
        msg = QMessageBox.question(self, "Urgent Event Must Not Wait", "Are you sure you want to click?",
                                   QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            print('you clicked Yes')
        else:
            print("You've choosen No")

# print(QApplication.style())


        # print([self.frameGeometry().getRect(),self.pos()])
        # coords = self.frameGeometry().getRect()
        # print(coords[1], coords[2])
# def run():
#     app = QtGui.QApplication(sys.argv)
#     GUI = Window()
#     sys.exit(app.exec_())
# run()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = fraktal()

    ex.show()
    sys.exit(app.exec_())

