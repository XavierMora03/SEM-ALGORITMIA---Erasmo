# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guigui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/2624891_devil_evil_hell boy_hero_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 100, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.separar_p)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(330, 160, 151, 17))
        self.checkBox.setObjectName("checkBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 300, 711, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 261, 231))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 40, 261, 231))
        self.textEdit_2.setObjectName("textEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(360, 190, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 210, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 230, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Separar Palabras"))
        self.checkBox.setText(_translate("MainWindow", "Converto todo minusculas"))
        self.radioButton.setText(_translate("MainWindow", "Azul"))
        self.radioButton_2.setText(_translate("MainWindow", "Mas Azul"))
        self.radioButton_3.setText(_translate("MainWindow", "muy azul"))
        
    def separar_p(self):
        texto = self.textEdit.toPlainText()
        if(self.checkBox.isChecked()):
            texto = texto.lower()
        
        
        if self.radioButton.isChecked():
            self.textEdit_2.setStyleSheet("background-color: #63C5DA;")
            
        if self.radioButton_2.isChecked():
            self.textEdit_2.setStyleSheet("background-color: #48AAAD;")
            
        if self.radioButton_3.isChecked():
            self.textEdit_2.setStyleSheet("background-color: #241571;")
        
        
        self.textEdit_2.setPlainText(texto)
        
        texto_spliteado = texto.split()
        for r in range(len(texto_spliteado),self.tableWidget.rowCount()):
            self.tableWidget.removeRow(len(texto_spliteado))
            
        for r in range(len(texto_spliteado)):
            rowAct =self.tableWidget.rowCount()
            if(rowAct <= r):
                self.tableWidget.insertRow(rowAct)

                
            self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(texto_spliteado[r]))
                
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

