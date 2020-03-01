# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DesignWindow(object):
    def setupUiWin(self, DesignWindow):
        DesignWindow.setObjectName("DesignWindow")
        DesignWindow.setWindowIcon(QtGui.QIcon("logoMain.png"))
        DesignWindow.resize(761, 557)
        DesignWindow.setMinimumSize(QtCore.QSize(761, 557))
        DesignWindow.setMaximumSize(QtCore.QSize(761, 557))
        self.centralwidget = QtWidgets.QWidget(DesignWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setGeometry(QtCore.QRect(400, 10, 350, 495))
        self.graphicsView.setMinimumSize(QtCore.QSize(350, 495))
        self.graphicsView.setMaximumSize(QtCore.QSize(350, 495))
        self.graphicsView.setObjectName("graphicsView")
        self.groupImg = QtWidgets.QGroupBox(self.centralwidget)
        self.groupImg.setGeometry(QtCore.QRect(240, 240, 131, 80))
        self.groupImg.setObjectName("groupImg")
        self.btnSelectImg = QtWidgets.QPushButton(self.groupImg)
        self.btnSelectImg.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.btnSelectImg.setObjectName("btnSelectImg")
        self.btnUndoImg = QtWidgets.QPushButton(self.groupImg)
        self.btnUndoImg.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.btnUndoImg.setObjectName("btnUndoImg")
        self.groupAddText = QtWidgets.QGroupBox(self.centralwidget)
        self.groupAddText.setGeometry(QtCore.QRect(20, 150, 351, 80))
        self.groupAddText.setObjectName("groupAddText")
        self.btnAddText = QtWidgets.QPushButton(self.groupAddText)
        self.btnAddText.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnAddText.setObjectName("btnAddText")
        self.btnUndoText = QtWidgets.QPushButton(self.groupAddText)
        self.btnUndoText.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.btnUndoText.setObjectName("btnUndoText")
        self.textInput = QtWidgets.QLineEdit(self.groupAddText)
        self.textInput.setGeometry(QtCore.QRect(90, 20, 251, 20))
        self.textInput.setObjectName("textInput")
        self.label = QtWidgets.QLabel(self.groupAddText)
        self.label.setGeometry(QtCore.QRect(110, 50, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupAddText)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 31, 16))
        self.label_2.setObjectName("label_2")
        self.sizeText = QtWidgets.QLineEdit(self.groupAddText)
        self.sizeText.setGeometry(QtCore.QRect(140, 50, 51, 20))
        self.sizeText.setObjectName("sizeText")
        self.btnSelectColor = QtWidgets.QPushButton(self.groupAddText)
        self.btnSelectColor.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.btnSelectColor.setObjectName("btnSelectColor")
        self.groupRec = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRec.setGeometry(QtCore.QRect(20, 240, 211, 80))
        self.groupRec.setObjectName("groupRec")
        self.btnAddRec = QtWidgets.QPushButton(self.groupRec)
        self.btnAddRec.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnAddRec.setObjectName("btnAddRec")
        self.btnUndoRec = QtWidgets.QPushButton(self.groupRec)
        self.btnUndoRec.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.btnUndoRec.setObjectName("btnUndoRec")
        self.widthRec = QtWidgets.QLineEdit(self.groupRec)
        self.widthRec.setGeometry(QtCore.QRect(120, 20, 81, 20))
        self.widthRec.setObjectName("widthRec")
        self.heightRec = QtWidgets.QLineEdit(self.groupRec)
        self.heightRec.setGeometry(QtCore.QRect(120, 50, 81, 20))
        self.heightRec.setObjectName("heightRec")
        self.label_3 = QtWidgets.QLabel(self.groupRec)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupRec)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 31, 16))
        self.label_4.setObjectName("label_4")
        self.groupSave = QtWidgets.QGroupBox(self.centralwidget)
        self.groupSave.setGeometry(QtCore.QRect(20, 330, 351, 81))
        self.groupSave.setObjectName("groupSave")
        self.label_5 = QtWidgets.QLabel(self.groupSave)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_5.setObjectName("label_5")
        self.textName = QtWidgets.QLineEdit(self.groupSave)
        self.textName.setGeometry(QtCore.QRect(10, 50, 201, 20))
        self.textName.setObjectName("textName")
        self.btnSave = QtWidgets.QPushButton(self.groupSave)
        self.btnSave.setGeometry(QtCore.QRect(220, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnSelectPdf = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectPdf.setGeometry(QtCore.QRect(30, 100, 81, 23))
        self.btnSelectPdf.setObjectName("btnSelectPdf")
        DesignWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DesignWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
        self.menubar.setObjectName("menubar")
        DesignWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DesignWindow)
        self.statusbar.setObjectName("statusbar")
        DesignWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DesignWindow)
        QtCore.QMetaObject.connectSlotsByName(DesignWindow)

    def retranslateUi(self, DesignWindow):
        _translate = QtCore.QCoreApplication.translate
        DesignWindow.setWindowTitle(_translate("DesignWindow", "Tạo mẫu mới"))
        self.groupImg.setTitle(_translate("DesignWindow", "Thêm ảnh"))
        self.btnSelectImg.setText(_translate("DesignWindow", "Chọn ảnh"))
        self.btnUndoImg.setText(_translate("DesignWindow", "Quay lại"))
        self.groupAddText.setTitle(_translate("DesignWindow", "Thêm text"))
        self.btnAddText.setText(_translate("DesignWindow", "Thêm text"))
        self.btnUndoText.setText(_translate("DesignWindow", "Quay lại"))
        self.label.setText(_translate("DesignWindow", "Size"))
        self.label_2.setText(_translate("DesignWindow", "Color"))
        self.btnSelectColor.setText(_translate("DesignWindow", "Chọn màu"))
        self.groupRec.setTitle(_translate("DesignWindow", "Thêm hình chữ nhật"))
        self.btnAddRec.setText(_translate("DesignWindow", "Thêm hình"))
        self.btnUndoRec.setText(_translate("DesignWindow", "Quay lại"))
        self.label_3.setText(_translate("DesignWindow", "Dài"))
        self.label_4.setText(_translate("DesignWindow", "Rộng"))
        self.groupSave.setTitle(_translate("DesignWindow", "Lưu lại"))
        self.label_5.setText(_translate("DesignWindow", "Nhập tên mẫu"))
        self.btnSave.setText(_translate("DesignWindow", "Lưu"))
        self.btnSelectPdf.setText(_translate("DesignWindow", "Chọn nền PDF"))

