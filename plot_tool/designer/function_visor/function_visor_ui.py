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
        FunctionVisor.resize(184, 33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FunctionVisor.sizePolicy().hasHeightForWidth())
        FunctionVisor.setSizePolicy(sizePolicy)
        FunctionVisor.setMinimumSize(QtCore.QSize(0, 0))
        FunctionVisor.setMaximumSize(QtCore.QSize(16777215, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionVisor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.deleteButton = QtWidgets.QToolButton(FunctionVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/trashButton/files/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QtCore.QSize(25, 25))
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
        self.name.setText(_translate("FunctionVisor", "Name"))
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

