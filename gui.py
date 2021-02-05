# -*- coding: utf-8 -*- 
'''
Created on 5 фев. 2021 г.

@author: smirnov_aa
'''
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QSplitter,\
    QLineEdit, QPushButton


class MainWindow(QWidget):
    '''
    classdocs
    '''

    def __init__(self):
        super(MainWindow, self).__init__()
        #self.setMinimumSize(240,320)
        #self.setMaximumSize(240,320)
        self._width=240
        self._height=320
        self.resize(self._width, self._height)
        self.setWindowTitle('0-бед or 0-bet')
        self.VBox=QVBoxLayout(self)
        self.VBox.setContentsMargins(5, 5, 5, 33)
        self.VBox.addStretch(1)
        self.restText=QLabel(self)
        self.restText.setText("Список заведений: ")
        self.restTable=QTableWidget(self)
        self.sep1=QSplitter(self)
        self.restUnit=QLineEdit(self)
        self.restAddButt=QPushButton(self)
        self.restAddButt.setText('Добавить заведение')
        self.sep2=QSplitter(self)
        self.restLottoreyButt=QPushButton(self)
        self.restLottoreyButt.setText('Лотерея')
        
        self.VBox.addWidget(self.restText)
        self.VBox.addWidget(self.restTable)
        self.VBox.addWidget(self.sep1)
        self.VBox.addWidget(self.restUnit)
        self.VBox.addWidget(self.restAddButt)
        self.VBox.addWidget(self.sep2)
        self.VBox.addWidget(self.restLottoreyButt)
        self.setLayout(self.VBox)   