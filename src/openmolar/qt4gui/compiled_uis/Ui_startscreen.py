#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/startscreen.ui'
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


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(276, 343)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(200, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/openmolar.svg")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(71, 16777215))
        self.password_lineEdit.setMaxLength(10)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.line = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.user1_lineEdit = QtGui.QLineEdit(Dialog)
        self.user1_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user1_lineEdit.setText(_fromUtf8(""))
        self.user1_lineEdit.setMaxLength(6)
        self.user1_lineEdit.setObjectName(_fromUtf8("user1_lineEdit"))
        self.gridLayout.addWidget(self.user1_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.user2_lineEdit = QtGui.QLineEdit(Dialog)
        self.user2_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user2_lineEdit.setMaxLength(6)
        self.user2_lineEdit.setObjectName(_fromUtf8("user2_lineEdit"))
        self.gridLayout.addWidget(self.user2_lineEdit, 1, 1, 1, 1)
        self.surgery_radioButton = QtGui.QRadioButton(Dialog)
        self.surgery_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.surgery_radioButton.setChecked(True)
        self.surgery_radioButton.setObjectName(
            _fromUtf8("surgery_radioButton"))
        self.gridLayout.addWidget(self.surgery_radioButton, 2, 0, 1, 2)
        self.reception_radioButton = QtGui.QRadioButton(Dialog)
        self.reception_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.reception_radioButton.setObjectName(
            _fromUtf8("reception_radioButton"))
        self.gridLayout.addWidget(self.reception_radioButton, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.advanced_frame = QtGui.QFrame(Dialog)
        self.advanced_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.advanced_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.advanced_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.advanced_frame.setObjectName(_fromUtf8("advanced_frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.advanced_frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line_2 = QtGui.QFrame(self.advanced_frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 0, 0, 1, 2)
        self.chosenServer_label = QtGui.QLabel(self.advanced_frame)
        self.chosenServer_label.setWordWrap(True)
        self.chosenServer_label.setObjectName(_fromUtf8("chosenServer_label"))
        self.gridLayout_3.addWidget(self.chosenServer_label, 1, 0, 2, 1)
        self.advanced_toolButton = QtGui.QToolButton(self.advanced_frame)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.advanced_toolButton.sizePolicy().hasHeightForWidth())
        self.advanced_toolButton.setSizePolicy(sizePolicy)
        self.advanced_toolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.advanced_toolButton.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextOnly)
        self.advanced_toolButton.setArrowType(QtCore.Qt.DownArrow)
        self.advanced_toolButton.setObjectName(
            _fromUtf8("advanced_toolButton"))
        self.gridLayout_3.addWidget(self.advanced_toolButton, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.advanced_frame, 6, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(
            20,
            40,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("accepted()")),
            Dialog.accept)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("rejected()")),
            Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("openMolar"))
        self.label_3.setText(_("System Password"))
        self.label.setText(_("User 1(required)"))
        self.label_2.setText(_("User 2 (optional)"))
        self.surgery_radioButton.setText(_("Surgery Machine"))
        self.reception_radioButton.setText(_("Reception Machine"))
        self.chosenServer_label.setText(_("TextLabel"))
        self.advanced_toolButton.setText(_("change"))

from openmolar.qt4gui import resources_rc

if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
