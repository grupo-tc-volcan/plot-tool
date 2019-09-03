# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter_visor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphPlotterVisor(object):
    def setupUi(self, GraphPlotterVisor):
        GraphPlotterVisor.setObjectName("GraphPlotterVisor")
        GraphPlotterVisor.resize(311, 356)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphPlotterVisor.sizePolicy().hasHeightForWidth())
        GraphPlotterVisor.setSizePolicy(sizePolicy)
        GraphPlotterVisor.setMaximumSize(QtCore.QSize(320, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(GraphPlotterVisor)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(GraphPlotterVisor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMaximumSize(QtCore.QSize(16777215, 400))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 293, 227))
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.xMinimum = QtWidgets.QDoubleSpinBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xMinimum.sizePolicy().hasHeightForWidth())
        self.xMinimum.setSizePolicy(sizePolicy)
        self.xMinimum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xMinimum.setFrame(True)
        self.xMinimum.setAlignment(QtCore.Qt.AlignCenter)
        self.xMinimum.setReadOnly(False)
        self.xMinimum.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.xMinimum.setPrefix("")
        self.xMinimum.setDecimals(4)
        self.xMinimum.setMinimum(-10000000.0)
        self.xMinimum.setMaximum(10000000.0)
        self.xMinimum.setObjectName("xMinimum")
        self.gridLayout.addWidget(self.xMinimum, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.xLabel = QtWidgets.QLineEdit(self.page)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout.addWidget(self.xLabel, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.name = QtWidgets.QLineEdit(self.page)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.xScale = QtWidgets.QComboBox(self.page)
        self.xScale.setObjectName("xScale")
        self.gridLayout.addWidget(self.xScale, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.xMagnitude = QtWidgets.QLineEdit(self.page)
        self.xMagnitude.setReadOnly(True)
        self.xMagnitude.setObjectName("xMagnitude")
        self.gridLayout.addWidget(self.xMagnitude, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.xMaximum = QtWidgets.QDoubleSpinBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xMaximum.sizePolicy().hasHeightForWidth())
        self.xMaximum.setSizePolicy(sizePolicy)
        self.xMaximum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xMaximum.setWrapping(False)
        self.xMaximum.setAlignment(QtCore.Qt.AlignCenter)
        self.xMaximum.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.xMaximum.setDecimals(4)
        self.xMaximum.setMinimum(-10000000.0)
        self.xMaximum.setMaximum(10000000.0)
        self.xMaximum.setObjectName("xMaximum")
        self.gridLayout.addWidget(self.xMaximum, 5, 1, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 293, 227))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(60)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yMagnitude = QtWidgets.QLineEdit(self.page_2)
        self.yMagnitude.setReadOnly(True)
        self.yMagnitude.setObjectName("yMagnitude")
        self.gridLayout_2.addWidget(self.yMagnitude, 3, 1, 1, 1)
        self.yScale = QtWidgets.QComboBox(self.page_2)
        self.yScale.setObjectName("yScale")
        self.gridLayout_2.addWidget(self.yScale, 2, 1, 1, 1)
        self.yLabel = QtWidgets.QLineEdit(self.page_2)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout_2.addWidget(self.yLabel, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.axes = QtWidgets.QComboBox(self.page_2)
        self.axes.setObjectName("axes")
        self.gridLayout_2.addWidget(self.axes, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.yMaximum = QtWidgets.QDoubleSpinBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yMaximum.sizePolicy().hasHeightForWidth())
        self.yMaximum.setSizePolicy(sizePolicy)
        self.yMaximum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.yMaximum.setAlignment(QtCore.Qt.AlignCenter)
        self.yMaximum.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.yMaximum.setDecimals(4)
        self.yMaximum.setMinimum(-10000000.0)
        self.yMaximum.setMaximum(1000000000.0)
        self.yMaximum.setObjectName("yMaximum")
        self.gridLayout_2.addWidget(self.yMaximum, 5, 1, 1, 1, QtCore.Qt.AlignRight)
        self.yMinimum = QtWidgets.QDoubleSpinBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yMinimum.sizePolicy().hasHeightForWidth())
        self.yMinimum.setSizePolicy(sizePolicy)
        self.yMinimum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.yMinimum.setAlignment(QtCore.Qt.AlignCenter)
        self.yMinimum.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.yMinimum.setDecimals(4)
        self.yMinimum.setMinimum(-10000000.0)
        self.yMinimum.setMaximum(10000000.0)
        self.yMinimum.setObjectName("yMinimum")
        self.gridLayout_2.addWidget(self.yMinimum, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.axesFaceColor = QtWidgets.QWidget(self.page_2)
        self.axesFaceColor.setObjectName("axesFaceColor")
        self.horizontalLayout_7.addWidget(self.axesFaceColor)
        self.axesFaceColorButton = QtWidgets.QToolButton(self.page_2)
        self.axesFaceColorButton.setObjectName("axesFaceColorButton")
        self.horizontalLayout_7.addWidget(self.axesFaceColorButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 6, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridVisible = QtWidgets.QCheckBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridVisible.sizePolicy().hasHeightForWidth())
        self.gridVisible.setSizePolicy(sizePolicy)
        self.gridVisible.setObjectName("gridVisible")
        self.horizontalLayout_10.addWidget(self.gridVisible)
        self.gridOption = QtWidgets.QComboBox(self.page_2)
        self.gridOption.setObjectName("gridOption")
        self.horizontalLayout_10.addWidget(self.gridOption)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 293, 227))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.faceColorView = QtWidgets.QWidget(self.page_3)
        self.faceColorView.setObjectName("faceColorView")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.faceColorView)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.faceColorView)
        self.faceColorButton = QtWidgets.QToolButton(self.page_3)
        self.faceColorButton.setObjectName("faceColorButton")
        self.horizontalLayout_2.addWidget(self.faceColorButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edgeColorView = QtWidgets.QWidget(self.page_3)
        self.edgeColorView.setObjectName("edgeColorView")
        self.horizontalLayout_5.addWidget(self.edgeColorView)
        self.edgeColorButton = QtWidgets.QToolButton(self.page_3)
        self.edgeColorButton.setObjectName("edgeColorButton")
        self.horizontalLayout_5.addWidget(self.edgeColorButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.legendFaceColorView = QtWidgets.QWidget(self.page_3)
        self.legendFaceColorView.setObjectName("legendFaceColorView")
        self.horizontalLayout_4.addWidget(self.legendFaceColorView)
        self.legendFaceColorButton = QtWidgets.QToolButton(self.page_3)
        self.legendFaceColorButton.setObjectName("legendFaceColorButton")
        self.horizontalLayout_4.addWidget(self.legendFaceColorButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.legendEdgeColorView = QtWidgets.QWidget(self.page_3)
        self.legendEdgeColorView.setObjectName("legendEdgeColorView")
        self.horizontalLayout_6.addWidget(self.legendEdgeColorView)
        self.legendEdgeColorButton = QtWidgets.QToolButton(self.page_3)
        self.legendEdgeColorButton.setObjectName("legendEdgeColorButton")
        self.horizontalLayout_6.addWidget(self.legendEdgeColorButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.visible = QtWidgets.QCheckBox(self.page_3)
        self.visible.setChecked(True)
        self.visible.setObjectName("visible")
        self.verticalLayout_3.addWidget(self.visible)
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.adjustButton = QtWidgets.QPushButton(GraphPlotterVisor)
        self.adjustButton.setObjectName("adjustButton")
        self.horizontalLayout_8.addWidget(self.adjustButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(GraphPlotterVisor)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GraphPlotterVisor)

    def retranslateUi(self, GraphPlotterVisor):
        _translate = QtCore.QCoreApplication.translate
        GraphPlotterVisor.setWindowTitle(_translate("GraphPlotterVisor", "Form"))
        self.label_4.setText(_translate("GraphPlotterVisor", "Minimum X"))
        self.label_3.setText(_translate("GraphPlotterVisor", "Scale X"))
        self.label_2.setText(_translate("GraphPlotterVisor", "Label X"))
        self.label_6.setText(_translate("GraphPlotterVisor", "Magnitude X"))
        self.label.setText(_translate("GraphPlotterVisor", "Name"))
        self.label_5.setText(_translate("GraphPlotterVisor", "Maximum X"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("GraphPlotterVisor", "General Settings"))
        self.label_12.setText(_translate("GraphPlotterVisor", "Magnitude Y"))
        self.label_10.setText(_translate("GraphPlotterVisor", "Minimum Y"))
        self.label_11.setText(_translate("GraphPlotterVisor", "Maximum Y"))
        self.label_9.setText(_translate("GraphPlotterVisor", "Scale Y"))
        self.label_18.setText(_translate("GraphPlotterVisor", "Axes Face Color"))
        self.label_7.setText(_translate("GraphPlotterVisor", "Axes"))
        self.label_8.setText(_translate("GraphPlotterVisor", "Label Y"))
        self.axesFaceColorButton.setText(_translate("GraphPlotterVisor", "..."))
        self.gridVisible.setText(_translate("GraphPlotterVisor", "Grid"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("GraphPlotterVisor", "Axes Settings"))
        self.label_13.setText(_translate("GraphPlotterVisor", "Face Color"))
        self.faceColorButton.setText(_translate("GraphPlotterVisor", "..."))
        self.label_14.setText(_translate("GraphPlotterVisor", "Edge Color"))
        self.edgeColorButton.setText(_translate("GraphPlotterVisor", "..."))
        self.label_15.setText(_translate("GraphPlotterVisor", "Legend Face Color"))
        self.legendFaceColorButton.setText(_translate("GraphPlotterVisor", "..."))
        self.label_16.setText(_translate("GraphPlotterVisor", "Legend Edge Color"))
        self.legendEdgeColorButton.setText(_translate("GraphPlotterVisor", "..."))
        self.visible.setText(_translate("GraphPlotterVisor", "Name Visible"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("GraphPlotterVisor", "Style Settings"))
        self.adjustButton.setText(_translate("GraphPlotterVisor", "Adjust Size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphPlotterVisor = QtWidgets.QWidget()
    ui = Ui_GraphPlotterVisor()
    ui.setupUi(GraphPlotterVisor)
    GraphPlotterVisor.show()
    sys.exit(app.exec_())

