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
        FunctionVisor.resize(229, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FunctionVisor.sizePolicy().hasHeightForWidth())
        FunctionVisor.setSizePolicy(sizePolicy)
        FunctionVisor.setMinimumSize(QtCore.QSize(0, 0))
        FunctionVisor.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionVisor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isVisibleBox = QtWidgets.QCheckBox(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isVisibleBox.sizePolicy().hasHeightForWidth())
        self.isVisibleBox.setSizePolicy(sizePolicy)
        self.isVisibleBox.setText("")
        self.isVisibleBox.setChecked(False)
        self.isVisibleBox.setObjectName("isVisibleBox")
        self.horizontalLayout.addWidget(self.isVisibleBox)
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

