# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 350)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.type = QtWidgets.QComboBox(self.groupBox_2)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.horizontalLayout_2.addWidget(self.type)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frequencyModule = QtWidgets.QRadioButton(self.page)
        self.frequencyModule.setAutoExclusive(False)
        self.frequencyModule.setObjectName("frequencyModule")
        self.gridLayout_4.addWidget(self.frequencyModule, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frequencyPhase = QtWidgets.QRadioButton(self.page)
        self.frequencyPhase.setAutoExclusive(False)
        self.frequencyPhase.setObjectName("frequencyPhase")
        self.gridLayout_4.addWidget(self.frequencyPhase, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.step = QtWidgets.QRadioButton(self.page_3)
        self.step.setAutoExclusive(True)
        self.step.setObjectName("step")
        self.gridLayout_6.addWidget(self.step, 1, 0, 1, 1)
        self.importButton = QtWidgets.QPushButton(self.page_3)
        self.importButton.setMaximumSize(QtCore.QSize(120, 30))
        self.importButton.setObjectName("importButton")
        self.gridLayout_6.addWidget(self.importButton, 2, 0, 1, 1)
        self.impulsive = QtWidgets.QRadioButton(self.page_3)
        self.impulsive.setAutoExclusive(True)
        self.impulsive.setObjectName("impulsive")
        self.gridLayout_6.addWidget(self.impulsive, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.bodeModule = QtWidgets.QRadioButton(self.page_2)
        self.bodeModule.setAutoExclusive(False)
        self.bodeModule.setObjectName("bodeModule")
        self.gridLayout_5.addWidget(self.bodeModule, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.bodePhase = QtWidgets.QRadioButton(self.page_2)
        self.bodePhase.setAutoExclusive(False)
        self.bodePhase.setObjectName("bodePhase")
        self.gridLayout_5.addWidget(self.bodePhase, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.previewBox = QtWidgets.QGroupBox(Dialog)
        self.previewBox.setFlat(False)
        self.previewBox.setCheckable(False)
        self.previewBox.setObjectName("previewBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.previewBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.previewLayout = QtWidgets.QVBoxLayout()
        self.previewLayout.setObjectName("previewLayout")
        self.verticalLayout_2.addLayout(self.previewLayout)
        self.gridLayout_3.addWidget(self.previewBox, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.PolesZeros = QtWidgets.QWidget()
        self.PolesZeros.setObjectName("PolesZeros")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.PolesZeros)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.zeros = QtWidgets.QLineEdit(self.PolesZeros)
        self.zeros.setObjectName("zeros")
        self.gridLayout_2.addWidget(self.zeros, 2, 1, 1, 1)
        self.poles = QtWidgets.QLineEdit(self.PolesZeros)
        self.poles.setObjectName("poles")
        self.gridLayout_2.addWidget(self.poles, 1, 1, 1, 1)
        self.gain = QtWidgets.QLineEdit(self.PolesZeros)
        self.gain.setObjectName("gain")
        self.gridLayout_2.addWidget(self.gain, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.PolesZeros)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.PolesZeros)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.PolesZeros)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.PolesZeros, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.denominator = QtWidgets.QLineEdit(self.tab_2)
        self.denominator.setObjectName("denominator")
        self.gridLayout.addWidget(self.denominator, 1, 1, 1, 1)
        self.numerator = QtWidgets.QLineEdit(self.tab_2)
        self.numerator.setObjectName("numerator")
        self.gridLayout.addWidget(self.numerator, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 0)
        self.formLayout.setHorizontalSpacing(60)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.xMagnitude = QtWidgets.QComboBox(Dialog)
        self.xMagnitude.setObjectName("xMagnitude")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xMagnitude)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.yMagnitude = QtWidgets.QComboBox(Dialog)
        self.yMagnitude.setObjectName("yMagnitude")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yMagnitude)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalWidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalWidget.setFont(font)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.status = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.verticalLayout_3.addWidget(self.horizontalWidget)
        self.info = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.info.setFont(font)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setIndent(8)
        self.info.setObjectName("info")
        self.verticalLayout_3.addWidget(self.info)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.type.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Output Generated"))
        self.label_7.setText(_translate("Dialog", "Output type"))
        self.type.setItemText(0, _translate("Dialog", "Frequency Response"))
        self.type.setItemText(1, _translate("Dialog", "Temporal Response"))
        self.type.setItemText(2, _translate("Dialog", "Bode"))
        self.frequencyModule.setText(_translate("Dialog", "|H(f)| Module"))
        self.frequencyPhase.setText(_translate("Dialog", "H(f)° Phase"))
        self.step.setText(_translate("Dialog", "Step Response"))
        self.importButton.setText(_translate("Dialog", "Import Signal"))
        self.impulsive.setText(_translate("Dialog", "Impulsive Response"))
        self.bodeModule.setText(_translate("Dialog", "|H(f)| Module"))
        self.bodePhase.setText(_translate("Dialog", "H(f)° Phase"))
        self.previewBox.setTitle(_translate("Dialog", "Preview"))
        self.label_3.setText(_translate("Dialog", "Gain"))
        self.label_4.setText(_translate("Dialog", "Poles"))
        self.label_5.setText(_translate("Dialog", "Zeros"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PolesZeros), _translate("Dialog", "Poles and Zeros"))
        self.label.setText(_translate("Dialog", "Numerator"))
        self.label_2.setText(_translate("Dialog", "Denominator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Polynomial"))
        self.label_8.setText(_translate("Dialog", "Name"))
        self.label_9.setText(_translate("Dialog", "Magnitude X"))
        self.label_10.setText(_translate("Dialog", "Magnitude Y"))
        self.label_6.setText(_translate("Dialog", "Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
