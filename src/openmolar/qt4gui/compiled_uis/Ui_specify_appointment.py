#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/specify_appointment.ui'
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
        Dialog.resize(593, 404)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(
            81,
            56,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.practix_comboBox = QtGui.QComboBox(Dialog)
        self.practix_comboBox.setObjectName(_fromUtf8("practix_comboBox"))
        self.gridLayout_3.addWidget(self.practix_comboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.apptlength_comboBox = QtGui.QComboBox(Dialog)
        self.apptlength_comboBox.setMaxVisibleItems(20)
        self.apptlength_comboBox.setObjectName(
            _fromUtf8("apptlength_comboBox"))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.apptlength_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.apptlength_comboBox, 1, 1, 1, 1)
        self.combinedApptcheckBox = QtGui.QCheckBox(Dialog)
        self.combinedApptcheckBox.setEnabled(False)
        self.combinedApptcheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combinedApptcheckBox.setObjectName(
            _fromUtf8("combinedApptcheckBox"))
        self.gridLayout_3.addWidget(self.combinedApptcheckBox, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(
            152,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 24))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 24))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.trt1_comboBox = QtGui.QComboBox(Dialog)
        self.trt1_comboBox.setMinimumSize(QtCore.QSize(176, 0))
        self.trt1_comboBox.setMaxVisibleItems(20)
        self.trt1_comboBox.setObjectName(_fromUtf8("trt1_comboBox"))
        self.gridLayout.addWidget(self.trt1_comboBox, 1, 0, 1, 1)
        self.trt2_comboBox = QtGui.QComboBox(Dialog)
        self.trt2_comboBox.setMinimumSize(QtCore.QSize(176, 0))
        self.trt2_comboBox.setMaxVisibleItems(20)
        self.trt2_comboBox.setObjectName(_fromUtf8("trt2_comboBox"))
        self.trt2_comboBox.addItem(_fromUtf8(""))
        self.trt2_comboBox.setItemText(0, _fromUtf8(""))
        self.gridLayout.addWidget(self.trt2_comboBox, 1, 1, 1, 1)
        self.trt3_comboBox = QtGui.QComboBox(Dialog)
        self.trt3_comboBox.setMinimumSize(QtCore.QSize(176, 0))
        self.trt3_comboBox.setMaxVisibleItems(20)
        self.trt3_comboBox.setObjectName(_fromUtf8("trt3_comboBox"))
        self.trt3_comboBox.addItem(_fromUtf8(""))
        self.trt3_comboBox.setItemText(0, _fromUtf8(""))
        self.gridLayout.addWidget(self.trt3_comboBox, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 24))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 3)
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scheduleNow_pushButton = QtGui.QPushButton(Dialog)
        self.scheduleNow_pushButton.setObjectName(
            _fromUtf8("scheduleNow_pushButton"))
        self.horizontalLayout_2.addWidget(self.scheduleNow_pushButton)
        spacerItem2 = QtGui.QSpacerItem(
            128,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("accepted()")),
            Dialog.accept)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("rejected()")),
            Dialog.reject)
        QtCore.QObject.connect(
            self.scheduleNow_pushButton,
            QtCore.SIGNAL(_fromUtf8("clicked()")),
            Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Enter an appointment"))
        self.label.setText(_("Appointment with"))
        self.label_2.setText(_("Length"))
        self.apptlength_comboBox.setItemText(0, _("5 minutes"))
        self.apptlength_comboBox.setItemText(1, _("10 minutes"))
        self.apptlength_comboBox.setItemText(2, _("15 minutes"))
        self.apptlength_comboBox.setItemText(3, _("20 minutes"))
        self.apptlength_comboBox.setItemText(4, _("30 minutes"))
        self.apptlength_comboBox.setItemText(5, _("40 minutes"))
        self.apptlength_comboBox.setItemText(6, _("45 minutes"))
        self.apptlength_comboBox.setItemText(7, _("1 hour"))
        self.apptlength_comboBox.setItemText(8, _("1 hour 15 minutes"))
        self.apptlength_comboBox.setItemText(9, _("1 hour 20 minutes"))
        self.apptlength_comboBox.setItemText(10, _("1 hour 30 minutes"))
        self.apptlength_comboBox.setItemText(11, _("1 hour 45 minutes"))
        self.apptlength_comboBox.setItemText(12, _("2 hours"))
        self.apptlength_comboBox.setItemText(13, _("2 hours 30 minutes"))
        self.apptlength_comboBox.setItemText(14, _("3 hours"))
        self.apptlength_comboBox.setItemText(15, _("other"))
        self.combinedApptcheckBox.setText(
            _("Combined Appointment With Hygenist?"))
        self.label_3.setText(_("Reason 1"))
        self.label_5.setText(_("Reason 3"))
        self.label_4.setText(_("Reason 2"))
        self.label_6.setText(_("Brief Note for Clinician (optional)"))
        self.scheduleNow_pushButton.setText(_("Schedule Appointment Now"))


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
