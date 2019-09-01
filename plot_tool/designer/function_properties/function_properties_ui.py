# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_properties_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(False)
        Form.resize(200, 146)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(30)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setObjectName("name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.color = QtWidgets.QPushButton(Form)
        self.color.setStyleSheet("background: rgb(0, 0, 0);")
        self.color.setText("")
        self.color.setObjectName("color")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.color)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.styleList = QtWidgets.QComboBox(Form)
        self.styleList.setObjectName("styleList")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.styleList)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.markerList = QtWidgets.QComboBox(Form)
        self.markerList.setObjectName("markerList")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.markerList)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.visible = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visible.sizePolicy().hasHeightForWidth())
        self.visible.setSizePolicy(sizePolicy)
        self.visible.setObjectName("visible")
        self.gridLayout.addWidget(self.visible, 0, 0, 1, 1)
        self.legend = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legend.sizePolicy().hasHeightForWidth())
        self.legend.setSizePolicy(sizePolicy)
        self.legend.setObjectName("legend")
        self.gridLayout.addWidget(self.legend, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Color"))
        self.label_3.setText(_translate("Form", "Style"))
        self.label_4.setText(_translate("Form", "Marker"))
        self.visible.setText(_translate("Form", "Visible"))
        self.legend.setText(_translate("Form", "Legend"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

