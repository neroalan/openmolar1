#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ############################################################################ #
# #                                                                          # #
# # Copyright (c) 2009-2014 Neil Wallace <neil@openmolar.com>                # #
# #                                                                          # #
# # This file is part of OpenMolar.                                          # #
# #                                                                          # #
# # OpenMolar is free software: you can redistribute it and/or modify        # #
# # it under the terms of the GNU General Public License as published by     # #
# # the Free Software Foundation, either version 3 of the License, or        # #
# # (at your option) any later version.                                      # #
# #                                                                          # #
# # OpenMolar is distributed in the hope that it will be useful,             # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of           # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            # #
# # GNU General Public License for more details.                             # #
# #                                                                          # #
# # You should have received a copy of the GNU General Public License        # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.       # #
# #                                                                          # #
# ############################################################################ #

import datetime
import logging
import time

from PyQt4 import QtCore, QtGui

from openmolar.settings import localsettings

from openmolar.dbtools import appointments
from openmolar.dbtools import search
from openmolar.dbtools.brief_patient import BriefPatient
from openmolar.ptModules import formatted_notes

from openmolar.qt4gui.dialogs import alterAday
from openmolar.qt4gui.dialogs import finalise_appt_time
from openmolar.qt4gui.dialogs import permissions
from openmolar.qt4gui.dialogs import choose_clinicians
from openmolar.qt4gui.dialogs.find_patient_dialog import FinalChoiceDialog
from openmolar.qt4gui.dialogs import begin_make_appt_dialog
from openmolar.qt4gui.dialogs.appointments_insert_blocks_dialog \
    import InsertBlocksDialog
from openmolar.qt4gui.dialogs.appointments_memo_dialog \
    import AppointmentsMemoDialog

from openmolar.qt4gui.customwidgets import appointmentwidget

from openmolar.qt4gui.printing import om_printing

from openmolar.qt4gui.compiled_uis import Ui_diary_widget

from openmolar.qt4gui.customwidgets.schedule_control \
    import DiaryScheduleController
from openmolar.qt4gui.customwidgets.diary_view_controller \
    import DiaryViewController

from openmolar.qt4gui.customwidgets.appointment_overviewwidget \
    import AppointmentOverviewWidget

from openmolar.qt4gui.customwidgets import aptOVcontrol
from openmolar.qt4gui.customwidgets import dent_hyg_selector
from openmolar.qt4gui.customwidgets import calendars

from openmolar.qt4gui.dialogs import appointment_card_dialog

LOGGER = logging.getLogger("openmolar")


