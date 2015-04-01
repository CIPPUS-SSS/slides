# coding=utf-8
"""
4月第一次例会中用可能用到的代码
张德通的预习
"""


## !/usr/bin/python3
## -*- coding:utf-8 -*-

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == "__main__":
# app = QApplication(sys.argv)
#
# w = QWidget()
# w.resize(250, 100)
# w.move(300, 300)
#
#
# w.setWindowTitle("simple")
# w.show()
# sys.exit(app.exec_())



# 设置icon，没有实现
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
#
#
#
#
# class Example(QWidget):
#
# def __init__(self):
# super().__init__()
#
# self.initUI()
#
# def initUI(self):
#
#         self.setGeometry(300, 300, 300 ,220)
#         self.setWindowTitle("Icon")
#         self.setWindowIcon(QIcon('pic.jpg'))
#
#         self.show()
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
# class Example(QWidget):
#
#     def __init__(myself):
#         super().__init__()
#         myself.initUI()
#
#     def initUI(myself):
#
#         QToolTip.setFont(QFont('SansSerif',10))
#         myself.setToolTip('this is a <b>QWidget</b> widget')
#
#         btn = QPushButton("Button", myself)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50,50)
#
#         myself.setGeometry(300,300,300,200)
#         myself.setWindowTitle("Tooltips")
#         myself.show()
#
# if __name__=="__main__":
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#


# #！/usr/bin/python3
# # -*- coding: utf-8 -*-
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("message box")
#         self.show()
#
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self,
#                                      "message",
#                                      "are you sure to quit?",
#                                      QMessageBox.Yes | QMessageBox.No,
#                                      QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# #！/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
# class Example(QWidget):
#
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.resize(250,150)
#         self.my_center()
#         self.setWindowTitle("center")
#         self.show()
#
#     def my_center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


"""
Main Window
Statusbar
"""

# #！/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         self.statusBar().showMessage("ready")
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("statusbar")
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

"""
    super()函数 参考：http://www.cnblogs.com/dkblog/archive/2011/02/24/1980654.html
    例1
"""

# class FooParent():
#     def bar(self, message):
#         print(message)
#
# class FooChild(FooParent):
#     def haha(self, message):
#         super().bar(message)
#
# if __name__ == '__main__':
#     FooChild().haha("hello world\n")
#

"""例2"""
#
# class A:
#     def __init__(self):
#         print("enter A")
#         print("leave A")
#
# class B(A):
#     def __init__(self):
#         print("enter B")
#         A.__init__(self)
#         print("leave B")
#
# class C(A):
#     def __init__(self):
#         print("enter C")
#         A.__init__(self)
#         print("leave C")
#
# class D(A):
#     def __init__(self):
#         print("enter D")
#         A.__init__(self)
#         print("leave D")
#
# class E(B, C, D):
#     def __init__(self):
#         print("enter E")
#         B.__init__(self)
#         C.__init__(self)
#         D.__init__(self)
#         print("enter E")
#
# if __name__ == "__main__":
#     E()


"""例3"""

# class A:
#     def __init__(self):
#         print("enter a")
#         print("leave a")

# class B(A):
#     def __init__(self):
#         print("enter B")
#         super().__init__()
#         print("leave b")
#
# class C(A):
#     def __init__(self):
#         print("enter c")
#         super().__init__()
#         print("leave c")
#
# class D(A):
#     def __init__(self):
#         print("enter d")
#         super().__init__()
#         print("leave d")
#
# class E(B, C, D):
#     def __init__(self):
#         print("enter e")
#         super().__init__()
#         print("leave e")
#
# if __name__ == "__main__":
#     E()
'''研究去吧！着玩意就够说上半小时的了！！http://blog.csdn.net/johnsonguo/article/details/585193'''

'''argc'''
# import sys
# if __name__=="__main__":
#     print(sys.argv)



##！/usr/bin/python3
##-*- coding: gbk -*-

# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         exitAction = QAction('&Exit', self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu("&File")
#         fileMenu.addAction("haha")
#         fileMenu.addAction("&haha")
#
#         fileMenu = menubar.addMenu("hello")
#         fileMenu.addAction(exitAction)
#         fileMenu.addAction(QIcon('pic.png'), "haha")
#
#         self.setGeometry(300, 300, 300, 250)
#         self.setWindowTitle("Menubar")
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


