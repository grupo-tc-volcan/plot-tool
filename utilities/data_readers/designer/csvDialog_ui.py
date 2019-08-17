# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csvDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 395)
        Dialog.setStyleSheet("background-color: rgb(230, 230, 230)\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 330, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 180, 451, 121))
        self.frame.setStyleSheet("\n"
"background-color: rgb(225, 225, 225);\n"
"border-color: rgb(189, 189, 189);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 68, 19))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 40, 68, 19))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 281, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 80, 281, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 68, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 101, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 101, 19))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 68, 19))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 30, 281, 31))
        self.plainTextEdit.setStyleSheet("bacground-color: rgb(255, 255, 255)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 80, 281, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 120, 281, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.actionhola = QtWidgets.QAction(Dialog)
        self.actionhola.setCheckable(True)
        self.actionhola.setObjectName("actionhola")
        self.actionchau = QtWidgets.QAction(Dialog)
        self.actionchau.setCheckable(True)
        self.actionchau.setObjectName("actionchau")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.plainTextEdit.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buttonBox.setWhatsThis(_translate("Dialog", "hola"))
        self.label_2.setText(_translate("Dialog", "Y-Axis"))
        self.label.setText(_translate("Dialog", "X-Axis"))
        self.label_4.setText(_translate("Dialog", "Name"))
        self.label_5.setText(_translate("Dialog", "Magnitude X"))
        self.label_6.setText(_translate("Dialog", "Magnitude Y"))
        self.label_3.setText(_translate("Dialog", "Plot Axis"))
        self.actionhola.setText(_translate("Dialog", "hola"))
        self.actionchau.setText(_translate("Dialog", "chau"))
        self.actionchau.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">chaaauuuuuu</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())