# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_visor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FunctionVisor(object):
    def setupUi(self, FunctionVisor):
        FunctionVisor.setObjectName("FunctionVisor")
        FunctionVisor.resize(341, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FunctionVisor.sizePolicy().hasHeightForWidth())
        FunctionVisor.setSizePolicy(sizePolicy)
        FunctionVisor.setMinimumSize(QtCore.QSize(0, 0))
        FunctionVisor.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionVisor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isVisibleBox = QtWidgets.QCheckBox(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isVisibleBox.sizePolicy().hasHeightForWidth())
        self.isVisibleBox.setSizePolicy(sizePolicy)
        self.isVisibleBox.setText("")
        self.isVisibleBox.setObjectName("isVisibleBox")
        self.horizontalLayout.addWidget(self.isVisibleBox)
        self.name = QtWidgets.QLabel(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.color = QtWidgets.QWidget(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy)
        self.color.setMinimumSize(QtCore.QSize(20, 0))
        self.color.setMaximumSize(QtCore.QSize(40, 1000))
        self.color.setStyleSheet("background-color: black;\n"
"")
        self.color.setObjectName("color")
        self.horizontalLayout_2.addWidget(self.color)
        self.changeColorButton = QtWidgets.QToolButton(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeColorButton.sizePolicy().hasHeightForWidth())
        self.changeColorButton.setSizePolicy(sizePolicy)
        self.changeColorButton.setMinimumSize(QtCore.QSize(0, 20))
        self.changeColorButton.setMaximumSize(QtCore.QSize(60, 40))
        self.changeColorButton.setObjectName("changeColorButton")
        self.horizontalLayout_2.addWidget(self.changeColorButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.deleteButton = QtWidgets.QPushButton(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(0, 25))
        self.deleteButton.setMaximumSize(QtCore.QSize(60, 40))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(FunctionVisor)
        QtCore.QMetaObject.connectSlotsByName(FunctionVisor)

    def retranslateUi(self, FunctionVisor):
        _translate = QtCore.QCoreApplication.translate
        FunctionVisor.setWindowTitle(_translate("FunctionVisor", "Form"))
        self.name.setText(_translate("FunctionVisor", "Nombre de GraphFunction"))
        self.changeColorButton.setText(_translate("FunctionVisor", "..."))
        self.deleteButton.setText(_translate("FunctionVisor", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FunctionVisor = QtWidgets.QWidget()
    ui = Ui_FunctionVisor()
    ui.setupUi(FunctionVisor)
    FunctionVisor.show()
    sys.exit(app.exec_())

