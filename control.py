import psycopg2
import getpass
from PyQt4 import QtCore, QtGui

def updateUi(cont, host, port):
    # connect to the database
    constr = "dbname=testdb host={} port={} user=postgres".format(host, port)
    conn = psycopg2.connect(constr)

    # create a cursor
    #cur = conn.cursor()
    userName = getpass.getuser()
    cur = conn.cursor(name=userName)
    
    # extract all the data
    tablename = "address"
    sql = "select * from {} order by フリガナ;".format(tablename)
    cur.execute(sql)
    row = cur.fetchone()

    # show the cursor
    r = 0
    cont.tableWidget.setRowCount(1000)
    cont.tableWidget.setColumnCount(10)
    while row is not None:
        cont.tableWidget.setItem(r, 0, QtGui.QTableWidgetItem(str(row[0])))
        cont.tableWidget.setItem(r, 1, QtGui.QTableWidgetItem(row[1]))
        cont.tableWidget.setItem(r, 2, QtGui.QTableWidgetItem(row[2]))
        cont.tableWidget.setItem(r, 3, QtGui.QTableWidgetItem(row[3]))
        cont.tableWidget.setItem(r, 4, QtGui.QTableWidgetItem(row[4]))
        cont.tableWidget.setItem(r, 5, QtGui.QTableWidgetItem(row[5]))
        cont.tableWidget.setItem(r, 6, QtGui.QTableWidgetItem(row[6]))
        cont.tableWidget.setItem(r, 7, QtGui.QTableWidgetItem(row[7]))
        cont.tableWidget.setItem(r, 8, QtGui.QTableWidgetItem(row[8]))
        cont.tableWidget.setItem(r, 9, QtGui.QTableWidgetItem(row[9]))
        row = cur.fetchone()
        r += 1
    cont.tableWidget.setCurrentCell(0, 0)
    # close the cursor and connection
    conn.commit()
    #cur.close()
    conn.close()

def Shinki(cont1):
    name     = (str(cont1.lineEdit_name.text()))
    furigana = (str(cont1.lineEdit_furigana.text()))
    category = (str(cont1.comboBox.currentText()))
    company  = (str(cont1.lineEdit_company.text()))
    address  = (str(cont1.lineEdit_address.text()))
    phone    = (str(cont1.lineEdit_phone.text()))
    mobile   = (str(cont1.lineEdit_mobile.text()))
    Fax      = (str(cont1.lineEdit_Fax.text()))
    Email    = (str(cont1.lineEdit_Email.text()))


    # connect to the database
    conn = psycopg2.connect("dbname=testdb host=localhost user=postgres")
    
    # create a cursor
    cur = conn.cursor()
    userName = getpass.getuser()
    #cur = conn.cursor(name=userName)
    
    # insert the data
    tablename = "address"
    field = '氏名, フリガナ, 種別, 会社名, 住所, 電話番号, 携帯, "Fax", "Email"'
    values = "'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}'" \
            .format(name, furigana, category, company, address, phone, mobile, Fax, Email)
    sql = "insert into {0} ({1}) values ({2});".format(tablename, field, values)
    cur.execute(sql)
    conn.commit()
    
    # close the cursor and connection
    cur.close()
    conn.close()

def Henshuu(cont2, cont2_2, ID, host, port):
    name     = (str(cont2.lineEdit_name.text()))
    furigana = (str(cont2.lineEdit_furigana.text()))
    category = (str(cont2.comboBox.currentText()))
    company  = (str(cont2.lineEdit_company.text()))
    address  = (str(cont2.lineEdit_address.text()))
    phone    = (str(cont2.lineEdit_phone.text()))
    mobile   = (str(cont2.lineEdit_mobile.text()))
    Fax      = (str(cont2.lineEdit_Fax.text()))
    Email    = (str(cont2.lineEdit_Email.text()))

    # connect to the database
    constr = "dbname=testdb host={} port={} user=postgres".format(host, port)
    conn = psycopg2.connect(constr)
    
    # create a cursor
    cur2 = conn.cursor()
    userName = getpass.getuser()
    #cur2 = conn.cursor(name=userName)

    # update the data
    tablename = "address"
    values = """氏名 = '{0}', フリガナ = '{1}', 種別 = '{2}', 会社名 = '{3}', 住所 = '{4}',
            電話番号 = '{5}', 携帯 = '{6}', \"Fax\" = '{7}', \"Email\" = '{8}'""" \
            .format(name, furigana, category, company, address, phone, mobile, Fax, Email)
    sql = 'update {0} set {1} where "ID" = {2};'.format(tablename, values, ID)

    try:
        cur2.execute(sql)
    except:
        cont2_2.show()
        control.SetEnabled_False(cont)
    finally:
        conn.commit()

        # close the cursor and connection
        cur2.close()
        conn.close()


def SetEnabled_True(cont):
    cont.pushButton_shinki.setEnabled(True)
    cont.pushButton_henshuu.setEnabled(True)
    cont.pushButton_sakujo.setEnabled(True)
    cont.pushButton_close.setEnabled(True)

def SetEnabled_False(cont):
    cont.pushButton_shinki.setEnabled(False)
    cont.pushButton_henshuu.setEnabled(False)
    cont.pushButton_sakujo.setEnabled(False)
    cont.pushButton_close.setEnabled(False)

def dataClear(cont1):
    cont1.lineEdit_name.clear()
    cont1.lineEdit_furigana.clear()
    cont1.comboBox.setCurrentIndex(0)
    cont1.lineEdit_company.clear()
    cont1.lineEdit_address.clear()
    cont1.lineEdit_phone.clear()
    cont1.lineEdit_mobile.clear()
    cont1.lineEdit_Fax.clear()
    cont1.lineEdit_Email.clear()

"""
def tableClear(cont):
    cont.tableWidget.clearContents()
"""

def SetColumnWidth(cont):
    cont.tableWidget.setColumnWidth(0,0)
    cont.tableWidget.setColumnWidth(2,150)
    cont.tableWidget.setColumnWidth(3,50)
    cont.tableWidget.setColumnWidth(5,150)
    cont.tableWidget.setColumnWidth(9,200)

