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

from PyQt4 import QtGui, QtCore

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath("../../../"))

from openmolar.settings import localsettings
from openmolar.qt4gui.dialogs.base_dialogs import BaseDialog
from openmolar.qt4gui.phrasebook.phrasebook_dialog import PhraseBookDialog

from openmolar import connect
from openmolar.dbtools import patient_write_changes
from openmolar.dbtools import db_patients


class AlterTodaysNotesDialog(BaseDialog):
    result = ""
    patient_loaded = True

    def __init__(self, sno, parent):
        BaseDialog.__init__(self, parent)
        self.sno = sno
        self.notes = []

        self.main_ui = parent
        QtCore.QTimer.singleShot(0, self.get_todays_notes)
        self.text_edit = QtGui.QTextEdit(self)

        self.patient_label = QtGui.QLabel("searching for patient...")

        phrasebook_button = QtGui.QPushButton(_("Open Phrasebook"))
        phrasebook_button.clicked.connect(self.show_phrasebook)

        self.insertWidget(self.patient_label)
        self.insertWidget(self.text_edit)
        self.insertWidget(phrasebook_button)
        # self.text_edit.setLineWrapMode(self.text_edit.FixedColumnWidth)
        # self.text_edit.setLineWrapColumnOrWidth(80)

        QtCore.QTimer.singleShot(0, self.get_patient_name)

    def sizeHint(self):
        return QtCore.QSize(800, 200)

    def get_patient_name(self):
        try:
            self.patient_label.setText(db_patients.name(self.sno))
        except localsettings.PatientNotFoundError as exc:
            QtGui.QMessageBox.warning(self, "Error", exc.message)

    def show_phrasebook(self):
        dl = PhraseBookDialog(self)
        newNotes = ""
        if dl.exec_():
            for phrase in dl.selectedPhrases:
                newNotes += phrase + "\n"
            self.text_edit.append(newNotes)

    def get_todays_notes(self):
        query = '''select ix, note from formatted_notes
        where serialno = %s and ndate=DATE(NOW()) and ntype ="newNOTE"
        and op1 = %s and op2 = %s
        '''
        ops = localsettings.operator.split("/")
        op1 = ops[0]
        try:
            op2 = ops[1]
        except IndexError:
            op2 = None
            query = query.replace("op2 =", "op2 is")
        db = connect.connect()
        cursor = db.cursor()
        count = cursor.execute(query, (self.sno, op1, op2))
        rows = cursor.fetchall()
        cursor.close()

        if self.patient_loaded and not count:
            QtGui.QMessageBox.information(self, "message",
                                          "No notes found for today!")
            return

        text = ""
        for ix, note in rows:

            self.notes.append((ix, note))
            text += note
        self.text_edit.setText(text)

        self.text_edit.textChanged.connect(self.item_edited)

    def item_edited(self):
        self.enableApply()

    def apply_changed(self):
        lines = unicode(self.text_edit.toPlainText()).strip(" \n)").split("\n")
        short_lines = []
        for note in lines:
            while len(note) > 79:
                if " " in note[:79]:
                    pos = note[:79].rindex(" ")
                    #--try to split nicely
                elif "," in note[:79]:
                    pos = note[:79].rindex(",")
                    #--try to split nicely
                else:
                    pos = 79
                    #--ok, no option (unlikely to happen though)
                short_lines.append(note[:pos])
                note = note[pos + 1:]
            short_lines.append(note.strip(" \n") + "\n")

        values = []
        i = 0
        for ix, note in self.notes:
            try:
                values.append((short_lines[i], ix))
            except IndexError:  # a line has been deleted.
                values.append(("", ix))
            i += 1

        query = 'update formatted_notes set note=%s where ix=%s'

        db = connect.connect()
        cursor = db.cursor()
        cursor.executemany(query, tuple(values))
        cursor.close()

        if len(short_lines) > i:
            patient_write_changes.toNotes(
                self.sno,
                [("newNOTE", n) for n in short_lines[i:]]
                )

    def exec_(self):
        if BaseDialog.exec_(self):
            self.apply_changed()
            return True

if __name__ == "__main__":

    localsettings.initiate()
    localsettings.operator = "NW"
    app = QtGui.QApplication([])

    dl = AlterTodaysNotesDialog(11956, None)
    dl.exec_()
