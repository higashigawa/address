# -*- coding: utf-8 -*-

import psycopg2
import getpass
import sys
from PyQt4 import QtCore, QtGui
from ui import renrakusaki
from ui import shinki_ui
from ui import henshuu_ui
from ui import sakujo_ui
from ui import error_ui
import clipboard
import control
#import os
#import openpyxl

global host
global port
host = "localhost"
port = 5432

class StartQT4(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        global cont
        cont = self.ui = renrakusaki.Ui_MainWindow() 
        self.ui.setupUi(self)
        control.updateUi(cont, host, port)
        QtCore.QObject.connect(self.ui.pushButton_shinki, QtCore.SIGNAL("clicked()"), self.onClickedShinki)
        QtCore.QObject.connect(self.ui.pushButton_henshuu, QtCore.SIGNAL("clicked()"), self.onClickedHenshuu)
        QtCore.QObject.connect(self.ui.pushButton_sakujo, QtCore.SIGNAL("clicked()"), self.onClickedSakujo)
        control.SetColumnWidth(cont)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.ui.tableWidget.cellDoubleClicked.connect(self.cell_was_clicked)
        self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)   # ダブルクリックでの編集不可
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  # 一行ごとの選択モード
        self.ui.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection) # 一行のみ選択モード（複数行選択不可）
        self.ui.tableWidget.setCurrentCell(0, 0)

        self.shinki = Shinki()
        self.henshuu = Henshuu()
        self.sakujo = Sakujo()

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
        control.SetEnabled_False(cont)
    
    def onClickedHenshuu(self):
        rows = self.ui.tableWidget.currentRow()
        global ID
        item = self.ui.tableWidget.item(rows, 0)
        self.error = Error()

        try:
            ID = item.text()

        except:
            self.error.show()
            self.ui.tableWidget.clearContents()
            control.updateUi(cont, host, port)

        else:
            # connect to the database
            constr = "dbname=testdb host={} port={} user=postgres".format(host, port)
            conn = psycopg2.connect(constr)
            
            # create a cursor
            #cur = conn.cursor()
            userName = getpass.getuser()
            cur = conn.cursor(name=userName)
            
            # extract all the data
            tablename = "address"
            sql = 'select * from {} where "ID" = {};'.format(tablename, ID)
            cur.execute(sql)
            
            # show the cursor
            row = cur.fetchone()
            try:
                if row[3] == "取引先":
                    self.種別 = 0
                elif row[3] == "家族":
                    self.種別 = 1
                else:
                    self.種別 = 2

            except:
                self.error.show()
                self.ui.tableWidget.clearContents()
                control.updateUi(cont, host, port)

            else:
                ID = row[0]
                self.henshuu.ui.lineEdit_name.setText(row[1])
                self.henshuu.ui.lineEdit_furigana.setText(row[2])
                self.henshuu.ui.comboBox.setCurrentIndex(self.種別)
                self.henshuu.ui.lineEdit_company.setText(row[4])
                self.henshuu.ui.lineEdit_address.setText(row[5])
                self.henshuu.ui.lineEdit_phone.setText(row[6])
                self.henshuu.ui.lineEdit_mobile.setText(row[7])
                self.henshuu.ui.lineEdit_Fax.setText(row[8])
                self.henshuu.ui.lineEdit_Email.setText(row[9])
                self.henshuu.show()
                control.SetEnabled_False(cont)
                cur.close()
                conn.close()

    def onClickedSakujo(self):
        self.sakujo.show()
        control.SetEnabled_False(cont)

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.ui.tableWidget.item(row, column)
        global text
        text = item.text()
        print(text)
        clipboard.copy_to_clipboard(text)


class Shinki(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        global cont1
        cont1 = self.ui = shinki_ui.Ui_Dialog()
        self.ui.setupUi(self)
        control.dataClear(cont1)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)

    """
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_F1:
            self.onClickedOK()
        elif key == QtCore.Qt.Key_F2:
            self.onClickedCancel()
    """

    def onClickedOK(self):
        control.Shinki(cont1)
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)
        control.SetEnabled_True(cont)
        control.dataClear(cont1)

    def onClickedCancel(self):
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)
        control.SetEnabled_True(cont)
        control.dataClear(cont1)


class Henshuu(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        global cont2
        cont2 = self.ui = henshuu_ui.Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)
        global cont2_2
        cont2_2 = self.error2 = Error2()

    """
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_F1:
            self.onClickedOK()
        elif key == QtCore.Qt.Key_F2:
            self.onClickedCancel()
    """

    def onClickedOK(self):
        control.SetEnabled_True(cont)
        control.Henshuu(cont2, cont2_2, ID, host, port)
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)

    def onClickedCancel(self):
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)
        control.SetEnabled_True(cont)


class Sakujo(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = sakujo_ui.Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.onClickedOK)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.onClickedCancel)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)

    def onClickedOK(self):
        rows = cont.tableWidget.currentRow()
        item = cont.tableWidget.item(rows, 0)
        self.error = Error()
        self.error2 = Error2()

        try:
            ID = item.text()

        except:
            self.error.show()
            control.SetEnabled_False(cont)

        else:
            control.SetEnabled_True(cont)
            
            # connect to the database
            constr = "dbname=testdb host={} port={} user=postgres".format(host, port)
            conn = psycopg2.connect(constr)
            
            # create a cursor
            cur = conn.cursor()
            userName = getpass.getuser()
            #cur = conn.cursor(name=userName)
            
            # extract all the data
            tablename = "address"
            
            # delete the data
            
            try:
                sql = 'delete from {} where "ID" = {}'.format(tablename, ID)
            
            except UnboundLocalError:
                self.error.show()
                control.SetEnabled_False(cont)
            
            else:
                try:
                    cur.execute(sql)
                except psycopg2.ProgrammingError:
                    self.error2.show()
                    control.SetEnabled_False(cont)
            
            # close the cursor and connection
            finally:
                conn.commit()
                #cur.close()
                conn.close()
                cont.tableWidget.clearContents()
                control.updateUi(cont, host, port)

    def onClickedCancel(self):
        control.SetEnabled_True(cont)
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)


class Error(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = error_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.onClickedCancel)

        #errorMessage = "※データーが存在しないか、選択されていません。"

        #self.ui.label.setText(errorMessage)

    def onClickedCancel(self):
        control.SetEnabled_True(cont)
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)


class Error2(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = error_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.onClickedCancel)

        errorMessage = """他のユーザーが編集中です。
        しばらくしてから、やり直して下さい。"""

        self.ui.label.setText(errorMessage)

    def onClickedCancel(self):
        control.SetEnabled_True(cont)
        cont.tableWidget.clearContents()
        control.updateUi(cont, host, port)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
