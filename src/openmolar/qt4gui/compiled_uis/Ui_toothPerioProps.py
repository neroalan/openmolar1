#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/toothPerioProps.ui'
#
# Created: Wed Nov  6 23:05:24 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(499, 148)
        Form.setMinimumSize(QtCore.QSize(0, 120))
        Form.setMaximumSize(QtCore.QSize(16777215, 517))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tooth_label = QtGui.QLabel(Form)
        self.tooth_label.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tooth_label.setFont(font)
        self.tooth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tooth_label.setObjectName(_fromUtf8("tooth_label"))
        self.gridLayout.addWidget(self.tooth_label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 2)
        self.orig_frame = QtGui.QFrame(Form)
        self.orig_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.orig_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.orig_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.orig_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.orig_frame.setObjectName(_fromUtf8("orig_frame"))
        self.gridLayout.addWidget(self.orig_frame, 1, 0, 2, 1)
        self.new_frame = QtGui.QFrame(Form)
        self.new_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.new_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.new_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.new_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.new_frame.setObjectName(_fromUtf8("new_frame"))
        self.gridLayout.addWidget(self.new_frame, 1, 1, 2, 1)
        self.copy_pushButton = QtGui.QPushButton(Form)
        self.copy_pushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.copy_pushButton.setObjectName(_fromUtf8("copy_pushButton"))
        self.gridLayout.addWidget(self.copy_pushButton, 1, 2, 1, 1)
        self.cp_pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cp_pushButton.sizePolicy().hasHeightForWidth())
        self.cp_pushButton.setSizePolicy(sizePolicy)
        self.cp_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.cp_pushButton.setMaximumSize(QtCore.QSize(40, 28))
        self.cp_pushButton.setObjectName(_fromUtf8("cp_pushButton"))
        self.gridLayout.addWidget(self.cp_pushButton, 1, 3, 1, 1)
        self.clear_pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clear_pushButton.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.clear_pushButton.setSizePolicy(sizePolicy)
        self.clear_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.clear_pushButton.setMaximumSize(QtCore.QSize(40, 28))
        self.clear_pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/eraser.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.clear_pushButton.setIcon(icon)
        self.clear_pushButton.setObjectName(_fromUtf8("clear_pushButton"))
        self.gridLayout.addWidget(self.clear_pushButton, 1, 4, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leftTooth_pushButton = QtGui.QPushButton(Form)
        self.leftTooth_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.leftTooth_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.leftTooth_pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/back.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.leftTooth_pushButton.setIcon(icon1)
        self.leftTooth_pushButton.setIconSize(QtCore.QSize(24, 18))
        self.leftTooth_pushButton.setObjectName(
            _fromUtf8("leftTooth_pushButton"))
        self.horizontalLayout.addWidget(self.leftTooth_pushButton)
        self.le_frame = QtGui.QFrame(Form)
        self.le_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.le_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.le_frame.setObjectName(_fromUtf8("le_frame"))
        self.horizontalLayout.addWidget(self.le_frame)
        self.rightTooth_pushButton = QtGui.QPushButton(Form)
        self.rightTooth_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.rightTooth_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.rightTooth_pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/forward.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.rightTooth_pushButton.setIcon(icon2)
        self.rightTooth_pushButton.setIconSize(QtCore.QSize(24, 18))
        self.rightTooth_pushButton.setObjectName(
            _fromUtf8("rightTooth_pushButton"))
        self.horizontalLayout.addWidget(self.rightTooth_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 2)
        self.mobilitycomboBox = QtGui.QComboBox(Form)
        self.mobilitycomboBox.setMaximumSize(QtCore.QSize(16777215, 28))
        self.mobilitycomboBox.setObjectName(_fromUtf8("mobilitycomboBox"))
        self.mobilitycomboBox.addItem(_fromUtf8(""))
        self.mobilitycomboBox.addItem(_fromUtf8(""))
        self.mobilitycomboBox.addItem(_fromUtf8(""))
        self.mobilitycomboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.mobilitycomboBox, 2, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.tooth_label.setText(_("ToothId"))
        self.comboBox.setItemText(0, _("Pocketing"))
        self.comboBox.setItemText(1, _("Bleeding"))
        self.comboBox.setItemText(2, _("Plaque"))
        self.comboBox.setItemText(3, _("Recession"))
        self.comboBox.setItemText(4, _("Furcation"))
        self.comboBox.setItemText(5, _("Suppuration"))
        self.comboBox.setItemText(6, _("Mobility"))
        self.comboBox.setItemText(7, _("Other"))
        self.copy_pushButton.setText(_("Copy &All"))
        self.cp_pushButton.setToolTip(_("delete tooth data"))
        self.cp_pushButton.setText(_("Cp"))
        self.clear_pushButton.setToolTip(_("delete tooth data"))
        self.leftTooth_pushButton.setToolTip(_("Apply and move Back a tooth"))
        self.rightTooth_pushButton.setToolTip(_("Apply & Move to Next Tooth"))
        self.mobilitycomboBox.setItemText(0, _("-"))
        self.mobilitycomboBox.setItemText(1, _("I"))
        self.mobilitycomboBox.setItemText(2, _("II"))
        self.mobilitycomboBox.setItemText(3, _("III"))

from openmolar.qt4gui import resources_rc

if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
