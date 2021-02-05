# -*- coding: utf-8 -*- 
'''
Created on 5 фев. 2021 г.

@author: smirnov_aa
'''
from PySide6.QtWidgets import QMainWindow, QSizePolicy

class MainWindow(QMainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(240,320)
        self.setMaximumSize(240,320)
        self._width=240
        self._height=320
        #self.resize(self._width, self._height)
        self.setWindowTitle('0-бед')