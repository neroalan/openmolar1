#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/toothProps.ui'
#
# Created: Sat Dec 14 19:08:51 2013
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
        Form.resize(150, 479)
        Form.setMinimumSize(QtCore.QSize(150, 459))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.edit_pushButton = QtGui.QPushButton(Form)
        self.edit_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/icons/pencil.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.edit_pushButton.setIcon(icon)
        self.edit_pushButton.setFlat(True)
        self.edit_pushButton.setObjectName(_fromUtf8("edit_pushButton"))
        self.horizontalLayout.addWidget(self.edit_pushButton)
        self.tooth_label = QtGui.QLabel(Form)
        self.tooth_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tooth_label.setFont(font)
        self.tooth_label.setText(_fromUtf8(""))
        self.tooth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tooth_label.setObjectName(_fromUtf8("tooth_label"))
        self.horizontalLayout.addWidget(self.tooth_label)
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
        self.clear_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clear_pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/eraser.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.clear_pushButton.setIcon(icon1)
        self.clear_pushButton.setFlat(True)
        self.clear_pushButton.setObjectName(_fromUtf8("clear_pushButton"))
        self.horizontalLayout.addWidget(self.clear_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.editframe = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editframe.sizePolicy().hasHeightForWidth())
        self.editframe.setSizePolicy(sizePolicy)
        self.editframe.setMinimumSize(QtCore.QSize(131, 24))
        self.editframe.setMaximumSize(QtCore.QSize(16777215, 24))
        self.editframe.setFrameShape(QtGui.QFrame.NoFrame)
        self.editframe.setFrameShadow(QtGui.QFrame.Plain)
        self.editframe.setObjectName(_fromUtf8("editframe"))
        self.verticalLayout.addWidget(self.editframe)
        self.comments_comboBox = QtGui.QComboBox(Form)
        self.comments_comboBox.setObjectName(_fromUtf8("comments_comboBox"))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.comments_comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comments_comboBox)
        self.frame = QtGui.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 120))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.am_pushButton = QtGui.QPushButton(Form)
        self.am_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.am_pushButton.setMaximumSize(QtCore.QSize(48, 24))
        self.am_pushButton.setAutoFillBackground(True)
        self.am_pushButton.setObjectName(_fromUtf8("am_pushButton"))
        self.horizontalLayout_2.addWidget(self.am_pushButton)
        self.co_pushButton = QtGui.QPushButton(Form)
        self.co_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.co_pushButton.setMaximumSize(QtCore.QSize(48, 24))
        self.co_pushButton.setAutoFillBackground(True)
        self.co_pushButton.setObjectName(_fromUtf8("co_pushButton"))
        self.horizontalLayout_2.addWidget(self.co_pushButton)
        self.gl_pushButton = QtGui.QPushButton(Form)
        self.gl_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.gl_pushButton.setMaximumSize(QtCore.QSize(48, 24))
        self.gl_pushButton.setAutoFillBackground(True)
        self.gl_pushButton.setObjectName(_fromUtf8("gl_pushButton"))
        self.horizontalLayout_2.addWidget(self.gl_pushButton)
        self.gold_pushButton = QtGui.QPushButton(Form)
        self.gold_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.gold_pushButton.setMaximumSize(QtCore.QSize(48, 24))
        self.gold_pushButton.setAutoFillBackground(True)
        self.gold_pushButton.setObjectName(_fromUtf8("gold_pushButton"))
        self.horizontalLayout_2.addWidget(self.gold_pushButton)
        self.porc_pushButton = QtGui.QPushButton(Form)
        self.porc_pushButton.setMinimumSize(QtCore.QSize(0, 20))
        self.porc_pushButton.setMaximumSize(QtCore.QSize(48, 24))
        self.porc_pushButton.setAutoFillBackground(True)
        self.porc_pushButton.setObjectName(_fromUtf8("porc_pushButton"))
        self.horizontalLayout_2.addWidget(self.porc_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ex_pushButton = QtGui.QPushButton(Form)
        self.ex_pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.ex_pushButton.setMaximumSize(QtCore.QSize(80, 40))
        self.ex_pushButton.setObjectName(_fromUtf8("ex_pushButton"))
        self.gridLayout_2.addWidget(self.ex_pushButton, 1, 0, 1, 1)
        self.rt_pushButton = QtGui.QPushButton(Form)
        self.rt_pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.rt_pushButton.setMaximumSize(QtCore.QSize(80, 40))
        self.rt_pushButton.setObjectName(_fromUtf8("rt_pushButton"))
        self.gridLayout_2.addWidget(self.rt_pushButton, 1, 1, 1, 1)
        self.leftTooth_pushButton = QtGui.QPushButton(Form)
        self.leftTooth_pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.leftTooth_pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leftTooth_pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/back.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.leftTooth_pushButton.setIcon(icon2)
        self.leftTooth_pushButton.setIconSize(QtCore.QSize(24, 18))
        self.leftTooth_pushButton.setFlat(True)
        self.leftTooth_pushButton.setObjectName(
            _fromUtf8("leftTooth_pushButton"))
        self.gridLayout_2.addWidget(self.leftTooth_pushButton, 0, 0, 1, 1)
        self.dressing_pushButton = QtGui.QPushButton(Form)
        self.dressing_pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.dressing_pushButton.setMaximumSize(QtCore.QSize(80, 40))
        self.dressing_pushButton.setObjectName(
            _fromUtf8("dressing_pushButton"))
        self.gridLayout_2.addWidget(self.dressing_pushButton, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 40))
        self.pushButton.setIconSize(QtCore.QSize(18, 24))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.rightTooth_pushButton = QtGui.QPushButton(Form)
        self.rightTooth_pushButton.setMinimumSize(QtCore.QSize(32, 24))
        self.rightTooth_pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.rightTooth_pushButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/forward.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.rightTooth_pushButton.setIcon(icon3)
        self.rightTooth_pushButton.setIconSize(QtCore.QSize(24, 18))
        self.rightTooth_pushButton.setFlat(True)
        self.rightTooth_pushButton.setObjectName(
            _fromUtf8("rightTooth_pushButton"))
        self.gridLayout_2.addWidget(self.rightTooth_pushButton, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.cb_scrollArea = QtGui.QScrollArea(Form)
        self.cb_scrollArea.setMinimumSize(QtCore.QSize(0, 140))
        self.cb_scrollArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cb_scrollArea.setWidgetResizable(True)
        self.cb_scrollArea.setObjectName(_fromUtf8("cb_scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 144, 147))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.cb_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.cb_scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.clear_pushButton.setToolTip(_("delete tooth data"))
        self.comments_comboBox.setItemText(0, _("ADD COMMENTS"))
        self.comments_comboBox.setItemText(1, _("!KUO"))
        self.comments_comboBox.setItemText(2, _("!Mobile Tooth"))
        self.comments_comboBox.setItemText(3, _("!Early Caries"))
        self.comments_comboBox.setItemText(4, _("!Filling Missing"))
        self.comments_comboBox.setItemText(5, _("!Chipped"))
        self.comments_comboBox.setItemText(6, _("!Cracked"))
        self.comments_comboBox.setItemText(7, _("!Poor Prognosis"))
        self.comments_comboBox.setItemText(8, _("!Extract Soon"))
        self.comments_comboBox.setItemText(9, _("!Implant required"))
        self.comments_comboBox.setItemText(10, _("DELETE COMMENTS"))
        self.am_pushButton.setText(_("AM"))
        self.co_pushButton.setText(_("CO"))
        self.gl_pushButton.setText(_("GL"))
        self.gold_pushButton.setText(_("Go"))
        self.porc_pushButton.setText(_("Po"))
        self.ex_pushButton.setToolTip(_("extract (plan only!)"))
        self.ex_pushButton.setText(_("EX"))
        self.rt_pushButton.setToolTip(_("root treatment"))
        self.rt_pushButton.setText(_("RT"))
        self.leftTooth_pushButton.setToolTip(_("Apply and move Back a tooth"))
        self.dressing_pushButton.setToolTip(_("porcelain veneer"))
        self.dressing_pushButton.setText(_("DR"))
        self.pushButton.setToolTip(_("Apply & Add Another Item"))
        self.pushButton.setText(_("&&"))
        self.rightTooth_pushButton.setToolTip(_("Apply & Move to Next Tooth"))

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
