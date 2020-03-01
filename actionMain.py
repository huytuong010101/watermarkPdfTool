from WindowMainUi import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from actionDesign import *
from watermarkPdf import *
import threading

class WindowMain(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.listInput = []
        # load file to combobox
        self.loadListPdfModel()
        # set event
        self.btnDelWatermark.clicked.connect(self.deleteWatermark)
        self.btnNewWatermark.clicked.connect(self.openDesignWindow)
        self.btnSelectPdf.clicked.connect(self.loadPdf)
        self.btnClearInput.clicked.connect(self.deleteAllInput)
        self.btnSelectFolder.clicked.connect(self.selectFolder)
        self.selectSave.clicked.connect(self.chooseSave)
        self.btnResetPath.clicked.connect(self.resetSave)
        self.btnStart.clicked.connect(self.startMark)

    def startMark(self):
        self.outputList.clear()
        listPage = []
        if self.inputPage.text() != "":
            try:
                text = self.inputPage.text()
                if "-" in text:
                    a, b = text.split("-")
                    a = int(a)
                    b = int(b)
                    listPage = range(a - 1, b)
                else:
                    arr = text.split()
                    listPage = list(map(lambda x: int(x)-1, arr))
            except:
                pass

        for pdfFile in self.listInput:
            threading.Thread(target= lambda : self.threadMark(pdfFile, listPage)).start()
        self.listInput = []
        self.inputList.clear()

    def threadMark(self, pdfFile, listPage):
        try:
            startMark(pdfFile, self.lbSave.text(), "watermark/" + self.listPdfWatermark.currentText(), listPage)
            self.outputList.append(pdfFile.split("/")[-1] + " - Xong")
        except Exception as e:
            self.outputList.append(pdfFile.split("/")[-1] + " - Lỗi")
            print(e)

    def resetSave(self):
        self.lbSave.setText("/")

    def chooseSave(self):
        dialog = QFileDialog().getExistingDirectory(MainWindow, "Chọn nơi lưu", "D:/")
        if dialog:
            self.lbSave.setText("/".join((dialog.split("\\"))))

    def loadPdf(self):
        fname = QFileDialog.getOpenFileNames(MainWindow, 'Chọn PDF', 'c:\\', "Pdf files (*.pdf)")
        if len(fname[0]):
            for path in fname[0]:
                self.listInput.append(path)
                self.inputList.append(path.split("/")[-1])

    def selectFolder(self):

        dialog = QFileDialog().getExistingDirectory(MainWindow, "Chọn folder","D:/")
        if len(dialog) == 0:
            return
        dirList = ["/".join(f.path.split("\\")) for f in os.scandir(dialog) if f.is_dir()]
        for path in dirList:
            for r, d, f in os.walk(path):
                for file in f:
                    if '.pdf' in file:
                        self.listInput.append(path + "/" + file)
                        self.inputList.append(file)

    def deleteAllInput(self):
        self.listInput = []
        self.inputList.clear()

    def openDesignWindow(self):
        self.DesignWindow = QMainWindow()
        WindowDesign().setupUi(self.DesignWindow, MainWindow, self.loadListPdfModel)
        self.DesignWindow.show()
        MainWindow.hide()

    def deleteWatermark(self):
        os.remove("watermark\\" + self.listPdfWatermark.currentText())
        self.loadListPdfModel()

    def loadListPdfModel(self):
        self.listPdfWatermark.clear()
        path = 'watermark\\'
        for r, d, f in os.walk(path):
            for file in f:
                if '.pdf' in file:
                    self.listPdfWatermark.addItem(file)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QMainWindow()
    ui = WindowMain()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
