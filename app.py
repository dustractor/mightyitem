from argparse import ArgumentParser
from itertools import combinations
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout,
    QCheckBox, QLabel, QLineEdit,QListWidget,
    QPushButton)

args = ArgumentParser()
args.add_argument("--foo",action="store_true")
ns,argv = args.parse_known_args()
globals().update(ns.__dict__)
print("foo:",foo)

class AppWin(QMainWindow):
    def chk_state_changed(self,state):
        print("self,state:",self,state)
    def txt_return_pressed(self):
        print(self.txt.text())
    def txt_text_edited(self,text):
        print("self,text:",self,text)
    def lsx_current_item_changed(self,item):
        print("self,item,item.text():",self,item,item.text())
    def btn_clicked(self):
        print("self:",self)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World!")
        self.box = QVBoxLayout()
        self.lbl = QLabel()
        self.chk = QCheckBox()
        self.txt = QLineEdit()
        self.lsx = QListWidget()
        self.btn = QPushButton()
        self.box.addWidget(self.lbl)
        self.box.addWidget(self.chk)
        self.box.addWidget(self.txt)
        self.box.addWidget(self.lsx)
        self.box.addWidget(self.btn)
        self.ldr = QWidget()
        self.ldr.setLayout(self.box)
        self.setCentralWidget(self.ldr)
        self.chk.stateChanged.connect(self.chk_state_changed)
        self.txt.returnPressed.connect(self.txt_return_pressed)
        self.txt.textEdited.connect(self.txt_text_edited)
        ls = ["".join(t) for t in combinations("abcdefg",2)]
        self.lsx.addItems(ls)
        self.lsx.currentItemChanged.connect(self.lsx_current_item_changed)
        self.btn.clicked.connect(self.btn_clicked)
combinations

app = QApplication(argv)
win = AppWin()
win.show()
app.exec()



