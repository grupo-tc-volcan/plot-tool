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
        FunctionVisor.resize(292, 61)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FunctionVisor.sizePolicy().hasHeightForWidth())
        FunctionVisor.setSizePolicy(sizePolicy)
        FunctionVisor.setMinimumSize(QtCore.QSize(0, 0))
        FunctionVisor.setMaximumSize(QtCore.QSize(16777215, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionVisor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isVisibleBox = QtWidgets.QCheckBox(FunctionVisor)
        self.isVisibleBox.setObjectName("isVisibleBox")
        self.verticalLayout_2.addWidget(self.isVisibleBox)
        self.isDotBox = QtWidgets.QCheckBox(FunctionVisor)
        self.isDotBox.setObjectName("isDotBox")
        self.verticalLayout_2.addWidget(self.isDotBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.name = QtWidgets.QLineEdit(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(0, 20))
        self.name.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setMaxLength(19)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.color = QtWidgets.QToolButton(FunctionVisor)
        self.color.setMinimumSize(QtCore.QSize(35, 30))
        self.color.setStyleSheet("background-color: rgb(0, 0, 0, 120);")
        self.color.setText("")
        self.color.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.color.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.color.setAutoRaise(False)
        self.color.setArrowType(QtCore.Qt.NoArrow)
        self.color.setObjectName("color")
        self.horizontalLayout.addWidget(self.color)
        self.deleteButton = QtWidgets.QToolButton(FunctionVisor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/trashButton/files/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QtCore.QSize(30, 35))
        self.deleteButton.setAutoRepeat(False)
        self.deleteButton.setAutoRaise(True)
        self.deleteButton.setArrowType(QtCore.Qt.NoArrow)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(FunctionVisor)
        QtCore.QMetaObject.connectSlotsByName(FunctionVisor)

    def retranslateUi(self, FunctionVisor):
        _translate = QtCore.QCoreApplication.translate
        FunctionVisor.setWindowTitle(_translate("FunctionVisor", "Form"))
        self.isVisibleBox.setText(_translate("FunctionVisor", "Visible"))
        self.isDotBox.setText(_translate("FunctionVisor", "Dots"))
        self.name.setText(_translate("FunctionVisor", "Nombre de "))
        self.deleteButton.setText(_translate("FunctionVisor", "..."))


from plot_tool.designer.resources import function_visor_resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FunctionVisor = QtWidgets.QWidget()
    ui = Ui_FunctionVisor()
    ui.setupUi(FunctionVisor)
    FunctionVisor.show()
    sys.exit(app.exec_())

