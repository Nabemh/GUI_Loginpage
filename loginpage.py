from PyQt6 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 552)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(40, 20, 451, 511))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(-130, 0, 731, 541))
        self.label.setStyleSheet("border-radius:20px;\n"
"\n"
"image: url(pexels-coco-hache-12411681.jpg);\n"
"")
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(79, 46, 301, 419))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.log_in = QtWidgets.QLabel(parent=self.widget)
        self.log_in.setGeometry(QtCore.QRect(185, 89, 111, 51))
        font = QtGui.QFont()
        font.setFamily("KacstScreen")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.log_in.setFont(font)
        self.log_in.setStyleSheet("color: rgb(255, 255, 255);")
        self.log_in.setObjectName("log_in")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 160, 240, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 225);\n"
"color:rgba(225, 225, 225, 230);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 230, 240, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 225);\n"
"color:rgba(225, 225, 225, 230);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton#pushButton { \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.447, stop:0 rgba(105, 101, 95, 1), stop:1 rgba(85, 98, 112, 226));\n"
" color:rgba(255, 255, 255, 210);\n"
" border-radius:5px; \n"
"}\n"
"QPushButton#pushButton:hover { \n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.447, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed { \n"
" background-color:rgba(105, 118, 132, 200); \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(147, 360, 161, 20))
        self.label_3.setStyleSheet("color: rgba(255, 255, 255, 140);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qt-Designer"))
        self.log_in.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_3.setText(_translate("Form", "Forgot your Password?"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec())