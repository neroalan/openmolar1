#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/diary_widget.ui'
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
        Form.resize(732, 551)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.diary_tabWidget = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.diary_tabWidget.sizePolicy().hasHeightForWidth())
        self.diary_tabWidget.setSizePolicy(sizePolicy)
        self.diary_tabWidget.setObjectName(_fromUtf8("diary_tabWidget"))
        self.tab_dayview = QtGui.QWidget()
        self.tab_dayview.setObjectName(_fromUtf8("tab_dayview"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_dayview)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setMargin(3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_18 = QtGui.QFrame(self.tab_dayview)
        self.frame_18.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_18.setObjectName(_fromUtf8("frame_18"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setMargin(3)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.dayCalendar_frame = QtGui.QWidget(self.frame_18)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dayCalendar_frame.sizePolicy().hasHeightForWidth())
        self.dayCalendar_frame.setSizePolicy(sizePolicy)
        self.dayCalendar_frame.setMinimumSize(QtCore.QSize(200, 180))
        self.dayCalendar_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.dayCalendar_frame.setObjectName(_fromUtf8("dayCalendar_frame"))
        self.verticalLayout_19.addWidget(self.dayCalendar_frame)
        self.goTodayPushButton = QtGui.QPushButton(self.frame_18)
        self.goTodayPushButton.setEnabled(False)
        self.goTodayPushButton.setMaximumSize(QtCore.QSize(16777215, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/agt_reload.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.goTodayPushButton.setIcon(icon)
        self.goTodayPushButton.setObjectName(_fromUtf8("goTodayPushButton"))
        self.verticalLayout_19.addWidget(self.goTodayPushButton)
        self.day_view_control_frame = QtGui.QFrame(self.frame_18)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.day_view_control_frame.sizePolicy().hasHeightForWidth())
        self.day_view_control_frame.setSizePolicy(sizePolicy)
        self.day_view_control_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.day_view_control_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.day_view_control_frame.setLineWidth(0)
        self.day_view_control_frame.setObjectName(
            _fromUtf8("day_view_control_frame"))
        self.verticalLayout_19.addWidget(self.day_view_control_frame)
        self.horizontalLayout_3.addWidget(self.frame_18)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.dayView_splitter = QtGui.QSplitter(self.tab_dayview)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dayView_splitter.sizePolicy().hasHeightForWidth())
        self.dayView_splitter.setSizePolicy(sizePolicy)
        self.dayView_splitter.setMinimumSize(QtCore.QSize(0, 300))
        self.dayView_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.dayView_splitter.setObjectName(_fromUtf8("dayView_splitter"))
        self.gridLayout_2.addWidget(self.dayView_splitter, 1, 0, 1, 1)
        self.emergency_dayview_scroll_bar = QtGui.QScrollBar(self.tab_dayview)
        self.emergency_dayview_scroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.emergency_dayview_scroll_bar.setObjectName(
            _fromUtf8("emergency_dayview_scroll_bar"))
        self.gridLayout_2.addWidget(
            self.emergency_dayview_scroll_bar,
            1,
            1,
            1,
            1)
        self.appt_notes_webView = QtWebKit.QWebView(self.tab_dayview)
        self.appt_notes_webView.setMinimumSize(QtCore.QSize(0, 150))
        self.appt_notes_webView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.appt_notes_webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.appt_notes_webView.setObjectName(_fromUtf8("appt_notes_webView"))
        self.gridLayout_2.addWidget(self.appt_notes_webView, 2, 0, 1, 2)
        self.daymemo_label = QtGui.QLabel(self.tab_dayview)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.daymemo_label.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.daymemo_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.daymemo_label.setFont(font)
        self.daymemo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.daymemo_label.setObjectName(_fromUtf8("daymemo_label"))
        self.gridLayout_2.addWidget(self.daymemo_label, 0, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.diary_tabWidget.addTab(self.tab_dayview, _fromUtf8(""))
        self.tab_weekview = QtGui.QWidget()
        self.tab_weekview.setObjectName(_fromUtf8("tab_weekview"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_weekview)
        self.gridLayout_11.setMargin(3)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.frame_8 = QtGui.QFrame(self.tab_weekview)
        self.frame_8.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setMargin(3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.weekCalendar_frame = QtGui.QWidget(self.frame_8)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.weekCalendar_frame.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.weekCalendar_frame.setSizePolicy(sizePolicy)
        self.weekCalendar_frame.setMinimumSize(QtCore.QSize(30, 180))
        self.weekCalendar_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.weekCalendar_frame.setObjectName(_fromUtf8("weekCalendar_frame"))
        self.verticalLayout_3.addWidget(self.weekCalendar_frame)
        self.goto_current_week_PushButton = QtGui.QPushButton(self.frame_8)
        self.goto_current_week_PushButton.setEnabled(False)
        self.goto_current_week_PushButton.setMaximumSize(
            QtCore.QSize(16777215, 24))
        self.goto_current_week_PushButton.setIcon(icon)
        self.goto_current_week_PushButton.setObjectName(
            _fromUtf8("goto_current_week_PushButton"))
        self.verticalLayout_3.addWidget(self.goto_current_week_PushButton)
        self.week_view_control_frame = QtGui.QFrame(self.frame_8)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.week_view_control_frame.sizePolicy().hasHeightForWidth())
        self.week_view_control_frame.setSizePolicy(sizePolicy)
        self.week_view_control_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.week_view_control_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.week_view_control_frame.setLineWidth(0)
        self.week_view_control_frame.setObjectName(
            _fromUtf8("week_view_control_frame"))
        self.verticalLayout_3.addWidget(self.week_view_control_frame)
        self.gridLayout_11.addWidget(self.frame_8, 0, 0, 2, 1)
        self.weekView_splitter = QtGui.QSplitter(self.tab_weekview)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.weekView_splitter.sizePolicy().hasHeightForWidth())
        self.weekView_splitter.setSizePolicy(sizePolicy)
        self.weekView_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.weekView_splitter.setObjectName(_fromUtf8("weekView_splitter"))
        self.layoutWidget = QtGui.QWidget(self.weekView_splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.day1_frame = QtGui.QFrame(self.layoutWidget)
        self.day1_frame.setMinimumSize(QtCore.QSize(0, 60))
        self.day1_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day1_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day1_frame.setObjectName(_fromUtf8("day1_frame"))
        self.gridLayout.addWidget(self.day1_frame, 0, 0, 1, 1)
        self.day2_frame = QtGui.QFrame(self.layoutWidget)
        self.day2_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day2_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day2_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day2_frame.setObjectName(_fromUtf8("day2_frame"))
        self.gridLayout.addWidget(self.day2_frame, 0, 1, 1, 1)
        self.day3_frame = QtGui.QFrame(self.layoutWidget)
        self.day3_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day3_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day3_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day3_frame.setObjectName(_fromUtf8("day3_frame"))
        self.gridLayout.addWidget(self.day3_frame, 0, 2, 1, 1)
        self.day4_frame = QtGui.QFrame(self.layoutWidget)
        self.day4_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day4_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day4_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day4_frame.setObjectName(_fromUtf8("day4_frame"))
        self.gridLayout.addWidget(self.day4_frame, 0, 3, 1, 1)
        self.day5_frame = QtGui.QFrame(self.layoutWidget)
        self.day5_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day5_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day5_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day5_frame.setObjectName(_fromUtf8("day5_frame"))
        self.gridLayout.addWidget(self.day5_frame, 0, 4, 1, 1)
        self.appt_OV_Frame1 = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame1.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame1.setSizePolicy(sizePolicy)
        self.appt_OV_Frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame1.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame1.setObjectName(_fromUtf8("appt_OV_Frame1"))
        self.gridLayout.addWidget(self.appt_OV_Frame1, 1, 0, 1, 1)
        self.appt_OV_Frame2 = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame2.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame2.setSizePolicy(sizePolicy)
        self.appt_OV_Frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame2.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame2.setObjectName(_fromUtf8("appt_OV_Frame2"))
        self.gridLayout.addWidget(self.appt_OV_Frame2, 1, 1, 1, 1)
        self.appt_OV_Frame3 = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame3.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.appt_OV_Frame3.setSizePolicy(sizePolicy)
        self.appt_OV_Frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame3.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame3.setObjectName(_fromUtf8("appt_OV_Frame3"))
        self.gridLayout.addWidget(self.appt_OV_Frame3, 1, 2, 1, 1)
        self.appt_OV_Frame4 = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame4.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame4.setSizePolicy(sizePolicy)
        self.appt_OV_Frame4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame4.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame4.setObjectName(_fromUtf8("appt_OV_Frame4"))
        self.gridLayout.addWidget(self.appt_OV_Frame4, 1, 3, 1, 1)
        self.appt_OV_Frame5 = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame5.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.appt_OV_Frame5.setSizePolicy(sizePolicy)
        self.appt_OV_Frame5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame5.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame5.setObjectName(_fromUtf8("appt_OV_Frame5"))
        self.gridLayout.addWidget(self.appt_OV_Frame5, 1, 4, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.weekView_splitter)
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_23.setMargin(0)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.day6_frame = QtGui.QFrame(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.day6_frame.sizePolicy().hasHeightForWidth())
        self.day6_frame.setSizePolicy(sizePolicy)
        self.day6_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day6_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day6_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day6_frame.setObjectName(_fromUtf8("day6_frame"))
        self.verticalLayout_23.addWidget(self.day6_frame)
        self.appt_OV_Frame6 = QtGui.QFrame(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame6.sizePolicy(
            ).hasHeightForWidth(
            ))
        self.appt_OV_Frame6.setSizePolicy(sizePolicy)
        self.appt_OV_Frame6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame6.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame6.setObjectName(_fromUtf8("appt_OV_Frame6"))
        self.verticalLayout_23.addWidget(self.appt_OV_Frame6)
        self.day7_frame = QtGui.QFrame(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.day7_frame.sizePolicy().hasHeightForWidth())
        self.day7_frame.setSizePolicy(sizePolicy)
        self.day7_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day7_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.day7_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.day7_frame.setObjectName(_fromUtf8("day7_frame"))
        self.verticalLayout_23.addWidget(self.day7_frame)
        self.appt_OV_Frame7 = QtGui.QFrame(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.appt_OV_Frame7.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame7.setSizePolicy(sizePolicy)
        self.appt_OV_Frame7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.appt_OV_Frame7.setFrameShadow(QtGui.QFrame.Sunken)
        self.appt_OV_Frame7.setObjectName(_fromUtf8("appt_OV_Frame7"))
        self.verticalLayout_23.addWidget(self.appt_OV_Frame7)
        self.gridLayout_11.addWidget(self.weekView_splitter, 0, 1, 1, 1)
        self.diary_tabWidget.addTab(self.tab_weekview, _fromUtf8(""))
        self.tab_monthview = QtGui.QWidget()
        self.tab_monthview.setObjectName(_fromUtf8("tab_monthview"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_monthview)
        self.gridLayout_5.setMargin(3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.monthView_scrollArea = QtGui.QScrollArea(self.tab_monthview)
        self.monthView_scrollArea.setWidgetResizable(True)
        self.monthView_scrollArea.setObjectName(
            _fromUtf8("monthView_scrollArea"))
        self.scrollAreaWidgetContents_14 = QtGui.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(
            QtCore.QRect(0, 0, 702, 456))
        self.scrollAreaWidgetContents_14.setObjectName(
            _fromUtf8("scrollAreaWidgetContents_14"))
        self.monthView_scrollArea.setWidget(self.scrollAreaWidgetContents_14)
        self.gridLayout_5.addWidget(self.monthView_scrollArea, 0, 0, 1, 4)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(
            _fromUtf8("horizontalLayout_22"))
        spacerItem = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.aptOVprevmonth = QtGui.QPushButton(self.tab_monthview)
        self.aptOVprevmonth.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVprevmonth.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/back.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.aptOVprevmonth.setIcon(icon1)
        self.aptOVprevmonth.setObjectName(_fromUtf8("aptOVprevmonth"))
        self.horizontalLayout_22.addWidget(self.aptOVprevmonth)
        self.label_65 = QtGui.QLabel(self.tab_monthview)
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.horizontalLayout_22.addWidget(self.label_65)
        self.aptOVnextmonth = QtGui.QPushButton(self.tab_monthview)
        self.aptOVnextmonth.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVnextmonth.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/forward.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.aptOVnextmonth.setIcon(icon2)
        self.aptOVnextmonth.setObjectName(_fromUtf8("aptOVnextmonth"))
        self.horizontalLayout_22.addWidget(self.aptOVnextmonth)
        spacerItem1 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 1, 2, 1, 1)
        self.printMonth_pushButton = QtGui.QPushButton(self.tab_monthview)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/ps.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.printMonth_pushButton.setIcon(icon3)
        self.printMonth_pushButton.setObjectName(
            _fromUtf8("printMonth_pushButton"))
        self.gridLayout_5.addWidget(self.printMonth_pushButton, 1, 3, 1, 1)
        self.monthClinicians_checkBox = QtGui.QCheckBox(self.tab_monthview)
        self.monthClinicians_checkBox.setChecked(True)
        self.monthClinicians_checkBox.setObjectName(
            _fromUtf8("monthClinicians_checkBox"))
        self.gridLayout_5.addWidget(self.monthClinicians_checkBox, 1, 0, 1, 1)
        self.monthView_clinicians_pushButton = QtGui.QPushButton(
            self.tab_monthview)
        self.monthView_clinicians_pushButton.setObjectName(
            _fromUtf8("monthView_clinicians_pushButton"))
        self.gridLayout_5.addWidget(
            self.monthView_clinicians_pushButton,
            1,
            1,
            1,
            1)
        self.diary_tabWidget.addTab(self.tab_monthview, _fromUtf8(""))
        self.tab_yearview = QtGui.QWidget()
        self.tab_yearview.setObjectName(_fromUtf8("tab_yearview"))
        self.gridLayout_22 = QtGui.QGridLayout(self.tab_yearview)
        self.gridLayout_22.setMargin(3)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.year_textBrowser = QtGui.QTextBrowser(self.tab_yearview)
        self.year_textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.year_textBrowser.setObjectName(_fromUtf8("year_textBrowser"))
        self.gridLayout_22.addWidget(self.year_textBrowser, 0, 0, 1, 3)
        self.yearView_frame = QtGui.QFrame(self.tab_yearview)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.yearView_frame.sizePolicy().hasHeightForWidth())
        self.yearView_frame.setSizePolicy(sizePolicy)
        self.yearView_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yearView_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.yearView_frame.setObjectName(_fromUtf8("yearView_frame"))
        self.gridLayout_22.addWidget(self.yearView_frame, 1, 0, 1, 3)
        self.yearClinicians_checkBox = QtGui.QCheckBox(self.tab_yearview)
        self.yearClinicians_checkBox.setChecked(True)
        self.yearClinicians_checkBox.setObjectName(
            _fromUtf8("yearClinicians_checkBox"))
        self.gridLayout_22.addWidget(self.yearClinicians_checkBox, 2, 0, 1, 1)
        self.yearView_clinicians_pushButton = QtGui.QPushButton(
            self.tab_yearview)
        self.yearView_clinicians_pushButton.setObjectName(
            _fromUtf8("yearView_clinicians_pushButton"))
        self.gridLayout_22.addWidget(
            self.yearView_clinicians_pushButton,
            2,
            1,
            1,
            1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.aptOVprevyear = QtGui.QPushButton(self.tab_yearview)
        self.aptOVprevyear.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVprevyear.setText(_fromUtf8(""))
        self.aptOVprevyear.setIcon(icon1)
        self.aptOVprevyear.setObjectName(_fromUtf8("aptOVprevyear"))
        self.horizontalLayout_2.addWidget(self.aptOVprevyear)
        self.label_64 = QtGui.QLabel(self.tab_yearview)
        self.label_64.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.horizontalLayout_2.addWidget(self.label_64)
        self.aptOVnextyear = QtGui.QPushButton(self.tab_yearview)
        self.aptOVnextyear.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVnextyear.setText(_fromUtf8(""))
        self.aptOVnextyear.setIcon(icon2)
        self.aptOVnextyear.setObjectName(_fromUtf8("aptOVnextyear"))
        self.horizontalLayout_2.addWidget(self.aptOVnextyear)
        spacerItem3 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_22.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.diary_tabWidget.addTab(self.tab_yearview, _fromUtf8(""))
        self.tab_agenda = QtGui.QWidget()
        self.tab_agenda.setObjectName(_fromUtf8("tab_agenda"))
        self.gridLayout_agenda = QtGui.QGridLayout(self.tab_agenda)
        self.gridLayout_agenda.setMargin(3)
        self.gridLayout_agenda.setSpacing(3)
        self.gridLayout_agenda.setObjectName(_fromUtf8("gridLayout_agenda"))
        self.agenda_calendar_frame = QtGui.QWidget(self.tab_agenda)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.agenda_calendar_frame.sizePolicy().hasHeightForWidth())
        self.agenda_calendar_frame.setSizePolicy(sizePolicy)
        self.agenda_calendar_frame.setMinimumSize(QtCore.QSize(220, 180))
        self.agenda_calendar_frame.setMaximumSize(QtCore.QSize(220, 200))
        self.agenda_calendar_frame.setObjectName(
            _fromUtf8("agenda_calendar_frame"))
        self.gridLayout_agenda.addWidget(
            self.agenda_calendar_frame,
            0,
            0,
            1,
            1)
        self.agenda_frame = QtGui.QFrame(self.tab_agenda)
        self.agenda_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.agenda_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.agenda_frame.setObjectName(_fromUtf8("agenda_frame"))
        self.gridLayout_agenda.addWidget(self.agenda_frame, 0, 1, 3, 1)
        self.agenda_goTodayPushButton = QtGui.QPushButton(self.tab_agenda)
        self.agenda_goTodayPushButton.setEnabled(False)
        self.agenda_goTodayPushButton.setMinimumSize(QtCore.QSize(220, 0))
        self.agenda_goTodayPushButton.setMaximumSize(QtCore.QSize(220, 24))
        self.agenda_goTodayPushButton.setIcon(icon)
        self.agenda_goTodayPushButton.setObjectName(
            _fromUtf8("agenda_goTodayPushButton"))
        self.gridLayout_agenda.addWidget(
            self.agenda_goTodayPushButton,
            1,
            0,
            1,
            1)
        self.agenda_control_frame = QtGui.QFrame(self.tab_agenda)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred,
            QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.agenda_control_frame.sizePolicy().hasHeightForWidth())
        self.agenda_control_frame.setSizePolicy(sizePolicy)
        self.agenda_control_frame.setMinimumSize(QtCore.QSize(220, 0))
        self.agenda_control_frame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.agenda_control_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.agenda_control_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.agenda_control_frame.setLineWidth(0)
        self.agenda_control_frame.setObjectName(
            _fromUtf8("agenda_control_frame"))
        self.gridLayout_agenda.addWidget(self.agenda_control_frame, 2, 0, 1, 1)
        self.diary_tabWidget.addTab(self.tab_agenda, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.diary_tabWidget)

        self.retranslateUi(Form)
        self.diary_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.goTodayPushButton.setText(_("Go To Today"))
        self.daymemo_label.setText(_("TextLabel"))
        self.diary_tabWidget.setTabText(
            self.diary_tabWidget.indexOf(self.tab_dayview),
            _("Day View"))
        self.goto_current_week_PushButton.setText(_("View Current Week"))
        self.diary_tabWidget.setTabText(
            self.diary_tabWidget.indexOf(self.tab_weekview),
            _("Week View"))
        self.label_65.setText(_("Month"))
        self.printMonth_pushButton.setText(_("Print Month View"))
        self.monthClinicians_checkBox.setText(_("All Clinicians"))
        self.monthView_clinicians_pushButton.setText(_("Select Clinicians"))
        self.diary_tabWidget.setTabText(
            self.diary_tabWidget.indexOf(self.tab_monthview),
            _("Month View"))
        self.yearClinicians_checkBox.setText(_("All Clinicians"))
        self.yearView_clinicians_pushButton.setText(_("Select Clinicians"))
        self.label_64.setText(_("Year"))
        self.diary_tabWidget.setTabText(
            self.diary_tabWidget.indexOf(self.tab_yearview),
            _("Year View"))
        self.agenda_goTodayPushButton.setText(_("Go To Today"))
        self.diary_tabWidget.setTabText(
            self.diary_tabWidget.indexOf(self.tab_agenda),
            _("Agenda"))

from PyQt4 import QtWebKit
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
