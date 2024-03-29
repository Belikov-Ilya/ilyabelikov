# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_APLWindow(object):
    def setupUi(self, APLWindow):
        APLWindow.setObjectName("APLWindow")
        APLWindow.resize(500, 340)
        APLWindow.setStyleSheet("background-color: rgb(1, 66, 106);")
        self.verticalLayoutWidget = QtWidgets.QWidget(APLWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 160, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button3.setObjectName("button3")
        self.verticalLayout.addWidget(self.button3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(APLWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 120, 160, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button7.setObjectName("button7")
        self.verticalLayout_2.addWidget(self.button7)
        self.button8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button8.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button8.setObjectName("button8")
        self.verticalLayout_2.addWidget(self.button8)
        self.button9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button9.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button9.setObjectName("button9")
        self.verticalLayout_2.addWidget(self.button9)
        self.button10 = QtWidgets.QPushButton(APLWindow)
        self.button10.setGeometry(QtCore.QRect(150, 250, 201, 23))
        self.button10.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button10.setObjectName("button10")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(APLWindow)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(330, 30, 160, 83))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button4.setObjectName("button4")
        self.verticalLayout_3.addWidget(self.button4)
        self.button5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button5.setObjectName("button5")
        self.verticalLayout_3.addWidget(self.button5)
        self.button6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button6.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.button6.setObjectName("button6")
        self.verticalLayout_3.addWidget(self.button6)

        self.retranslateUi(APLWindow)
        QtCore.QMetaObject.connectSlotsByName(APLWindow)

    def retranslateUi(self, APLWindow):
        _translate = QtCore.QCoreApplication.translate
        APLWindow.setWindowTitle(_translate("APLWindow", "Английская Премьер Лига"))
        self.button1.setText(_translate("APLWindow", "Манчестер Сити"))
        self.button2.setText(_translate("APLWindow", "Арсенал"))
        self.button3.setText(_translate("APLWindow", "Манчестер Юнайтед"))
        self.button7.setText(_translate("APLWindow", "Эвертон"))
        self.button8.setText(_translate("APLWindow", "Фулхэм"))
        self.button9.setText(_translate("APLWindow", "Челси"))
        self.button10.setText(_translate("APLWindow", "Записать исход матча"))
        self.button4.setText(_translate("APLWindow", "Ливерпуль "))
        self.button5.setText(_translate("APLWindow", "Тоттенхэм"))
        self.button6.setText(_translate("APLWindow", "Лестер Сити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APLWindow = QtWidgets.QWidget()
    ui = Ui_APLWindow()
    ui.setupUi(APLWindow)
    APLWindow.show()
    sys.exit(app.exec_())
