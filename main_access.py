# -*- coding: utf-8 -*-

import adodbapi
import sys
from PyQt4 import QtCore, QtGui
from ui import renrakusaki
from ui import shinki_ui
from ui import henshuu_ui
from ui import sakujo_ui
from ui import error_ui
#import os
#import openpyxl


class StartQT4(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = renrakusaki.Ui_MainWindow() 
        self.ui.setupUi(self)
        self.updateUi()
        QtCore.QObject.connect(self.ui.pushButton_shinki, QtCore.SIGNAL("clicked()"), self.onClickedShinki)
        QtCore.QObject.connect(self.ui.pushButton_henshuu, QtCore.SIGNAL("clicked()"), self.onClickedHenshuu)
        QtCore.QObject.connect(self.ui.pushButton_sakujo, QtCore.SIGNAL("clicked()"), self.onClickedSakujo)
        self.ui.tableWidget.setColumnWidth(0,0)
        self.ui.tableWidget.setColumnWidth(2,150)
        self.ui.tableWidget.setColumnWidth(3,50)
        self.ui.tableWidget.setColumnWidth(5,150)
        self.ui.tableWidget.setColumnWidth(9,200)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)   # ダブルクリックでの編集不可
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  # 一行ごとの選択モード
        self.ui.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection) # 一行のみ選択モード（複数行選択不可）
        self.ui.tableWidget.setCurrentCell(0, 0)

        self.shinki = Shinki()
        self.henshuu = Henshuu()
        self.sakujo = Sakujo()
        self.error = Error()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_F1:
            self.onClickedShinki()
        elif key == QtCore.Qt.Key_F2:
            self.onClickedHenshuu()
        elif key == QtCore.Qt.Key_F3:
            self.onClickedSakujo()
        elif key == QtCore.Qt.Key_F4:
            sys.exit(app.exec_())

    def onClickedShinki(self):
        self.shinki.show()
        self.SetEnabled_False()
    
    def onClickedHenshuu(self):
        rows = self.ui.tableWidget.currentRow()

        # connect to the database
        database = r"./data/Database1.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' %database
        conn = adodbapi.connect(constr)
        
        # create a cursor
        cur = conn.cursor()
        
        # extract all the data
        tablename = "address"
        sql = "select * from %s order by フリガナ" %tablename
        cur.execute(sql)

        # show the cursor
        global ID
        r = -1
        for row in cur:
            r += 1
            if row.種別 == "取引先":
                self.種別 = 0
            elif row.種別 == "家族":
                self.種別 = 1
            else:
                self.種別 = 2

            if r == rows:
                ID = row[0]
                self.henshuu.ui.lineEdit_name.setText(row.氏名)
                self.henshuu.ui.lineEdit_furigana.setText(row.フリガナ)
                self.henshuu.ui.comboBox.setCurrentIndex(self.種別)
                self.henshuu.ui.lineEdit_company.setText(row.会社名)
                self.henshuu.ui.lineEdit_address.setText(row.住所)
                self.henshuu.ui.lineEdit_phone.setText(row.電話番号)
                self.henshuu.ui.lineEdit_mobile.setText(row.携帯)
                self.henshuu.ui.lineEdit_Fax.setText(row.Fax)
                self.henshuu.ui.lineEdit_Email.setText(row.Email)

        try:
            if r < rows:
                ID2 = "{}".format(ID3)

        except NameError:
            myapp.error.show()

        else:
            self.henshuu.show()

        finally:
            self.SetEnabled_False()
            cur.close()
            conn.close()

    def onClickedSakujo(self):
        self.sakujo.show()
        self.SetEnabled_False()


    def SetEnabled_True(self):
        self.ui.pushButton_shinki.setEnabled(True)
        self.ui.pushButton_henshuu.setEnabled(True)
        self.ui.pushButton_sakujo.setEnabled(True)
        self.ui.pushButton_close.setEnabled(True)

    def SetEnabled_False(self):
        self.ui.pushButton_shinki.setEnabled(False)
        self.ui.pushButton_henshuu.setEnabled(False)
        self.ui.pushButton_sakujo.setEnabled(False)
        self.ui.pushButton_close.setEnabled(False)


    def updateUi(self):
        # connect to the database
        database = r"./data/Database1.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' %database
        conn = adodbapi.connect(constr)
        
        # create a cursor
        cur = conn.cursor()
        
        # extract all the data
        tablename = "address"
        sql = "select * from %s order by フリガナ" %tablename
        cur.execute(sql)
        # show the cursor
        r = 0
        self.ui.tableWidget.setRowCount(1000)
        self.ui.tableWidget.setColumnCount(10)
        for row in cur:
            self.ui.tableWidget.setItem(r, 0, QtGui.QTableWidgetItem(row.ID))
            self.ui.tableWidget.setItem(r, 1, QtGui.QTableWidgetItem(row.氏名))
            self.ui.tableWidget.setItem(r, 2, QtGui.QTableWidgetItem(row.フリガナ))
            self.ui.tableWidget.setItem(r, 3, QtGui.QTableWidgetItem(row.種別))
            self.ui.tableWidget.setItem(r, 4, QtGui.QTableWidgetItem(row.会社名))
            self.ui.tableWidget.setItem(r, 5, QtGui.QTableWidgetItem(row.住所))
            self.ui.tableWidget.setItem(r, 6, QtGui.QTableWidgetItem(row.電話番号))
            self.ui.tableWidget.setItem(r, 7, QtGui.QTableWidgetItem(row.携帯))
            self.ui.tableWidget.setItem(r, 8, QtGui.QTableWidgetItem(row.Fax))
            self.ui.tableWidget.setItem(r, 9, QtGui.QTableWidgetItem(row.Email))
            r += 1

        # close the cursor and connection
        cur.close()
        conn.close()


    def dataClear(self):
        self.ui.tableWidget.setItem(r, 0, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 1, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 2, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 3, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 4, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 5, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 6, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 7, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 8, QtGui.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(r, 9, QtGui.QTableWidgetItem(""))


class Shinki(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = shinki_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.dataClear()
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)


    def onClickedOK(self):
        name     = (str(self.ui.lineEdit_name.text()))
        furigana = (str(self.ui.lineEdit_furigana.text()))
        category = (str(self.ui.comboBox.currentText()))
        company  = (str(self.ui.lineEdit_company.text()))
        address  = (str(self.ui.lineEdit_address.text()))
        phone    = (str(self.ui.lineEdit_phone.text()))
        mobile   = (str(self.ui.lineEdit_mobile.text()))
        Fax      = (str(self.ui.lineEdit_Fax.text()))
        Email    = (str(self.ui.lineEdit_Email.text()))


        # connect to the database
        database = r"./data/Database1.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' %database
        conn = adodbapi.connect(constr)
        
        # create a cursor
        cur = conn.cursor()
        
        # insert the data
        tablename = "address"
        field = "氏名, フリガナ, 種別, 会社名, 住所, 電話番号, 携帯, Fax, Email"
        values = "'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}'" \
                .format(name, furigana, category, company, address, phone, mobile, Fax, Email)
        sql = "insert into {0} ({1}) values ({2});".format(tablename, field, values)

        cur.execute(sql)
        conn.commit()
        
        # close the cursor and connection
        cur.close()
        conn.close()

        myapp.updateUi()
        myapp.SetEnabled_True()
        self.dataClear()

    def dataClear(self):
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_furigana.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.lineEdit_company.clear()
        self.ui.lineEdit_address.clear()
        self.ui.lineEdit_phone.clear()
        self.ui.lineEdit_mobile.clear()
        self.ui.lineEdit_Fax.clear()
        self.ui.lineEdit_Email.clear()

    def onClickedCancel(self):
        myapp.SetEnabled_True()
        self.dataClear()


class Henshuu(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = henshuu_ui.Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

    def onClickedOK(self):
        myapp.SetEnabled_True()
        name     = (str(self.ui.lineEdit_name.text()))
        furigana = (str(self.ui.lineEdit_furigana.text()))
        category = (str(self.ui.comboBox.currentText()))
        company  = (str(self.ui.lineEdit_company.text()))
        address  = (str(self.ui.lineEdit_address.text()))
        phone    = (str(self.ui.lineEdit_phone.text()))
        mobile   = (str(self.ui.lineEdit_mobile.text()))
        Fax      = (str(self.ui.lineEdit_Fax.text()))
        Email    = (str(self.ui.lineEdit_Email.text()))

        # connect to the database
        database = r"./data/Database1.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' %database
        conn = adodbapi.connect(constr)
        
        # create a cursor
        cur2 = conn.cursor()

        # update the data
        tablename = "address"
        values = """氏名 = '{0}', フリガナ = '{1}', 種別 = '{2}', 会社名 = '{3}', 住所 = '{4}',
                電話番号 = '{5}', 携帯 = '{6}', \"Fax\" = '{7}', \"Email\" = '{8}'""" \
                .format(name, furigana, category, company, address, phone, mobile, Fax, Email)
        sql = 'update {0} set {1} where "ID" = {2};'.format(tablename, values, ID)

        cur2.execute(sql)
        conn.commit()

        # close the cursor and connection
        cur2.close()
        conn.close()
        myapp.updateUi()


    def onClickedCancel(self):
        myapp.SetEnabled_True()



class Sakujo(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = sakujo_ui.Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)


    def onClickedOK(self):
        rows = myapp.ui.tableWidget.currentRow()
        myapp.SetEnabled_True()

        # connect to the database
        database = r"./data/Database1.mdb"
        constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s' %database
        conn = adodbapi.connect(constr)
        
        # create a cursor
        cur = conn.cursor()
        
        # extract all the data
        tablename = "address"
        sql = "select * from %s order by フリガナ" %tablename
        cur.execute(sql)
        global r
        r = -1
        for row in cur:
            r += 1
            if r == rows:
                ID = row

        # create a cursor
        cur2 = conn.cursor()

        # delete the data
        try:
            sql = "delete from {} where ID = {}".format(tablename, ID[0])

        except UnboundLocalError:
            myapp.error.show()
            myapp.SetEnabled_False()

        else:
            cur2.execute(sql)
            conn.commit()
            myapp.dataClear()

        # close the cursor and connection
        finally:
            cur.close()
            cur2.close()
            conn.close()
            myapp.updateUi()


    def onClickedCancel(self):
        myapp.SetEnabled_True()


class Error(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = error_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.onClickedCancel)


    def onClickedCancel(self):
        myapp.SetEnabled_True()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
