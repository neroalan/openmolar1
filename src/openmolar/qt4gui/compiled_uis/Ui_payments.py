#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/payments.ui'
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(226, 404)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.cash_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.cash_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.cash_pushButton.setObjectName(_fromUtf8("cash_pushButton"))
        self.gridLayout_2.addWidget(self.cash_pushButton, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.cheque_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.cheque_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.cheque_pushButton.setObjectName(_fromUtf8("cheque_pushButton"))
        self.gridLayout_2.addWidget(self.cheque_pushButton, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.debit_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.debit_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.debit_pushButton.setObjectName(_fromUtf8("debit_pushButton"))
        self.gridLayout_2.addWidget(self.debit_pushButton, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.credit_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.credit_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.credit_pushButton.setObjectName(_fromUtf8("credit_pushButton"))
        self.gridLayout_2.addWidget(self.credit_pushButton, 3, 2, 1, 1)
        self.cash_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.cash_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.cash_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cash_lineEdit.setMaxLength(10)
        self.cash_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cash_lineEdit.setObjectName(_fromUtf8("cash_lineEdit"))
        self.gridLayout_2.addWidget(self.cash_lineEdit, 0, 1, 1, 1)
        self.cheque_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.cheque_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.cheque_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cheque_lineEdit.setMaxLength(10)
        self.cheque_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cheque_lineEdit.setObjectName(_fromUtf8("cheque_lineEdit"))
        self.gridLayout_2.addWidget(self.cheque_lineEdit, 1, 1, 1, 1)
        self.debitCard_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.debitCard_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.debitCard_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.debitCard_lineEdit.setMaxLength(10)
        self.debitCard_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.debitCard_lineEdit.setObjectName(_fromUtf8("debitCard_lineEdit"))
        self.gridLayout_2.addWidget(self.debitCard_lineEdit, 2, 1, 1, 1)
        self.creditCard_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.creditCard_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.creditCard_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.creditCard_lineEdit.setMaxLength(10)
        self.creditCard_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.creditCard_lineEdit.setObjectName(
            _fromUtf8("creditCard_lineEdit"))
        self.gridLayout_2.addWidget(self.creditCard_lineEdit, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.sundries_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.sundries_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.sundries_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.sundries_lineEdit.setMaxLength(10)
        self.sundries_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sundries_lineEdit.setObjectName(_fromUtf8("sundries_lineEdit"))
        self.gridLayout.addWidget(self.sundries_lineEdit, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.annualHDP_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.annualHDP_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.annualHDP_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.annualHDP_lineEdit.setMaxLength(10)
        self.annualHDP_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.annualHDP_lineEdit.setObjectName(_fromUtf8("annualHDP_lineEdit"))
        self.gridLayout.addWidget(self.annualHDP_lineEdit, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.misc_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.misc_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.misc_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.misc_lineEdit.setMaxLength(10)
        self.misc_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.misc_lineEdit.setObjectName(_fromUtf8("misc_lineEdit"))
        self.gridLayout.addWidget(self.misc_lineEdit, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.total_doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.total_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.total_doubleSpinBox.setSizePolicy(sizePolicy)
        self.total_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.total_doubleSpinBox.setReadOnly(True)
        self.total_doubleSpinBox.setMaximum(20000.0)
        self.total_doubleSpinBox.setObjectName(
            _fromUtf8("total_doubleSpinBox"))
        self.horizontalLayout.addWidget(self.total_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Apply | QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.cash_lineEdit)
        self.label_2.setBuddy(self.cheque_lineEdit)
        self.label_3.setBuddy(self.debitCard_lineEdit)
        self.label_4.setBuddy(self.creditCard_lineEdit)
        self.label_8.setBuddy(self.sundries_lineEdit)
        self.label_7.setBuddy(self.annualHDP_lineEdit)
        self.label_9.setBuddy(self.misc_lineEdit)
        self.label_6.setBuddy(self.total_doubleSpinBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("rejected()")),
            Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.cash_lineEdit, self.cheque_lineEdit)
        Dialog.setTabOrder(self.cheque_lineEdit, self.debitCard_lineEdit)
        Dialog.setTabOrder(self.debitCard_lineEdit, self.creditCard_lineEdit)
        Dialog.setTabOrder(self.creditCard_lineEdit, self.sundries_lineEdit)
        Dialog.setTabOrder(self.sundries_lineEdit, self.annualHDP_lineEdit)
        Dialog.setTabOrder(self.annualHDP_lineEdit, self.misc_lineEdit)
        Dialog.setTabOrder(self.misc_lineEdit, self.total_doubleSpinBox)
        Dialog.setTabOrder(self.total_doubleSpinBox, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.cheque_pushButton)
        Dialog.setTabOrder(self.cheque_pushButton, self.credit_pushButton)
        Dialog.setTabOrder(self.credit_pushButton, self.debit_pushButton)
        Dialog.setTabOrder(self.debit_pushButton, self.cash_pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Payments"))
        self.groupBox_2.setTitle(_("Payments for treatment"))
        self.label.setText(_("Cash"))
        self.cash_pushButton.setText(_("-"))
        self.label_2.setText(_("Cheque"))
        self.cheque_pushButton.setText(_("-"))
        self.label_3.setText(_("Debit Card"))
        self.debit_pushButton.setText(_("-"))
        self.label_4.setText(_("Credit Card"))
        self.credit_pushButton.setText(_("-"))
        self.groupBox.setTitle(_("Other Payments"))
        self.label_8.setText(_("Sundries"))
        self.label_7.setText(_("Annual HDP"))
        self.label_9.setText(_("Miscellaneous"))
        self.label_6.setText(
            _("Amount which will appear on receipt  (read only)"))


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