#
# #!/usr/bin/python3
# #-*- coding:utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# from PyQt5.QtGui import QIcon
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         exitAction = QAction(QIcon('pic.png'), 'Exit', self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.triggered.connect(qApp.quit)
#
#         self.toolbar = self.addToolBar('a')
#         self.toolbar.addAction(exitAction)
#
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('工具栏')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


#
# #上面那两个加起来的效果。
# import sys
# from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
# from PyQt5.QtGui import QIcon
#
#
# class example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         textEdit = QTextEdit()
#         self.setCentralWidget(textEdit)
#
#         exitAction = QAction(QIcon('pic.png'), 'Exit', self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.close)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#
#         toolbar = self.addToolBar('Exit')
#         toolbar.addAction(exitAction)
#
#         self.setGeometry(300, 300, 300, 250)
#         self.setWindowTitle('main window')
#         self.show()

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())




'''
Layout management in PyQt5
Absolute positioning
'''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication
#
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         lbl1 = QLabel("zetcode", self)
#         lbl1.move(15,10)
######
#         lbl2 = QLabel("tutorials", self)
#         lbl2.move(35,40)
#
#         lbl3 = QLabel("for programmers", self)
#         lbl3.move(55,70)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Absloute')
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''
Box layout
'''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         okButton = QPushButton("ok")
#         cancelButton = QPushButton("cancel")
#         hello = QPushButton("hello")
#
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         hbox.addWidget(hello)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('button')
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''QGridLayout'''
#
# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         names = ['Cls', 'bck', '', 'close',
#                  '7', '8', '9', '/',
#                  '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                  '0', '.', '=', '+']
#
#         positions = [(i,j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#             if name == '':
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#
#         self.move(300, 150)
#         self.setWindowTitle('calculate')
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())

#
#
#
# '''
# Review example
# '''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         title = QLabel('title')
#         author = QLabel("author")
#         review = QLabel('review')
#
#         titleEdit = QLineEdit()
#         authorEdit = QLineEdit()
#         reviewEdit = QLineEdit()
#
#         grid = QGridLayout()
#         grid.setSpacing(10)
#
#         grid.addWidget(title, 1, 0)
#         grid.addWidget(titleEdit, 1, 1)
#
#         grid.addWidget(author, 2, 0)
#         grid.addWidget(authorEdit, 2, 1)
#
#         grid.addWidget(review, 3, 0)
#         grid.addWidget(reviewEdit, 3, 1, 10, 1)
#
#         self.setLayout(grid)
#         self.setGeometry(0, 0, 400, 300)
#         self.setWindowTitle('Review')
#         self.show()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''signals and slots'''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication
#
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
#
#         #self可有可无，QSlider::QSlider(Qt::Orientation orientation, QWidget * parent = 0)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('signals & slots')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''Reimplementing event handler'''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication
#
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('event handler')
#         self.show()
#
#     #重新实现keyPressEvent.
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''Event Sender'''
# #！/usr/bin/python3
# #-*- coding:utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         btn1 = QPushButton("button 1", self)
#         btn1.move(30, 50)
#
#         btn2 = QPushButton('button 2', self)
#         btn2.move(150, 50)
#
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('event sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + 'was pressed')
#
#
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


'''Emitting signals'''
#!/usr/bin/python3
#-*- coding:utf-8 -*-
#
# import sys
# from PyQt5.QtCore import pyqtSignal, QObject
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
# class example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('emit signal')
#         self.show()
#
#     def mousePressEvent(self,QMouseEvent):
#         # self.c.closeApp.emit()
#         self.statusBar().showMessage("haha")
#
# class Communicate(QObject):
#     closeApp = pyqtSignal()
#
# if __name__ =="__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())
#

#
# import sys
# from PyQt5.QtWidgets import *
#
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.le = QLineEdit(self)
#         self.btn = QPushButton('dialog', self)
#         self.initUi()
#
#     def initUi(self):
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le.move(130, 22)
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Input dialog')
#         self.show()
#
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'input Dialog', 'enter your name:  ')
#         if ok:
#             self.le.setText(str(text))
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''QColorDialog'''
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.frm = QFrame(self)
#         self.btn = QPushButton('dialog', self)
#         self.initUi()
#
#     def initUi(self):
#         col = QColor(250, 250, 250)
#         self.btn.move(20, 20)
#
#         self.btn.clicked.connect(self.showDialog)
#         self.frm.setStyleSheet('QWidget { background-color:%s }' % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)
#
#         self.setGeometry(300, 300, 250, 180)
#
#         self.setWindowTitle("color dialog")
#         self.show()
#
#     def showDialog(self):
#         col = QColorDialog.getColor()
#
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''QFontDialog'''
#
# import sys
# from PyQt5.QtWidgets import *
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         vbox = QVBoxLayout()
#
#         btn = QPushButton('dialog', self)
#         btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         btn.move(20, 20)
#
#         vbox.addWidget(btn)
#         btn.clicked.connect(self.showDialog)
#         self.blb = QLabel("knowledge only matters", self)
#         self.blb.move(130, 20)
#
#         vbox.addWidget(self.blb)
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('font dialog')
#         self.show()
#
#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.blb.setFont(font)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''QFileDialog'''
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
# class example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#
#         self.textEdit = QTextEdit()
#         self.setCentralWidget(self.textEdit)
#         self.statusBar()
#
#         openFile = QAction(QIcon('pic.png'), 'open', self)
#         openFile.setShortcut('Ctrl + Q')
#         openFile.setStatusTip('open new file')
#         openFile.triggered.connect(self.showDialog)
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu("&File")
#         fileMenu.addAction(openFile)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('file dialog')
#         self.show()
#
#     def showDialog(self):
#         fname = QFileDialog.getOpenFileName(self, 'openfile', '/home')
#
#         f = open(fname, 'r')
#
#         '''with!'''
#         with f:
#             data = f.read()
#             self.textEdit.setText(data)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''decorator'''
'''01'''
# def myfunc():
#     print('myfunc() called')
#
#
# myfunc()
# myfunc()

