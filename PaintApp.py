#ARKAPRATIM GHOSH
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PaintApp")
        self.setGeometry(100,100,800,600)
        self.image=QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing=False
        self.brushSize=2
        self.brushColor=Qt.black
        self.lastPoint=QPoint()
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu("FILE")
        bsize=mainMenu.addMenu("BRUSH SIZE")
        bcolor=mainMenu.addMenu("BRUSH COLOR")

        saveA=QAction("SAVE",self)
        saveA.setShortcut("Ctrl+S")
        fileMenu.addAction(saveA)
        saveA.triggered.connect(self.save)#

        clearA=QAction("CLEAR",self)
        clearA.setShortcut("Ctrl+X")
        fileMenu.addAction(clearA)
        clearA.triggered.connect(self.clear)#

        pix4=QAction("4px",self)
        bsize.addAction(pix4)
        pix4.triggered.connect(self.Pixel_4)#

        pix7=QAction("7px",self)
        bsize.addAction(pix7)
        pix7.triggered.connect(self.Pixel_7)#

        pix9=QAction("9px",self)
        bsize.addAction(pix9)
        pix9.triggered.connect(self.Pixel_9)#

        pix12=QAction("12px",self)
        bsize.addAction(pix12)
        pix12.triggered.connect(self.Pixel_12)#

        black=QAction("Black",self)
        bcolor.addAction(black)
        black.triggered.connect(self.blackColor)#

        white = QAction("White", self)
        bcolor.addAction(white)
        white.triggered.connect(self.whiteColor)  #

        green= QAction("Green", self)
        bcolor.addAction(green)
        green.triggered.connect(self.greenColor)  #

        red = QAction("Red", self)
        bcolor.addAction(red)
        black.triggered.connect(self.RedColor)  #

        yellow = QAction("Yellow", self)
        bcolor.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)  #

        def MousePoint(self,event):
            if event.button()==Qt.LeftButton:
                self.drawing=True
                self.lastPoint=event.pos()

        def MouseMove(self,event):
            if (event.buttons() & Qt.LeftButton) & self.drawing:
                painter=QPainter(self.image)
                painter.setPen(QPen(self.brushColor,self.brushSize,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin))
                painter.drawLine(self.lastPoint,event.pos())
                self.lastPoint=event.pos()
                self.update()

        def MouseRelease(self,event):
            if event.button()==Qt.LeftButton:
                self.drawing=False

        def paintEvent(self,event):
            canvasPainter=QPainter(self)
            canvasPainter.drawImage(self.rect(),self.image,self.image.rect())

        def save(self):
            filepath,_=QFileDialog.getSaveFileName(self,"SAVE IMAGE","","PNG(*.png);;JPEG(*.jpg *jpeg);;All Files(*.*)")
            if filepath=="":
                return
            self.image.save(filepath)

        def clear(self):
            self.image.fill(Qt.white)
            self.update()

        def Pixel_4(self):
            self.brushSize=4

        def Pixel_7(self):
            self.brushSize=7

        def Pixel_9(self):
            self.brushSize=9

        def Pixel_12(self):
            self.brushSize=12

        def blackColor(self):
            self.brushColor=Qt.black

        def yellowColor(self):
            self.brushColor=Qt.yellow

        def whiteColor(self):
            self.brushColor=Qt.white

        def redColor(self):
            self.brushColor=Qt.red

        def greenColor(self):
            self.brushColor=Qt.green

App=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(App.exec())