class DiaryWidget(QtGui.QWidget):
    VIEW_MODE = 0
    SCHEDULING_MODE = 1
    BLOCKING_MODE = 2
    NOTES_MODE = 3

    appt_mode = VIEW_MODE

    pt = None
    finding_next_slot = 0  # -1 = backwards, 1 = forwards

    patient_card_request = QtCore.pyqtSignal(object)
    pt_diary_changed = QtCore.pyqtSignal(object)
    bring_to_front = QtCore.pyqtSignal()
    print_mh_signal = QtCore.pyqtSignal(object)

    alterAday_clipboard = []  # clipboard used by the alterAday dialog
    alterAday_clipboard_date = None

    message_alert = None
    laid_out = False

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_diary_widget.Ui_Form()
        self.ui.setupUi(self)
        self.appointmentData = appointments.DayAppointmentData()

        self.schedule_controller = DiaryScheduleController(self)
        self.view_controller = DiaryViewController(self)

        # keep a pointer to this layout as the layout is moved between
        # dayview and weekview
        self.appt_mode_layout = QtGui.QVBoxLayout(
            self.ui.day_view_control_frame)
        self.appt_mode_layout.setMargin(0)

        self.appt_mode_layout.addWidget(self.schedule_controller)
        self.appt_mode_layout.addStretch(0)
        self.appt_mode_layout.addWidget(self.view_controller)

        self.day_scroll_bar = None
        self.apptBookWidgets = []

        #-appointment OVerview widget
        self.ui.apptoverviews = []

        for frame in (self.ui.appt_OV_Frame1,
                      self.ui.appt_OV_Frame2,
                      self.ui.appt_OV_Frame3,
                      self.ui.appt_OV_Frame4,
                      self.ui.appt_OV_Frame5,
                      self.ui.appt_OV_Frame6,
                      self.ui.appt_OV_Frame7
                      ):
            bw = AppointmentOverviewWidget("0820", "1910", 10, 3, self)
            self.ui.apptoverviews.append(bw)

            hlayout = QtGui.QHBoxLayout(frame)
            hlayout.setMargin(2)
            hlayout.addWidget(bw)

        self.ui.apptoverviewControls = []

        for widg in (self.ui.day1_frame,
                     self.ui.day2_frame,
                     self.ui.day3_frame,
                     self.ui.day4_frame,
                     self.ui.day5_frame,
                     self.ui.day6_frame,
                     self.ui.day7_frame
                     ):
            hlayout = QtGui.QHBoxLayout(widg)
            hlayout.setMargin(0)
            control = aptOVcontrol.control()
            self.ui.apptoverviewControls.append(control)
            hlayout.addWidget(control)

        self.ui.weekView_splitter.setSizes([600, 10])

        self.appt_clinician_selector = dent_hyg_selector.dentHygSelector()
        self.monthClinicianSelector = dent_hyg_selector.dentHygSelector()

        #--customise the appointment widget calendar
        self.ui.dayCalendar = calendars.controlCalendar()
        self.calendar_layout = QtGui.QHBoxLayout(self.ui.dayCalendar_frame)
        self.calendar_layout.setMargin(0)
        self.calendar_layout.addWidget(self.ui.dayCalendar)

        self.ui.weekCalendar = calendars.weekCalendar()
        hlayout = QtGui.QHBoxLayout(self.ui.weekCalendar_frame)
        hlayout.setMargin(0)
        hlayout.addWidget(self.ui.weekCalendar)

        #--add a month view
        self.ui.monthView = calendars.monthCalendar()
        # hlayout=QtGui.QHBoxLayout(self.ui.monthView_frame)
        # hlayout.setMargin(0)
        # hlayout.addWidget(self.ui.monthView)
        self.ui.monthView_scrollArea.setWidget(self.ui.monthView)
        #--add a year view
        self.ui.yearView = calendars.yearCalendar()
        hlayout = QtGui.QHBoxLayout(self.ui.yearView_frame)
        hlayout.setMargin(0)
        hlayout.addWidget(self.ui.yearView)

        self.agenda_widget = QtGui.QTextBrowser()
        layout = QtGui.QVBoxLayout(self.ui.agenda_frame)
        layout.setMargin(0)
        layout.addWidget(self.agenda_widget)

        self.init_signals()

        self.ticker = QtCore.QTimer()
        self.ticker.start(30000)  # fire every 30 seconds
        self.ticker.timeout.connect(self.triangles)

    def initiate(self):
        LOGGER.debug("initialising diary clinicians")
        for selector in (self.appt_clinician_selector,
                         self.monthClinicianSelector):
            selector.set_dents(localsettings.activedents)
            selector.set_hygs(localsettings.activehygs)

    def showEvent(self, event):
        LOGGER.debug("ShowEvent called laid_out = %s", self.laid_out)
        if not self.laid_out:
            self.initiate()
            QtCore.QTimer.singleShot(10, self.layout_diary)

    def advise(self, arg, warning_level=0):
        '''
        inform the user of events -
        warning level0 = status bar only.
        warning level 1 advisory
        warning level 2 critical (and logged)
        '''
        def accept():
            self.message_alert.accept()

        if warning_level == 0:
            if self.message_alert is not None:
                accept()
            else:
                self.message_alert = QtGui.QMessageBox(self)
                self.message_alert.setStandardButtons(
                    QtGui.QMessageBox.NoButton)
                self.message_alert.setWindowTitle(_("advisory"))
                self.message_alert.setModal(False)

            self.message_alert.setText(arg)
            QtCore.QTimer.singleShot(3 * 1000, accept)
            self.message_alert.show()

        elif warning_level == 1:
            QtGui.QMessageBox.information(self, _("Advisory"), arg)

        elif warning_level == 2:
            now = QtCore.QTime.currentTime()
            QtGui.QMessageBox.warning(self, _("Error"), arg)
            #--for logging purposes
            LOGGER.warning("%d:%02d ERROR MESSAGE %s" % (
                now.hour(), now.minute(), arg))

    def reset(self):
        '''
        reset the tabwidget
        '''
        self.ui.diary_tabWidget.setCurrentIndex(0)
        self.ui.appt_notes_webView.setVisible(
            self.appt_mode == self.NOTES_MODE)

    def selected_date(self):
        '''
        a convenience function which calls a widget function
        (keeps code more readable)
        '''
        return self.ui.dayCalendar.selectedDate()

    def set_date(self, sd):
        '''
        a convenience function which calls a widget function
        (keeps code more readable)
        '''
        self.ui.dayCalendar.setSelectedDate(sd)

    def gotoToday_clicked(self):
        '''
        handles button pressed asking for today to be loaded on the
        appointments page
        '''
        self.gotoToday()

    def printMonth_pushButton_clicked(self):
        '''
        print the current Monthe View
        '''
        om_printing.printMonth(self)

    def appointment_book_print(self, dentist):
        '''
        print an appointment book
        '''
        adate = self.selected_date()
        try:
            books = ((dentist, adate), )
            om_printing.printdaylists(self, books)
        except KeyError:
            self.advise("error printing book", 1)

    def bookmemo_Edited(self, arg):
        '''
        user has double clicked on the appointment widget memo label
        '''
        dentist, memo = arg
        apptix = localsettings.apptix[dentist]
        if self.appointmentData.getMemo(apptix) != memo:
            appointments.setMemos(
                self.selected_date().toPyDate(),
                ((apptix, memo),))
            self.advise("adding day memo - %s %s" % (dentist, memo))

    def load_patient(self, patient, update=True):
        LOGGER.debug("DiaryWidget.load_patient, update=%s" % update)

        self.pt = patient
        if self.schedule_controller.pt != patient:
            self.schedule_controller.clear()
            self.schedule_controller.set_patient(patient)
        for book in self.apptBookWidgets:
            if patient is not None:
                book.selected_serialno = patient.serialno
            else:
                book.selected_serialno = None
            book.update()
        if update:
            self.layout_diary()

    def set_appt_mode(self, mode, update_required=True):
        LOGGER.debug("DiaryWidget.set_appt_mode")
        if self.appt_mode == mode:
            return
        self.finding_next_slot = 0
        self.appt_mode = mode
        self.schedule_controller.set_mode(mode)
        self.view_controller.set_mode(mode)
        if mode == self.NOTES_MODE:
            self.ui.appt_notes_webView.setHtml(_("No patient Selected"))
            self.ui.diary_tabWidget.setCurrentIndex(0)
            self.set_date(QtCore.QDate.currentDate())

        else:
            self.pt = self.schedule_controller.pt
            serialno = 0 if self.pt is None else self.pt.serialno
            for book in self.apptBookWidgets:
                book.selected_serialno = serialno
                book.update()
        if update_required:
            self.layout_diary()

    def highlight_serialno(self, serialnos):
        '''
        a custom widget (dentist diary) has sent a signal that an
        appointment has been selected.
        the arg is a list of serial numbers
        '''
        serialno = serialnos[0]

        if self.appt_mode == self.NOTES_MODE:
            html = formatted_notes.todays_notes(serialno)
            self.ui.appt_notes_webView.setHtml(html)
            page = self.ui.appt_notes_webView.page()
            page.setLinkDelegationPolicy(page.DelegateAllLinks)

        # this next bit is useful in showing "double appointments"
        if self.appt_mode not in (self.SCHEDULING_MODE, self.BLOCKING_MODE):
            for book in self.apptBookWidgets:
                book.selected_serialno = serialno
                book.update()

    def apptBook_slot_clicked(self, dent, time, length):
        dt = datetime.datetime.combine(self.appointmentData.date, time)
        slot = appointments.FreeSlot(dt, dent, length)
        self.makeAppt(self.schedule_controller.appointment_model.currentAppt,
                      slot)

    def manage_month_and_year_View_clinicians(self):
        '''
        radiobutton toggling who's book to show on the appointment
        '''
        self.dl = choose_clinicians.dialog(self.monthClinicianSelector, self)
        self.dl.exec_()
        val = self.monthClinicianSelector.allChecked()
        self.ui.monthClinicians_checkBox.setChecked(val)
        self.ui.yearClinicians_checkBox.setChecked(val)
        self.layout_diary()

    def month_and_year_All_clinicians(self):
        '''
        checkbox has been clicked, if True, then checkAll
        '''
        if self.sender().isChecked():
            self.monthClinicianSelector.checkAll()
        else:
            self.monthClinicianSelector.checkAll(QtCore.Qt.Unchecked)
        self.layout_diary()

    def aptOVwidget_userHasChosen_slot(self, slot):
        '''
        user has been offered a slot, and accepted it.
        the argument provides the required details
        '''
        self.makeAppt(self.schedule_controller.appointment_model.currentAppt,
                      slot)

    def begin_makeAppt(self):
        '''
        make an appointment - switch user to "scheduling mode" and present the
        appointment overview to show possible appointments
        also handles both 1st appointment buttons
        '''
        LOGGER.debug("DiaryWidget.begin_makeAppt")
        self.ui.appt_notes_webView.setVisible(False)

        self.schedule_controller.set_mode(
            self.schedule_controller.SCHEDULE_MODE)

        appt = self.schedule_controller.appointment_model.currentAppt
        if appt is None:
            self.advise(_("Please select an appointment to schedule"), 1)
            return
        if not appt.unscheduled:
            self.layout_diary()
            self.advise(_("appointment already scheduled for") + " %s" % (
                        localsettings.readableDate(appt.date)), 1)
            return

        begin_make_appt_dialog.WEEK_VIEW = self.viewing_week

        hyg_appt_selected = appt.dent in localsettings.activehyg_ixs

        begin_make_appt_dialog.ANY_HYGIENIST = hyg_appt_selected

        dl = begin_make_appt_dialog.BeginMakeApptDialog(self.pt, appt, self)

        if (hyg_appt_selected or
           self.schedule_controller.min_hyg_slot_length is None):
            dl.joint_appt_checkbox.setEnabled(False)

        if not dl.exec_():
            self.schedule_controller.reset()
            self.finding_next_slot = 0
            self.layout_diary()
            return

        # uncomment this line for debugging.
        # self.advise(dl.message, 1)

        # apply dialog settings
        self.schedule_controller.set_selection_mode(
            dl.clinician_selection_mode)

        self.schedule_controller.set_excluded_days(dl.excluded_days)
        self.schedule_controller.set_ignore_emergency_spaces(
            dl.ignore_emergency_spaces)

        self.schedule_controller.finding_joint_appointments = \
            dl.joint_appointment_search

        self.finding_next_slot = 1

        self.signals_calendar(False)
        if dl.start_search_criteria == dl.APPT_WEEKS_TIME:
            start_date = QtCore.QDate.currentDate().addDays(7)
        elif dl.start_search_criteria == dl.APPT_FOLLOW_ON:
            start_date = self.schedule_controller.last_appt_date
        else:
            start_date = QtCore.QDate.currentDate()

        self.set_date(start_date)
        self.ui.weekCalendar.setSelectedDate(start_date)
        self.signals_calendar()

        if dl.use_week_view:
            self.ui.diary_tabWidget.setCurrentIndex(1)
        else:
            self.ui.diary_tabWidget.setCurrentIndex(0)
        self.layout_diary()

    def weekViewAvailableSlots(self, get_hyg_slots=True):
        '''
        show slots on the appt overview widgets
        returns (arg1, arg2)
        arg1 is a boolean, whether the search was valid
        arg2 is a message
        arg3 is the appointments
        '''
        if not self.viewing_week:
            return ((), ())

        seldate = self.selected_date()

        if seldate.toPyDate() > localsettings.BOOKEND:
            message = (_("Reached") +
                       ' %s <br />' % localsettings.longDate(localsettings.BOOKEND) +
                       _("which is specified as the book end point"))
            return (False, message, ())

        dayno = seldate.dayOfWeek()
        weekdates = []
        for day in range(1, 8):
            weekdates.append(seldate.addDays(day - dayno))
        today = QtCore.QDate.currentDate()
        if today in weekdates:
            startday = today
        else:
            startday = weekdates[0]  # --monday
        sunday = weekdates[6]  # --sunday

        message = ""

        dents = self.schedule_controller.selectedClinicians
        #--check for suitable apts in the selected WEEK!

        slots = appointments.future_slots(
            startday.toPyDate(),
            sunday.toPyDate(),
            dents,
            self.schedule_controller.ignore_emergency_spaces)

        if get_hyg_slots:
            hyg_slots = appointments.future_slots(
                startday.toPyDate(),
                sunday.toPyDate(),
                localsettings.activehyg_ixs,
                self.schedule_controller.ignore_emergency_spaces)
        else:
            hyg_slots = ()
        dent_slots = appointments.getLengthySlots(slots,
                                                  self.schedule_controller.min_slot_length)

        hyg_slots = appointments.getLengthySlots(hyg_slots,
                                                 self.schedule_controller.min_hyg_slot_length)

        return (dent_slots, hyg_slots)

    def makeAppt(self, appt, slot):
        '''
        called by a click on my custom overview slot - or a drop event
        user has selected an offered appointment
        '''

        if not appt:
            self.advise(
                _("Please select an appointment to place here"), 1)
            return
        if appt.date:
            self.advise(
                _("Please choose another appointment - this one is made already!"), 1)
            return

        appointment_made = False
        selectedtime = localsettings.pyTimetoWystime(slot.time())
        slotlength = slot.length
        selectedDent = slot.dent
        if appt.dent and selectedDent != appt.dent:
            #--the user has selected a slot with a different dentist
            #--raise a dialog to check this was intentional!!
            message = _('You have chosen an appointment with') + " %s<br />" % (
                localsettings.apptix_reverse[selectedDent])
            message += _("Is this correct?")

            result = QtGui.QMessageBox.question(self, "Confirm", message,
                                                QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if result == QtGui.QMessageBox.No:
                # dialog rejected
                return

        if slotlength > appt.length:
            #--the slot selected is bigger than the appointment length so
            #--fire up a dialog to allow for fine tuning
            dl = finalise_appt_time.ftDialog(slot.time(), slotlength,
                                             appt.length, self)

            if dl.exec_():
                #--dialog accepted
                selectedtime = localsettings.pyTimetoWystime(dl.selectedTime)
                slotlength = appt.length  # satisfies the next conditional code
            else:
                #--dialog cancelled
                return

        if slotlength == appt.length:
            #--ok... suitable appointment found
            message = '''<center>%s<br />%s<br /><b>%s<br />%s
            <br />%s</b></center>''' % (
                _("Confirm Make appointment for"),
                appt.name,
                localsettings.wystimeToHumanTime(selectedtime),
                localsettings.readableDate(slot.date()),
                localsettings.apptix_reverse.get(selectedDent, "??"))

            #--get final confirmation
            result = QtGui.QMessageBox.question(self, "Confirm", message,
                                                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                                QtGui.QMessageBox.Yes)
            if result == QtGui.QMessageBox.No:
                # dialog rejected
                for widg in self.ui.apptoverviews:
                    widg.update()
                return

            #--make name conform to the 30 character sql limitation
            #--on this field.
            name = appt.name[:30]
            #--don't throw an exception with ord("")
            cst = 0
            try:
                cst = ord(appt.cset[0])
            except TypeError:
                pass
            except IndexError:
                pass

            endtime = localsettings.minutesPastMidnighttoWystime(
                localsettings.minutesPastMidnight(selectedtime) + appt.length)

            if self.schedule_controller.ignore_emergency_spaces:
                appointments.cancel_emergency_slot(
                    slot.date(), selectedDent, selectedtime, endtime)

            #-- make appointment
            if appointments.make_appt(
                slot.date(), selectedDent, selectedtime, endtime,
                appt.name[:30], appt.serialno, appt.trt1,
                    appt.trt2, appt.trt3, appt.memo, appt.flag, cst, 0, 0):

                if appt.serialno != 0:
                    if not appointments.pt_appt_made(
                        appt.serialno, appt.aprix, slot.date(),
                            selectedtime, selectedDent):

                        self.advise(
                            _("Error putting appointment back into patient diary"))

                    self.schedule_controller.get_data()
                    self.schedule_controller.set_chosen_appointment(None)
                    self.pt_diary_changed.emit(self.pt.serialno)

                    #== and offer an appointment card
                    if appointments.has_unscheduled(appt.serialno):
                        self.advise(_("more appointments to schedule"))
                    else:
                        self.offer_appointment_card()
                        self.set_appt_mode(self.VIEW_MODE)

            else:
                self.advise(u"<b>%s</b><hr /><em>%s<br />%s</em>" % (
                            _("Error making appointment - sorry!"),
                            _(
                            "It is most likely that another user utilised this space."),
                            _("Please try again.")
                            ), 2)
        else:
            # Hopefully this should never happen!!!!
            self.advise(
                "error - the appointment doesn't fit there.. slotlength " +
                "is %d and we need %d" % (slotlength, appt.length), 2)

        self.layout_diary()

    def apptOVheaderclick(self, arg):
        '''
        a click on the dentist portion of the appointment overview widget
        current implementation has little value!
        '''
        apptix, adate = arg
        LOGGER.debug("week header clicked apptix=%s date=%s", apptix, adate)

    def offer_appointment_card(self):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm",
                                            "Print Appointment Card?",
                                            QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                            QtGui.QMessageBox.Yes)
        if result == QtGui.QMessageBox.Yes:
            dl = appointment_card_dialog.AppointmentCardDialog(self.pt, self)
            dl.exec_()

    def triangles(self, call_update=True):
        ''''
        this moves a red line down the appointment books
        called by A Qtimer, or programmatically when adding data
        '''
        if self.ui.diary_tabWidget.currentIndex() == 0:
            currenttime = "%02d%02d" % (
                time.localtime()[3],
                time.localtime()[4])
            d = self.selected_date()
            if d == QtCore.QDate.currentDate():
                for book in self.apptBookWidgets:
                    if book.setCurrentTime(currenttime) and call_update:
                        book.update()
            else:
                for book in self.apptBookWidgets:
                    book.setCurrentTime(None)

    def aptFontSize(self, e):
        '''
        user selecting a different appointment book slot
        '''
        localsettings.appointmentFontSize = e
        for book in self.apptBookWidgets:
            book.update()
        for book in self.ui.apptoverviews:
            book.update()
        self.ui.monthView.update()
        self.ui.yearView.update()

    def aptOVlabelClicked(self, sd):
        '''
        go to the appointment book for the date on the label
        '''
        self.set_date(sd)
        self.ui.diary_tabWidget.setCurrentIndex(0)

    def aptOV_monthBack(self):
        '''
        appointment Overview page - change the calendar date,
        and let it's event handler do the rest
        '''
        self.set_date(self.selected_date().addMonths(-1))

    def aptOV_monthForward(self):
        '''
        appointment Overview page - change the calendar date,
        and let it's event handler do the rest
        '''
        self.set_date(self.selected_date().addMonths(1))

    def aptOV_yearBack(self):
        '''
        appointment Overview page - change the calendar date,
        and let it's event handler do the rest
        '''
        self.set_date(self.selected_date().addYears(-1))

    def aptOV_yearForward(self):
        '''
        appointment Overview page - change the calendar date,
        and let it's event handler do the rest
        '''
        self.set_date(self.selected_date().addYears(1))

    def gotoToday(self):
        '''
        appointment page - change the calendar date,
        and let it's event handler do the rest
        '''
        self.set_date(QtCore.QDate.currentDate())

    def clearTodaysEmergencyTime(self):
        '''
        clears emergency slots for today
        '''
        #-- raise a dialog to check
        result = QtGui.QMessageBox.question(self, "Confirm",
                                            "Clear today's emergency slots?",
                                            QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                            QtGui.QMessageBox.Yes)
        if result == QtGui.QMessageBox.Yes:
            number_cleared = appointments.clearEms(localsettings.currentDay())
            self.advise("Cleared %d emergency slots" % number_cleared, 1)
            self.layout_diary()

    def add_appointmentwidget(self):
        LOGGER.debug("initiating a new AppointmentWidget")
        book = appointmentwidget.AppointmentWidget(
            "0800", "1900", self)
        self.apptBookWidgets.append(book)
        self.ui.dayView_splitter.addWidget(book)
        self.signals_apptWidgets(book)
        book.mode = self.appt_mode
        if self.day_scroll_bar is None:
            self.day_scroll_bar = book.scrollArea.verticalScrollBar()
            self.ui.emergency_dayview_scroll_bar.valueChanged.connect(
                self.day_scroll_bar.setValue)

        if len(self.apptBookWidgets) > 1:
            self.apptBookWidgets[-1].set_scroll_bar(self.day_scroll_bar)
        for widg in self.apptBookWidgets[:-1]:
            widg.scroll_bar_off()

    def calendar_signal(self):
        '''
        called when the user clicks on the calendar
        (ie. NOT when called programatically by move_on)
        '''
        LOGGER.debug("DiaryWidget.calendar_signal")
        self.finding_next_slot = 0
        self.layout_diary()

    def layout_diary(self):
        '''
        slot to catch a date change from the custom mont/year widgets emitting
        a date signal
        OR the diary tab shifting
        OR the checkboxes have been tweaked
        OR a memo has been added
        '''
        LOGGER.debug("DiaryWidget.layout_diary")
        self.laid_out = True

        date_ = self.selected_date()
        self.ui.weekCalendar.setSelectedDate(date_)
        self.ui.monthView.setSelectedDate(date_.toPyDate())
        self.ui.yearView.setSelectedDate(date_.toPyDate())
        today = QtCore.QDate.currentDate()
        self.ui.goTodayPushButton.setEnabled(date_ != today)
        self.ui.goto_current_week_PushButton.setEnabled(
            date_.weekNumber() != today.weekNumber())

        self.ui.appt_notes_webView.setVisible(
            self.appt_mode == self.NOTES_MODE)
        self.schedule_controller.set_mode(self.appt_mode)

        i = self.ui.diary_tabWidget.currentIndex()

        if i == 0:
            self.layout_dayView()
        elif i == 1:
            self.layout_weekView()
        elif i == 2:
            self.layout_month()
        elif i == 3:
            self.layout_year()
            self.layout_yearHeader()
        elif i == 4:
            self.layout_agenda()

        if self.appt_mode == self.SCHEDULING_MODE:
            if date_ > localsettings.BOOKEND:
                self.advise(u'''<b>%s<br />%s %s</b><hr /><em>(%s)</em>
                <ul><li>%s</li><li>%s</li><li>%s</li></ul>''' % (
                            _("This date is beyond the diary limit."),
                            _(
                            "If the appointment wizard has brought you here"),
                            _(
                            "you should search again with different criteria."),
                            _("for instance..."),
                            _("no excluded days"),
                            _("ignore emergencies"),
                            _("add or view more clinicians.")), 1)

            elif date_ < localsettings.currentDay():
                self.advise(
                    _("You can't schedule an appointment in the past"),
                    1)
                self.set_date(localsettings.currentDay())

            elif (i in (0, 1) and self.schedule_controller.is_searching
                  and self.schedule_controller.chosen_slot is None):
                self.advise(_("No matching appointments found"))

    def layout_year(self):
        '''
        grab year memos
        '''
        LOGGER.debug("DiaryWidget.layout_year")

        year = self.selected_date().year()
        startdate = datetime.date(year, 1, 1)
        enddate = datetime.date(year + 1, 1, 1)

        dents = self.getUserCheckedClinicians()
        self.ui.yearView.setDents(dents)

        data = appointments.getDayInfo(startdate, enddate, dents)
        self.ui.yearView.setData(data)

        data = appointments.getBankHols(startdate, enddate)
        self.ui.yearView.setHeadingData(data)

        self.ui.yearView.update()

    def layout_yearHeader(self):
        '''
        put dayname, bank hol info, and any memos into the year header textBrowser
        '''
        dayData = self.ui.yearView.getDayData()
        # print dayData.dayName, dayData.publicHoliday, dayData.memos
        headerText = '''<html><head><link rel="stylesheet"
        href="%s" type="text/css"></head><body><div class="center">
        <table width="100%%">
        <tr><td colspan="3" class="yearheader">%s</td></tr>''' % (
            localsettings.stylesheet, dayData.dayName)

        if dayData.publicHoliday != "":
            headerText += '''<tr><td colspan="3" class="bankholiday">%s</td>
            </tr>''' % dayData.publicHoliday

        for dentix in dayData.dents.keys():
            dent = dayData.dents[dentix]
            if dentix == 0:
                headerText += '''<tr><td class="yearops" colspan="2">ALL</td>
                <td class="yearmemo">%s</td></tr>''' % dent.memo
            else:
                times = ""
                if dent.flag:
                    times = "%s - %s" % (
                        localsettings.wystimeToHumanTime(dent.start),
                        localsettings.wystimeToHumanTime(dent.end))

                headerText += '''<tr><td class="yearops">%s</td>
                <td class="yearops">%s</td>
                <td class="yearmemo">%s</td></tr>
                ''' % (dent.initials, times, dent.memo)
        headerText += "</table></body></html>"

        self.ui.year_textBrowser.setText(headerText)

    def layout_month(self):
        '''
        grab month memos
        '''
        LOGGER.debug("DiaryWidget.layout_month")

        qdate = self.selected_date()
        startdate = datetime.date(qdate.year(), qdate.month(), 1)

        qdate = qdate.addMonths(1)
        enddate = datetime.date(qdate.year(), qdate.month(), 1)

        dents = self.getUserCheckedClinicians()
        self.ui.monthView.setDents(dents)

        data = appointments.getDayInfo(startdate, enddate, dents)
        self.ui.monthView.setData(data)

        data = appointments.getBankHols(startdate, enddate)
        self.ui.monthView.setHeadingData(data)

        self.ui.monthView.update()

    def layout_weekView(self):
        '''
        lay out the week view widget
        called by checking a dentist checkbox on apptov tab
        or by changeing the date on the appt OV calendar
        '''
        if not self.viewing_week:
            return

        LOGGER.debug("DiaryWidget.layout_weekView")

        self.ui.week_view_control_frame.setLayout(self.appt_mode_layout)

        self.current_weekViewClinicians = set()
        date_ = self.selected_date()

        dayno = date_.dayOfWeek()
        weekdates = []

        for day in range(7):
            weekday = (date_.addDays(day + 1 - dayno))
            weekdates.append(weekday)
            header = self.ui.apptoverviewControls[day]
            header.setDate(weekday)
            pydate = weekday.toPyDate()
            memo = appointments.getBankHol(pydate)
            gm = appointments.getGlobalMemo(pydate)
            if memo != "" and gm != "":
                memo += "<br />"
            memo += gm
            header.setMemo(memo)

        thisWeek = QtCore.QDate.currentDate() in weekdates
        self.ui.goto_current_week_PushButton.setEnabled(not thisWeek)

        for ov in self.ui.apptoverviews:
            ov.date = weekdates[self.ui.apptoverviews.index(ov)]
            ov.clear()
            ov.mode = self.appt_mode

            ov.dents = \
                self.view_controller.clinician_days(ov.date.toPyDate())

            for dent in ov.dents:
                self.current_weekViewClinicians.add(dent.ix)

            ov.init_dicts()
            for dent in ov.dents:
                ov.setStartTime(dent)
                ov.setEndTime(dent)
                ov.setMemo(dent)
                ov.setFlags(dent)

        if self.appt_mode == self.SCHEDULING_MODE:
            if date_ < QtCore.QDate.currentDate():  # and not thisWeek):
                self.advise(
                    _("You can't schedule an appointment in the past"))
                # stop looking backwards
                self.finding_next_slot = 0
                # self.set_date(localsettings.currentDay())
                # return
            if date_ > localsettings.BOOKEND:
                # self.advise(_("You are beyond scheduling range"),1)
                self.finding_next_slot = 0
                available_slots = []
                self.schedule_controller.set_available_slots([])

            elif self.schedule_controller.finding_joint_appointments:

                dent_slots, hyg_slots = self.weekViewAvailableSlots()

                self.schedule_controller.set_joint_slots(
                    dent_slots, hyg_slots)

                if (self.finding_next_slot != 0 and
                   self.schedule_controller.search_again):
                    self.step_date(self.finding_next_slot != -1)
                    return

                if self.finding_next_slot == -1:
                    self.schedule_controller.use_last_slot = True
                    self.finding_next_slot = 1

            else:
                dent_slots, hyg_slots = self.weekViewAvailableSlots(False)
                self.schedule_controller.set_available_slots(dent_slots)

                if (self.finding_next_slot != 0 and
                   self.schedule_controller.search_again):
                    self.step_date(self.finding_next_slot != -1)
                    return

                if self.finding_next_slot == -1:
                    self.schedule_controller.use_last_slot = True
                    self.finding_next_slot = 1

            if self.schedule_controller.is_searching:
                for ov in self.ui.apptoverviews:
                    for slot in self.schedule_controller.available_slots:
                        if slot.date_time.date() == ov.date.toPyDate():
                            ov.addSlot(slot)
                    for slot in self.schedule_controller.hygienist_slots:
                        if slot.date_time.date() == ov.date.toPyDate():
                            ov.addSlot(slot)

                    ov.enable_clinician_slots(
                        self.schedule_controller.selectedClinicians)

                    ov.set_active_slots(
                        (self.schedule_controller.chosen_slot,
                         self.schedule_controller.chosen_hyg_slot)
                    )

        elif self.appt_mode == self.BLOCKING_MODE:
            available_slots, hyg_slots = self.weekViewAvailableSlots()
            for ov in self.ui.apptoverviews:
                ov.enable_clinician_slots(
                    localsettings.activedents + localsettings.activehygs)
                for slot in available_slots:
                    if slot.date_time.date() == ov.date.toPyDate():
                        ov.addSlot(slot)

        for ov in self.ui.apptoverviews:
            date_ = ov.date.toPyDate()
            for dent in ov.dents:
                ov.appts[dent.ix] = appointments.day_summary(date_, dent.ix)

        # add lunches and blocks
        for ov in self.ui.apptoverviews:
            date_ = ov.date.toPyDate()
            for dent in ov.dents:
                ov.eTimes[dent.ix] = appointments.getBlocks(date_, dent.ix)
                ov.lunches[dent.ix] = appointments.getLunch(date_, dent.ix)

        for ov in self.ui.apptoverviews:
            ov.update()

        # needed to sync agenda and dayview
        if self.schedule_controller.chosen_slot:
            sync_date = QtCore.QDate(
                self.schedule_controller.chosen_slot.date())
            LOGGER.debug("sync date%s" % sync_date)
            if (sync_date.weekNumber() ==
               self.ui.weekCalendar.selectedDate().weekNumber()):
                self.signals_calendar(False)
                self.ui.weekCalendar.setSelectedDate(sync_date)
                self.set_date(sync_date)
                self.signals_calendar()

    def layout_dayView(self):
        '''
        this populates the appointment book widgets (on maintab, pageindex 1)
        '''
        if not self.viewing_day:
            return

        LOGGER.debug("DiaryWidget.layout_dayView")
        self.ui.emergency_dayview_scroll_bar.hide()
        self.ui.dayCalendar_frame.setLayout(self.calendar_layout)
        self.ui.day_view_control_frame.setLayout(self.appt_mode_layout)

        for book in self.apptBookWidgets:
            book.clearAppts()
            book.setTime = None
            book.mode = self.appt_mode

        date_ = self.selected_date().toPyDate()

        # choose dentists to show.
        dents = self.view_controller.clinician_list(date_)

        self.appointmentData.setDate(date_)
        self.appointmentData.getAppointments(dents)

        if self.appt_mode == self.SCHEDULING_MODE:
            if (date_ < localsettings.currentDay() or
               date_ > localsettings.BOOKEND):
                self.finding_next_slot = 0
                available_slots = []
                self.schedule_controller.set_available_slots([])

            elif self.schedule_controller.finding_joint_appointments:
                dentists = []
                for dent in dents:
                    if dent in localsettings.activedent_ixs:
                        dentists.append(dent)

                dent_slots = self.appointmentData.slots(
                    self.schedule_controller.min_slot_length,
                    self.schedule_controller.ignore_emergency_spaces,
                    dentists
                )

                hyg_slots = self.appointmentData.slots(
                    self.schedule_controller.min_hyg_slot_length,
                    self.schedule_controller.ignore_emergency_spaces,
                    localsettings.activehyg_ixs
                )

                self.schedule_controller.set_joint_slots(
                    dent_slots, hyg_slots)

                if self.finding_next_slot == -1:
                    self.schedule_controller.use_last_slot = True
                    # self.finding_next_slot = 1

                if (self.finding_next_slot != 0 and
                   self.schedule_controller.search_again):
                    self.step_date(self.finding_next_slot != -1)
                    return

            else:
                minlength = self.schedule_controller.min_slot_length

                available_slots = self.appointmentData.slots(
                    minlength,
                    self.schedule_controller.ignore_emergency_spaces
                )
                self.schedule_controller.set_available_slots(available_slots)

                if self.finding_next_slot == -1:
                    self.schedule_controller.use_last_slot = True
                    # self.finding_next_slot = 1

                if (self.finding_next_slot != 0 and
                   self.schedule_controller.search_again):
                    self.step_date(self.finding_next_slot != -1)
                    return

        self.ui.daymemo_label.setText(self.appointmentData.memo)

        workingDents = self.appointmentData.workingDents
        number_of_books = len(workingDents)

        abs_start = self.appointmentData.earliest_start
        abs_end = self.appointmentData.latest_end

        while number_of_books > len(self.apptBookWidgets):
            self.add_appointmentwidget()

        #-- clean past links to dentists
        i = 0
        for book in self.apptBookWidgets:
            i += 1
            book.dentist = None
            book.setDayStartTime(abs_start)
            book.setDayEndTime(abs_end)

        if self.day_scroll_bar:
            self.day_scroll_bar.setValue(0)

        i = len(self.apptBookWidgets) - number_of_books
        for dent in workingDents:
            book = self.apptBookWidgets[i]

            book.setDentist(dent)

            book.setDayStartTime(abs_start)
            book.setDayEndTime(abs_end)

            bookstart = self.appointmentData.getStart(dent)
            bookend = self.appointmentData.getEnd(dent)

            book.setStartTime(bookstart)
            book.setEndTime(bookend)
            out = not self.appointmentData.inOffice.get(dent, False)
            book.setOutOfOffice(out)

            book.header_label.setText(localsettings.apptix_reverse[dent])

            book.memo_lineEdit.setText(self.appointmentData.getMemo(dent))

            apps = self.appointmentData.dentAppointments(dent)
            for app in apps:
                book.setAppointment(app)

            # if scheduling.. add slots to the widgets

            if (self.appt_mode == self.SCHEDULING_MODE
               and self.schedule_controller.is_searching):

                for slot in self.schedule_controller.available_slots:
                    book.addSlot(slot)

            # NEW CODE
                for slot in self.schedule_controller.hygienist_slots:
                    book.addSlot(slot)

                if not book.set_active_slot(
                        self.schedule_controller.chosen_slot):
                    book.set_active_slot(
                        self.schedule_controller.chosen_hyg_slot)
            # NEW CODE ENDS
                book.enable_slots(
                    book.apptix in
                    self.schedule_controller.selectedClinicians)

            i += 1

        self.triangles(False)

        book_list = []
        for book in self.apptBookWidgets:
            if book.dentist is None:
                #--book has no data
                book.hide()
                book_list.append(0)
            else:
                book_list.append(100)
                book.show()
                book.update()

        # make sure the splitter is reset (user could have hidden a widget they
        # now need)
        self.ui.dayView_splitter.setSizes(book_list)

        if i == 0:
            t = self.ui.daymemo_label.text() + " - " + _("No books to show!")
            self.ui.daymemo_label.setText(t)
            # self.advise("all off today")
        else:
            if self.apptBookWidgets[-1].outofoffice:
                esb = self.ui.emergency_dayview_scroll_bar

                esb.setMinimum(self.day_scroll_bar.minimum())
                esb.setMaximum(self.day_scroll_bar.maximum())
                esb.setPageStep(self.day_scroll_bar.pageStep())
                esb.setValue(self.day_scroll_bar.value())
                esb.show()

    def chosen_slot_changed(self):
        '''
        user has toggled the forwards and backwards buttons
        '''
        chosen_slot = self.schedule_controller.chosen_slot
        hyg_slot = self.schedule_controller.chosen_hyg_slot
        if self.viewing_week:
            for ov in self.ui.apptoverviews:
                ov.set_active_slots((chosen_slot, hyg_slot))
            for ov in self.ui.apptoverviews:
                ov.toggle_blink()
        elif self.viewing_day:
            for book in self.apptBookWidgets:
                if not book.set_active_slot(chosen_slot):
                    book.set_active_slot(hyg_slot)

            for book in self.apptBookWidgets:
                book.canvas.toggle_blink()

        if chosen_slot:
            sync_date = QtCore.QDate(chosen_slot.date())

            LOGGER.debug("chosen_slot sync date %s" % sync_date)
            self.signals_calendar(False)
            self.ui.weekCalendar.setSelectedDate(sync_date)
            self.set_date(sync_date)
            self.signals_calendar()

    def layout_agenda(self):
        '''
        this populates the diary agenda
        '''
        if self.ui.diary_tabWidget.currentIndex() != 4:
            return
        self.ui.agenda_calendar_frame.setLayout(self.calendar_layout)
        self.ui.agenda_control_frame.setLayout(self.appt_mode_layout)

        d = self.selected_date().toPyDate()

        agenda_data = appointments.AgendaData()

        self.appointmentData.setDate(d)
        self.appointmentData.getAppointments()

        if self.appt_mode == self.SCHEDULING_MODE:
            if d < localsettings.currentDay():
                # self.advise(_("You can't schedule an appointment in the past"))
                # stop looking backwards
                self.finding_next_slot = 0
                # self.set_date(localsettings.currentDay())
                # return
            minlength = self.schedule_controller.min_slot_length
            available_slots = self.appointmentData.slots(minlength)
            self.schedule_controller.set_available_slots(available_slots)

            if available_slots == []:
                self.step_date(self.finding_next_slot != -1)
                return
        else:
            available_slots = []

        for app in self.appointmentData.appointments:
            agenda_data.add_appointment(d, app)

        for slot in available_slots:
            agenda_data.add_slot(slot)

        if (self.appt_mode == self.SCHEDULING_MODE
           and self.schedule_controller.appointment_model.currentAppt):

            if self.finding_next_slot == -1:
                self.schedule_controller.use_last_slot = True
                self.finding_next_slot = 1

            agenda_data.set_active_slot(self.schedule_controller.chosen_slot)

        self.agenda_widget.setText(agenda_data.to_html())

    def getUserCheckedClinicians(self):
        '''
        checks the gui to see which dentists, hygienists are checked.
        returns a list
        '''
        retlist = []
        for dent in self.monthClinicianSelector.selectedClinicians:
            retlist.append(localsettings.apptix.get(dent))
        return tuple(retlist)

    def appointment_clicked(self, list_of_snos):
        if len(list_of_snos) == 1:
            sno = list_of_snos[0]
        else:
            candidates = search.getcandidates_from_serialnos(list_of_snos)
            dl = FinalChoiceDialog(candidates, self)
            dl.exec_()
            sno = dl.chosen_sno

        if sno is not None:
            serialno = int(sno)
            self.patient_card_request.emit(serialno)

    def edit_appointment_memo_clicked(self, list_of_snos, start, dentist):
        if len(list_of_snos) != 1:
            self.advise(
                _("multiple appointments selected, unable to edit memo"), 2)
            return
        sno = list_of_snos[0]
        adate = self.selected_date().toPyDate()
        atime = int(start.replace(":", ""))
        note, result = appointments.get_appt_note(sno, adate, atime, dentist)
        if not result:
            self.advise(_("unable to locate appointment memo, sorry"), 2)
        else:
            new_note, result = QtGui.QInputDialog.getText(
                self,
                _("New Memo"),
                _("Please enter Memo for this appointment"),
                text=note)
            if result and new_note != note:
                appointments.set_appt_note(
                    sno, adate, atime, dentist, new_note)

        self.layout_dayView()
        if self.pt:
            self.pt_diary_changed.emit(self.pt.serialno)

    def appointment_cancel(self, list_of_snos, start, dentist):
        if len(list_of_snos) != 1:
            self.advise("multiple appointments selected, unable to cancel", 2)
            return

        sno = list_of_snos[0]
        serialno = int(sno)
        adate = self.selected_date().toPyDate()
        dent_inits = localsettings.apptix_reverse.get(dentist)

        message = _("Confirm Delete appointment at")
        message += " %s %s " % (start, localsettings.readableDate(adate))
        message += _("with") + " %s?" % dent_inits

        if QtGui.QMessageBox.question(self, _("Confirm"), message,
                                      QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                      QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:

            appt = appointments.APR_Appointment()
            appt.atime = int(start.replace(":", ""))
            appt.dent = dentist
            appt.date = adate
            appt.serialno = serialno
            appt.aprix = "UNKNOWN"

            if appointments.delete_appt_from_aslot(appt):

                appointments.made_appt_to_proposed(appt)

                self.layout_dayView()
                self.schedule_controller.get_data()

                #--keep in the patient's diary?

                if QtGui.QMessageBox.question(
                    self,
                    _("Question"),
                    _("Removed from appointment book - "
                      "keep for rescheduling?"),
                    QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                        QtGui.QMessageBox.No) == QtGui.QMessageBox.No:
                    # remove from the patients diary
                    if appointments.delete_appt_from_apr(appt):
                        self.advise(_("Successfully removed appointment"))
                        self.schedule_controller.get_data()
                    else:
                        self.advise(_("Error removing from patient diary"), 2)

            else:
                #--aslot proc has returned False!
                # let the user know, and go no further
                self.advise(_("Error Removing from Appointment Book"), 2)
                self.layout_dayView()

        if self.pt is not None:
            self.pt_diary_changed.emit(self.pt.serialno)

    def clearEmergencySlot(self, arg):
        '''
        this function is the slot for a signal invoked when the user clicks
        on a "blocked" slot.
        only question is... do they want to free it?
        it expects an arg like ('8:50', '11:00', 4)
        '''
        adate = self.selected_date().toPyDate()
        message = _("Do you want to unblock the selected slot?")
        message += "<br />%s - %s <br />" % (arg[0], arg[1])
        message += "%s<br />" % localsettings.readableDate(adate)
        message += "with %s?" % localsettings.ops.get(arg[2])

        if QtGui.QMessageBox.question(
                self,
                _("Confirm"),
                message,
            QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
            appt = appointments.APR_Appointment()
            appt.atime = localsettings.humanTimetoWystime(arg[0])
            appt.date = adate
            appt.dent = arg[2]
            appointments.delete_appt_from_aslot(appt)
            self.layout_dayView()

    def blockEmptySlot(self, tup):
        '''
        block the empty slot
        '''
        adate = self.selected_date().toPyDate()
        start = tup[0].toPyTime()
        end = tup[1].toPyTime()
        adjstart = tup[2].toPyTime()
        adjend = tup[3].toPyTime()
        dent = tup[4]
        reason = tup[5]
        if not appointments.block_appt(adate, dent, start, end,
                                       adjstart, adjend, reason):
            self.advise(
                _("unable to block - "
                  "has the book been altered elsewhere?"), 1)
        self.layout_dayView()

    def fillEmptySlot(self, tup):
        '''
        fill the empty slot - this is called via the appointment widget.
        '''
        adate = self.selected_date().toPyDate()
        start = tup[0].toPyTime()
        end = tup[1].toPyTime()
        adjstart = tup[2].toPyTime()
        adjend = tup[3].toPyTime()
        pt = tup[6]
        dent = tup[4]
        reason = tup[5]
        if not appointments.fill_appt(adate, dent, start, end,
                                      adjstart, adjend, reason, pt):
            self.advise(
                _("unable to make appointment - "
                  "has the book been altered elsewhere?"), 1)
        self.layout_dayView()

        self.pt_diary_changed.emit(pt.serialno)

    def appt_dropped_onto_daywidget(self, appt, droptime, dent):
        '''
        appointment has been dropped onto a daybook widget
        appt is of type openmolar.dbtools.appointments.Appointment
        droptime is a pytime
        dent = numeric representation of dentist who's book was involved
        '''
        date_time = datetime.datetime.combine(
            self.selected_date().toPyDate(),
            droptime)

        LOGGER.debug("appt dropped %s %s %s" % (date_time, dent, appt.length))
        slot = appointments.FreeSlot(date_time, dent, appt.length)
        self.makeAppt(appt, slot)

    def start_scheduling_current_patient(self):
        self.start_scheduling(self.pt)

    def start_scheduling(self, pt):
        LOGGER.debug("DiaryWidget.start_scheduling")
        self.set_appt_mode(self.SCHEDULING_MODE)
        self.load_patient(pt, update=False)
        self.begin_makeAppt()

    def find_appt(self, appt):
        LOGGER.debug("DiaryWidgetfind_appt %s" % appt)
        pt = BriefPatient(appt.serialno)
        self.load_patient(pt)
        self.set_appt_mode(self.VIEW_MODE)
        self.set_date(appt.date)
        self.bring_to_front.emit()

    def aptOVlabelRightClicked(self, d):
        '''
        user wants to change appointment overview properties for date d
        '''
        if permissions.granted(self):
            dl = alterAday.alterDayDialog(self, d)

            if dl.getInput():
                self.layout_weekView()

    def insert_regular_blocks(self):
        '''
        insert blocks and appointments
        '''
        dl = InsertBlocksDialog()
        if dl.exec_():
            dl.apply()

    def diary_tabWidget_nav(self, i):
        '''
        catches a signal that the diary tab widget has been moved
        '''
        LOGGER.debug("diary_tabwidget_nav called")
        self.layout_diary()

    def schedule_controller_appointment_selected(self, appt):
        '''
        a new appointment has been selected for scheduling
        '''
        LOGGER.debug("DiaryWidget.schedule_controller_appointment_selected")

        self.finding_next_slot = 0
        self.schedule_controller.reset()
        self.layout_diary()

    def step_date(self, forwards=True):
        date_ = self.selected_date()
        LOGGER.debug("step date called current=%s, forwards=%s" % (
            date_, forwards))

        if forwards:
            if self.viewing_week:
                # goto 1st day of next week
                date_ = date_.addDays(1)
                while date_.dayOfWeek() != 1:
                    date_ = date_.addDays(1)
            else:
                date_ = date_.addDays(1)

            self.finding_next_slot = 1

        else:
            if self.viewing_week:
                # goto last day of next week
                date_ = date_.addDays(-1)
                while date_.dayOfWeek() != 7:
                    date_ = date_.addDays(-1)
            else:
                date_ = date_.addDays(-1)

            self.finding_next_slot = -1

        self.signals_calendar(False)
        self.set_date(date_)
        self.signals_calendar()
        self.layout_diary()

    def reset_and_view(self, patient):
        '''
        called when the diary is made visible by user navigating the mainUI
        tabwidget
        '''

        self.set_appt_mode(self.VIEW_MODE, update_required=False)
        self.ui.diary_tabWidget.setCurrentIndex(0)
        self.load_patient(patient, update=False)
        self.signals_calendar(False)
        self.set_date(localsettings.currentDay())
        self.signals_calendar()
        self.layout_diary()

    @property
    def viewing_day(self):
        '''
        is the user viewing a day?
        '''
        return self.ui.diary_tabWidget.currentIndex() == 0

    @property
    def viewing_week(self):
        '''
        is the user viewing a week?
        '''
        return self.ui.diary_tabWidget.currentIndex() == 1

    @property
    def viewing_agenda(self):
        '''
        is the user viewing a week?
        '''
        return self.ui.diary_tabWidget.currentIndex() == 4

    def memo_dialog(self, date_):
        dl = AppointmentsMemoDialog(date_, self)
        if dl.exec_():
            dl.apply()
            self.layout_diary()

    def edit_public_hol(self, date_):
        '''
        enter/modify the stored public holiday field
        '''
        LOGGER.debug("edit pub hol for %s", date_)
        current = appointments.getBankHol(date_)
        new, result = QtGui.QInputDialog.getText(
            self,
            _("Public Holidays"),
            _("Enter the information for ") + localsettings.longDate(date_),
            QtGui.QLineEdit.Normal,
            current)
        new_value = unicode(new.toUtf8())
        if result and current != new_value:
            appointments.setPubHol(date_, new_value)
            self.layout_diary()

    def init_signals(self):
        self.ui.diary_tabWidget.currentChanged.connect(
            self.diary_tabWidget_nav)

        self.ui.goTodayPushButton.clicked.connect(self.gotoToday_clicked)

        self.ui.goto_current_week_PushButton.clicked.connect(
            self.gotoToday_clicked)

        self.ui.printMonth_pushButton.clicked.connect(
            self.printMonth_pushButton_clicked)

        self.schedule_controller.patient_selected.connect(
            self.load_patient)

        self.signals_appointmentOVTab()

        self.schedule_controller.show_first_appointment.connect(
            self.begin_makeAppt)

        self.schedule_controller.move_on.connect(self.step_date)

        self.schedule_controller.chosen_slot_changed.connect(
            self.chosen_slot_changed)

        self.schedule_controller.appointment_selected.connect(
            self.schedule_controller_appointment_selected)

        self.schedule_controller.find_appt.connect(self.find_appt)
        self.schedule_controller.start_scheduling.connect(
            self.start_scheduling_current_patient)

        self.view_controller.update_needed.connect(
            self.layout_diary)

        self.view_controller.apt_mode_changed.connect(self.set_appt_mode)

    def signals_apptWidgets(self, book):

        book.connect(book, QtCore.SIGNAL("print_me"),
                     self.appointment_book_print)

        book.connect(book, QtCore.SIGNAL("new_memo"),
                     self.bookmemo_Edited)

        book.connect(book, QtCore.SIGNAL("PatientClicked"),
                     self.highlight_serialno)

        book.connect(book, QtCore.SIGNAL("AppointmentClicked"),
                     self.appointment_clicked)

        book.connect(book, QtCore.SIGNAL("EditAppointmentMemo"),
                     self.edit_appointment_memo_clicked)

        book.connect(book, QtCore.SIGNAL("AppointmentCancel"),
                     self.appointment_cancel)

        book.connect(book, QtCore.SIGNAL("ClearEmergencySlot"),
                     self.clearEmergencySlot)

        book.connect(book, QtCore.SIGNAL("BlockEmptySlot"),
                     self.blockEmptySlot)

        book.connect(book, QtCore.SIGNAL("Appointment_into_EmptySlot"),
                     self.fillEmptySlot)

        book.connect(book.canvas, QtCore.SIGNAL("ApptDropped"),
                     self.appt_dropped_onto_daywidget)

        book.slotClicked.connect(self.apptBook_slot_clicked)
        book.print_mh_signal.connect(self.print_mh_signal.emit)

    def signals_calendar(self, connect=True):
        if connect:
            self.ui.dayCalendar.selectionChanged.connect(self.calendar_signal)
        else:
            self.ui.dayCalendar.selectionChanged.disconnect(
                self.calendar_signal)

    def signals_appointmentOVTab(self):

        self.signals_calendar()

        QtCore.QObject.connect(self.ui.weekCalendar,
                               QtCore.SIGNAL("weekChanged"),
                               self.ui.dayCalendar.setSelectedDate)

        for cal in (self.ui.yearView, self.ui.monthView):
            cal.selected_date_signal.connect(
                self.ui.dayCalendar.setSelectedDate)
            cal.memo_dialog_signal.connect(self.memo_dialog)
            cal.public_holiday_signal.connect(self.edit_public_hol)

        self.ui.aptOVprevmonth.clicked.connect(self.aptOV_monthBack)
        self.ui.aptOVnextmonth.clicked.connect(self.aptOV_monthForward)
        self.ui.aptOVprevyear.clicked.connect(self.aptOV_yearBack)
        self.ui.aptOVnextyear.clicked.connect(self.aptOV_yearForward)
        self.ui.monthView_clinicians_pushButton.clicked.connect(
            self.manage_month_and_year_View_clinicians)
        self.ui.yearView_clinicians_pushButton.clicked.connect(
            self.manage_month_and_year_View_clinicians)
        self.ui.monthClinicians_checkBox.clicked.connect(
            self.month_and_year_All_clinicians)
        self.ui.yearClinicians_checkBox.clicked.connect(
            self.month_and_year_All_clinicians)

        for widg in self.ui.apptoverviews:
            widg.connect(widg, QtCore.SIGNAL("SlotClicked"),
                         self.aptOVwidget_userHasChosen_slot)

            widg.connect(widg, QtCore.SIGNAL("ApptDropped"),
                         self.makeAppt)

            widg.connect(widg, QtCore.SIGNAL("DentistHeading"),
                         self.apptOVheaderclick)

        for control in self.ui.apptoverviewControls:
            control.dayview_signal.connect(self.aptOVlabelClicked)
            control.edit_hours_signal.connect(self.aptOVlabelRightClicked)
            control.edit_memo_signal.connect(self.memo_dialog)


class _testDiary(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        dw = DiaryWidget()
        dw.initiate()
        dw.patient_card_request.connect(self.sig_catcher)

        from openmolar.dbtools import patient_class
        pt = patient_class.patient(1)
        dw.schedule_controller.set_patient(pt)

        self.setCentralWidget(dw)

        action1 = QtGui.QAction("clear emergency slots", self)
        action1.triggered.connect(dw.clearTodaysEmergencyTime)

        action2 = QtGui.QAction("insert regular blocks", self)
        action2.triggered.connect(dw.insert_regular_blocks)

        self.menuBar().addAction(action1)
        self.menuBar().addAction(action2)

    def sig_catcher(self, *args):
        print "signal caught", args

if __name__ == "__main__":
    LOGGER.setLevel(logging.DEBUG)
    import gettext
    import gettext
    gettext.install("openmolar")

    localsettings.initiate()

    app = QtGui.QApplication([])
    mw = _testDiary()
    mw.show()

    app.exec_()
