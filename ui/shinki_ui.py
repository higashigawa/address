# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nas-263\OneDrive\works\address\ui\shinki_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(440, 203)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 9, 401, 158))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_company = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_company.setFont(font)
        self.lineEdit_company.setCursorPosition(0)
        self.lineEdit_company.setObjectName(_fromUtf8("lineEdit_company"))
        self.gridLayout.addWidget(self.lineEdit_company, 1, 5, 1, 1)
        self.lineEdit_address = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setObjectName(_fromUtf8("lineEdit_address"))
        self.gridLayout.addWidget(self.lineEdit_address, 2, 2, 1, 4)
        self.lineEdit_Email = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet(_fromUtf8(""))
        self.lineEdit_Email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_Email.setObjectName(_fromUtf8("lineEdit_Email"))
        self.gridLayout.addWidget(self.lineEdit_Email, 4, 5, 1, 1)
        self.lineEdit_mobile = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_mobile.setFont(font)
        self.lineEdit_mobile.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_mobile.setObjectName(_fromUtf8("lineEdit_mobile"))
        self.gridLayout.addWidget(self.lineEdit_mobile, 3, 5, 1, 1)
        self.lineEdit_phone = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setAutoFillBackground(False)
        self.lineEdit_phone.setStyleSheet(_fromUtf8(""))
        self.lineEdit_phone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_phone.setCursorPosition(0)
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.gridLayout.addWidget(self.lineEdit_phone, 3, 2, 1, 1)
        self.lineEdit_Fax = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_Fax.setFont(font)
        self.lineEdit_Fax.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Fax.setObjectName(_fromUtf8("lineEdit_Fax"))
        self.gridLayout.addWidget(self.lineEdit_Fax, 4, 2, 1, 1)
        self.label_furigana = QtGui.QLabel(self.gridLayoutWidget)
        self.label_furigana.setObjectName(_fromUtf8("label_furigana"))
        self.gridLayout.addWidget(self.label_furigana, 0, 3, 1, 1)
        self.label_address = QtGui.QLabel(self.gridLayoutWidget)
        self.label_address.setObjectName(_fromUtf8("label_address"))
        self.gridLayout.addWidget(self.label_address, 2, 0, 1, 1)
        self.label_Fax = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Fax.setObjectName(_fromUtf8("label_Fax"))
        self.gridLayout.addWidget(self.label_Fax, 4, 0, 1, 1)
        self.label_mobile = QtGui.QLabel(self.gridLayoutWidget)
        self.label_mobile.setObjectName(_fromUtf8("label_mobile"))
        self.gridLayout.addWidget(self.label_mobile, 3, 3, 1, 1)
        self.label_company = QtGui.QLabel(self.gridLayoutWidget)
        self.label_company.setObjectName(_fromUtf8("label_company"))
        self.gridLayout.addWidget(self.label_company, 1, 3, 1, 1)
        self.label_phone = QtGui.QLabel(self.gridLayoutWidget)
        self.label_phone.setObjectName(_fromUtf8("label_phone"))
        self.gridLayout.addWidget(self.label_phone, 3, 0, 1, 1)
        self.label_shubetsu = QtGui.QLabel(self.gridLayoutWidget)
        self.label_shubetsu.setObjectName(_fromUtf8("label_shubetsu"))
        self.gridLayout.addWidget(self.label_shubetsu, 1, 0, 1, 1)
        self.Label_name = QtGui.QLabel(self.gridLayoutWidget)
        self.Label_name.setObjectName(_fromUtf8("Label_name"))
        self.gridLayout.addWidget(self.Label_name, 0, 0, 1, 1)
        self.label_Email = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Email.setObjectName(_fromUtf8("label_Email"))
        self.gridLayout.addWidget(self.label_Email, 4, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8(""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.lineEdit_furigana = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_furigana.setFont(font)
        self.lineEdit_furigana.setStyleSheet(_fromUtf8(""))
        self.lineEdit_furigana.setCursorPosition(0)
        self.lineEdit_furigana.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_furigana.setObjectName(_fromUtf8("lineEdit_furigana"))
        self.gridLayout.addWidget(self.lineEdit_furigana, 0, 5, 1, 1)
        self.lineEdit_name = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet(_fromUtf8(""))
        self.lineEdit_name.setCursorPosition(0)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 1)
        self.lineEdit_furigana.raise_()
        self.label_address.raise_()
        self.label_Fax.raise_()
        self.label_mobile.raise_()
        self.label_company.raise_()
        self.label_phone.raise_()
        self.label_shubetsu.raise_()
        self.lineEdit_name.raise_()
        self.Label_name.raise_()
        self.label_Email.raise_()
        self.label_furigana.raise_()
        self.lineEdit_Fax.raise_()
        self.lineEdit_phone.raise_()
        self.lineEdit_mobile.raise_()
        self.lineEdit_company.raise_()
        self.lineEdit_Email.raise_()
        self.lineEdit_address.raise_()
        self.comboBox.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_name, self.lineEdit_furigana)
        Dialog.setTabOrder(self.lineEdit_furigana, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.lineEdit_company)
        Dialog.setTabOrder(self.lineEdit_company, self.lineEdit_address)
        Dialog.setTabOrder(self.lineEdit_address, self.lineEdit_phone)
        Dialog.setTabOrder(self.lineEdit_phone, self.lineEdit_mobile)
        Dialog.setTabOrder(self.lineEdit_mobile, self.lineEdit_Fax)
        Dialog.setTabOrder(self.lineEdit_Fax, self.lineEdit_Email)
        Dialog.setTabOrder(self.lineEdit_Email, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "新規登録", None))
        self.label_furigana.setText(_translate("Dialog", "フリガナ:", None))
        self.label_address.setText(_translate("Dialog", "住所", None))
        self.label_Fax.setText(_translate("Dialog", "Fax:", None))
        self.label_mobile.setText(_translate("Dialog", "携帯:", None))
        self.label_company.setText(_translate("Dialog", "会社名:", None))
        self.label_phone.setText(_translate("Dialog", "電話番号:", None))
        self.label_shubetsu.setText(_translate("Dialog", "種別:", None))
        self.Label_name.setText(_translate("Dialog", "氏名:", None))
        self.label_Email.setText(_translate("Dialog", "Email:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "取引先", None))
        self.comboBox.setItemText(1, _translate("Dialog", "家族", None))
        self.comboBox.setItemText(2, _translate("Dialog", "友人", None))

