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

'''
this module provides an html summary of the patient's details
'''

from __future__ import division

import datetime
import logging
import sys
from openmolar.settings import localsettings
from openmolar.dbtools import patient_class

LOGGER = logging.getLogger("openmolar")


def getAge(pt):
    '''
    display the patient's age in human readable form
    '''
    ageYears, months, isToday = pt.getAge()
    if isToday:
        return "<h5> %s %s</h5>" % (ageYears, _("TODAY!"))
    if ageYears > 18:
        return "(%syo)" % ageYears
    else:

        html = "<br />%s %s" % (
            ageYears,
            _("years") if ageYears == 1 else _("year"))
        html += " %s %s" % (
            months,
            _("months") if months == 1 else _("month"))
        return html


def header(pt):
    html = '''
    <html>
    <head><link rel="stylesheet" href="%s" type="text/css"></head>
    <body><div align = "center">
    <h4>Patient %d</h4>
    <h3>%s %s %s</h3>
    %s %s<hr />
        ''' % (
        localsettings.stylesheet, pt.serialno, pt.title.title(),
        pt.fname.title(), pt.sname.title(),
        localsettings.formatDate(pt.dob), getAge(pt))

    address = (pt.addr1, pt.addr2, pt.addr3, pt.town, pt.county, pt.pcde)
    html += "<br />".join([l for l in address if l != ""])
    if pt.pcde == "":
        html += "<b>%s</b>" % _("!UNKNOWN POSTCODE!")

    if not pt.status in ("Active", "", None):
        html += "<hr /><h1>%s</h1>" % pt.status

    return html


def details(pt, Saved=True):
    '''returns an html set showing pt name etc...'''

    try:
        html = header(pt) + '<hr />'
        if "N" in pt.cset:
            html += '''<img src="%s/nhs_scot.png" alt="NHS" />
            <br />''' % localsettings.resources_path

            if pt.exemption != "":
                html += "%s=%s" % (_("exemption"), pt.exemption)
            else:
                html += _("NOT EXEMPT")
            html += "<br />"
        elif "I" in pt.cset:
            html += '''<img src="%s/hdp_small.png" alt="HDP" />
            <br />''' % localsettings.resources_path

        elif "P" in pt.cset:
            html += '''<img src="%s/private.png" alt="PRIVATE" />
            <br />''' % localsettings.resources_path

        else:
            html += '%s = %s <br />' % (_("UNKNOWN COURSETYPE"), pt.cset)

        html += "%s<br />" % pt.fee_table.briefName
        try:
            html += 'dentist      = %s' % localsettings.ops[pt.dnt1]
            if pt.dnt2 != 0 and pt.dnt1 != pt.dnt2:
                html += '/%s' % localsettings.ops[pt.dnt2]
        except KeyError as e:
            html += '<h4>%s</h4><hr />' % _(
                "Please Set a Dentist for this patient!")
        if pt.memo != '':
            html += '<h4>%s</h4>%s<hr />' % (_("Memo"), pt.memo)

        tx_dates = [
            (_("Treatment"), pt.last_treatment_date),
            (_("IO xrays"), pt.pd9),
            (_("Panoral"), pt.pd8),
            (_("Scaling"), pt.pd10)
        ]

        letype, le_date = "", datetime.date(1, 1, 1)
        for i, date_ in enumerate((pt.pd5, pt.pd6, pt.pd7)):
            if date_ and date_ > le_date:
                le_date = date_
                letype = ("(CE)", "(ECE)", "(FCA)")[i]
        if le_date == datetime.date(1, 1, 1):
            le_date = None
        if letype != "":
            tx_dates.append(('%s %s' % (_("Exam"), letype), le_date))

        html += '<h4>%s</h4><table width="100%%" border="1">' % _("History")
        for i, (att, val) in enumerate(tx_dates):

            html += '''<tr><td align="center">%s</td>
            <td align="center">%s%s%s</td></tr>''' % (
                att,
                "<b>" if i in (0, 4) else "",
                localsettings.formatDate(val),
                "</b>" if i in (0, 4) else "")

        html += "</table>"
        html += "<h4>%s</h4>" % _("Recall")
        if pt.recall_active:
            if pt.recd > localsettings.currentDay() or pt.has_exam_booked:
                html += "%s " % localsettings.formatDate(pt.recd)
                html += _("(exam booked)") if pt.has_exam_booked else ""
            else:
                html += '<div style="color:red;">%s</div>' % (
                    localsettings.formatDate(pt.recd))
        else:
            html += '<div style="color:red;">%s</div>' % _("DO NOT RECALL")

        alert = _("NOT SAVED") if not Saved else ""
        if pt.fees > 0:
            amount = localsettings.formatMoney(pt.fees)
            html += '<hr /><h3 class="debt">%s = %s %s</h3>' % (
                _("Account"), amount, alert)
        if pt.fees < 0:
            amount = localsettings.formatMoney(-pt.fees)
            html += '<hr /><h3>%s %s %s</h3>' % (amount, _("in credit"), alert)
        if pt.underTreatment:
            html += '<hr /><h2 class="ut_label">%s</h2><hr />' % _(
                "UNDER TREATMENT")
        return '''%s\n</div></body></html>''' % html
    except Exception as exc:
        LOGGER.exception("error in patientDetails.details")
        return "error displaying details, sorry <br />%s" % exc

if __name__ == '__main__':
    localsettings.initiate()
    localsettings.loadFeeTables()
    try:
        serialno = int(sys.argv[len(sys.argv) - 1])
    except:
        serialno = 4792
    print details(patient_class.patient(serialno))