'''02'''
#
#
# def deco(func):
#     print("before myfunc() called")
#     func()
#     print("after myfunc() called")
#     return func
#
#
# @deco
# def myfunc():
#     print("myfunc() called")
#
# # myfunc = deco(myfunc)
#
# myfunc()
# myfunc()


'''QCheckBox'''
#
# #!/usr/bin/python3
# #-*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
# from PyQt5.QtCore import Qt
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initui()
#
#     def initui(self):
#         cb = QCheckBox('show title', self)
#         cb.move(20, 20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QCheckBox')
#         self.show()
#
#     def changeTitle(self, state):
#         if state == Qt.Checked:
#             self.setWindowTitle('Qcheckboxx')
#         else:
#             self.setWindowTitle(' ')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''Toggle button'''
#
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
# from PyQt5.QtGui import QColor
#
# class example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initui()
#
#     def initui(self):
#         self.col = QColor(255, 255, 255)
#
#         redb = QPushButton('red', self)
#         redb.setCheckable(True)
#         redb.move(10, 10)
#
#         redb.clicked[bool].connect(self.setColor)
#
#         gedb = QPushButton('green', self)
#         gedb.setCheckable(True)
#         gedb.move(10, 60)
#
#         blueb = QPushButton('blue', self)
#         blueb.setCheckable(True)
#         blueb.move(10, 110)
#
#         blueb.clicked[bool].connect(self.setColor)
#
#         self.square = QFrame(self)
#         self.square.setGeometry(150, 20, 100, 100)
#         self.square.setStyleSheet('QWidget {background-color: %s }' % self.col.name)
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('toggle button')
#         self.show()
#
#     def setColor(self, pressed):
#
#         source = self.sender()
#
#         if pressed:
#             val = 0
#         else:
#             val = 255
#
#         if source.text() == 'red':
#             self.col.setRed(val)
#         elif source.text() == 'green':
#             self.col.setGreen(val)
#         else:
#             self.col.setBlue(val)
#
#         self.square.setStyleSheet('QFrame {background-color: %s} '% self.col.name())
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = example()
#     sys.exit(app.exec_())


'''QSlider'''
#
# import sys
# from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
#
# class example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#
#     def initUi(self):
#         sld = QSlilder(Qt.Horizontal, self)