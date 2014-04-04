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

import MySQLdb
import sys
from openmolar.connect import connect
from openmolar.settings import localsettings


def write(sno, data):
    db = connect()
    cursor = db.cursor()

    result = True
    query = 'insert into mednotes (serialno,drnm,adrtel,curmed,oldmed,allerg,heart,lungs,liver,kidney,bleed,anaes,other,alert'
    dateToWrite = data[13]
    if dateToWrite is None:
        query += ") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (int(sno),) + data[:13]
    else:
        query += ",chkdate) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (int(sno),) + data[:13] + (dateToWrite,)
        print values
    try:
        cursor.execute("delete from mednotes where serialno=%d" % sno)
        cursor.execute(query, values)
    except Exception as e:
        print e
        result = False
    db.commit()
    cursor.close()
    # db.close()

    return result


def writeHist(sno, data):
    db = connect()
    cursor = db.cursor()

    for ix, note in data:
        query = '''insert into mnhist (serialno,chgdate,ix,note)
        values (%s, NOW(), %s, %s)'''
        values = (sno, ix, note)
        cursor.execute(query, values)
    db.commit()
    cursor.close()
    # db.close()

    return True

if __name__ == "__main__":
    import datetime
    newdata = (
        "doctor", "address", "curmeds", "pastmeds", "allergies", "heart", "lungs", "liver", "bleeding", "Kidneys",
        "ops", "other", True, datetime.date.today())
    write(11956, newdata)
    writeHist(11956, ((140, "new doctor"),))
