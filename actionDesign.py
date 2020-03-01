from pdf2png import *
from designWindow import *
from png2pdf import *
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QColorDialog, QFileDialog
from PyQt5.QtGui import QBrush, QPen, QPixmap, QFont, QPaintDevice, QImage, QPainter
from PyQt5.QtCore import Qt


class WindowDesign(Ui_DesignWindow):
    def setupUi(self, DesignWindow, OldWindow, funcReload):
        super().setupUiWin(DesignWindow)

        # cac bien noi bo
        self.numOfRect = 0
        self.numOfImg = 0
        self.numOfText = 0
        self.rect = []
        self.img = []
        self.text = []
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 10, 10)
        q = QPixmap("watermark/pdfModel.png").scaledToWidth(650)
        self.width = q.width()
        self.height = q.height()
        self.scene.setSceneRect(0, 0, self.width, self.height)
        self.mau = self.scene.addPixmap(q)
        self.graphicsView.setScene(self.scene)

        # Gan cac su kien
        self.btnSelectImg.clicked.connect(self.addImage)
        self.widthRec.textChanged.connect(self.changeWidth)
        self.heightRec.textChanged.connect(self.changeHeight)
        self.btnAddRec.clicked.connect(self.addRect)
        self.btnUndoRec.clicked.connect(self.undoRec)
        self.btnSelectColor.clicked.connect(self.selectColor)
        self.btnAddText.clicked.connect(self.addText)
        self.textInput.textChanged.connect(self.changeText)
        self.sizeText.textChanged.connect(self.changeSize)
        self.btnUndoText.clicked.connect(self.undoText)
        self.btnSave.clicked.connect(lambda: self.makeImg(DesignWindow,OldWindow, funcReload))
        self.btnSelectPdf.clicked.connect(lambda: self.loadPdf(DesignWindow))
        self.btnUndoImg.clicked.connect(self.undoImg)

    def loadPdf(self, ThisWindow):
        fname = QFileDialog.getOpenFileName(ThisWindow, 'Chọn PDF mẫu', 'c:\\', "Pdf files (*.pdf)")
        if fname[0]:
            pdf2png(fname[0],"watermark/")
            q = QPixmap("watermark/pdfModel.png").scaledToWidth(650)
            self.width = q.width()
            self.height = q.height()
            self.scene.setSceneRect(0, 0, self.width, self.height)
            self.mau.hide()
            self.mau = self.scene.addPixmap(q)

    def makeImg(self, ThisWindow, OldWindow, funcReload):
        name = self.textName.text() if self.textName.text() != "" else "NoName"
        self.mau.hide()
        img = QImage(self.width, self.height, QImage.Format_ARGB32)
        painter = QPainter(img)
        self.scene.render(painter)
        painter.end()
        img.save("watermark/template.png")
        png2pdf("watermark/template.png", "watermark/" + name + ".pdf")
        ThisWindow.close()
        OldWindow.show()
        funcReload()

    def addImage(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file','c:\\', "Image files (*.png)")
        if fname[0]:
            temImg = QPixmap(fname[0])
            temImg = temImg.scaledToWidth(int(temImg.width()*70/123))
            self.img.append({"main": self.scene.addPixmap(temImg), "url": fname[0]})
            self.img[self.numOfImg]["main"].setFlag(QGraphicsItem.ItemIsMovable)
            self.numOfImg += 1

    def undoImg(self):
        if self.numOfImg > 0:
            self.img[-1]["main"].hide()
            self.img.pop()
            self.numOfImg -= 1

    def undoText(self):
        if self.numOfText > 0:
            self.text[-1]["main"].hide()
            self.text.pop()
            self.numOfText -= 1

    def changeSize(self):
        try:
            size = int(self.sizeText.text())
            if self.numOfText > 0:
                self.text[-1]["size"] = size
                html = self.toHtml(self.text[-1]["content"], self.text[-1]["color"], size)
                self.text[-1]["main"].setHtml(html)
        except:
            pass

    def changeText(self):
        content = self.textInput.text()
        if content != "" and self.numOfText > 0:
            self.text[-1]["content"] = content
            html = self.toHtml(content, self.text[-1]["color"], self.text[-1]["size"])
            self.text[-1]["main"].setHtml(html)

    def addText(self):
        content = "Không có nội dung" if self.textInput.text() == "" else self.textInput.text()
        try:
            size = int(self.sizeText.text())
        except:
            size = 15
        self.text.append({"main": self.scene.addText(""), "content": content, "color": [0, 0, 255], "size": size})
        self.text[self.numOfText]["main"].setHtml(self.toHtml(content, [0, 0, 255], size))
        self.text[self.numOfText]["main"].setFlag(QGraphicsItem.ItemIsMovable)
        self.numOfText += 1

    def selectColor(self):
        color = QColorDialog.getColor()
        if self.numOfText > 0:
            self.text[-1]["color"] = [color.red(), color.green(), color.blue()]
            html = self.toHtml(self.text[-1]["content"], self.text[-1]["color"],
                               self.text[-1]["size"])
            self.text[self.numOfText - 1]["main"].setHtml(html)

    def undoRec(self):
        if self.numOfRect > 0:
            self.rect[-1].hide()
            self.rect.pop()
            self.numOfRect -= 1

    def changeWidth(self):
        try:
            r = self.rect[-1].rect()
            r.setWidth(float(self.widthRec.text()))
            self.rect[-1].setRect(r)
        except:
            pass

    def changeHeight(self):
        try:
            r = self.rect[-1].rect()
            r.setHeight(float(self.heightRec.text()))
            self.rect[-1].setRect(r)
        except:
            pass

    def addRect(self):
        self.rect.append(self.scene.addRect(0, 0, 100, 100, QPen(Qt.red, -1), QBrush(Qt.white)))
        self.rect[self.numOfRect].setFlag(QGraphicsItem.ItemIsMovable)
        self.numOfRect += 1
        self.widthRec.setText("100")
        self.heightRec.setText("100")
    @staticmethod
    def toHtml(content, color, size):
        str = '<span style="color: rgb({},{},{});font-size: {}px">{}</span>'
        return str.format(color[0], color[1], color[2], size, content)

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    DesignWindow = QtWidgets.QMainWindow()
    ui = WindowDesign()
    ui.setupUi(DesignWindow)
    DesignWindow.show()
    sys.exit(app.exec_())
'''
