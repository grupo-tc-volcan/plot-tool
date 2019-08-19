# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataViewerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 256)
        Dialog.setStyleSheet("background-color: rgb(230, 230, 230)\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 200, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.YAxisSelector = QtWidgets.QSpinBox(Dialog)
        self.YAxisSelector.setGeometry(QtCore.QRect(160, 130, 211, 25))
        self.YAxisSelector.setObjectName("YAxisSelector")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 50, 391, 121))
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
        self.XAxisSelector = QtWidgets.QSpinBox(Dialog)
        self.XAxisSelector.setGeometry(QtCore.QRect(160, 90, 211, 25))
        self.XAxisSelector.setObjectName("XAxisSelector")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 68, 19))
        self.label_3.setObjectName("label_3")
        self.actionhola = QtWidgets.QAction(Dialog)
        self.actionhola.setCheckable(True)
        self.actionhola.setObjectName("actionhola")
        self.actionchau = QtWidgets.QAction(Dialog)
        self.actionchau.setCheckable(True)
        self.actionchau.setObjectName("actionchau")

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

