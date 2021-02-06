# -*- coding: utf-8 -*- 
'''
Created on 5 фев. 2021 г.

@author: smirnov_aa
'''
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableView,\
    QLineEdit, QPushButton, QFrame, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QObject, QSize
from PySide6.QtCore import Signal, Slot

#объявление сигналов Qt
class Sig(QObject):
    lists=Signal(list, list)#cигнал для передачи списков в основное тело программы
    def __init__(self):
        super().__init__()      

class MainWindow(QWidget):
    '''
    Объявление UI для программы
    '''
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self._width=360
        self._height=320
        self.setMinimumSize(self._width,self._height)
        self.setMaximumSize(self._width,self._height)
        #self.resize(self._width, self._height)
        self.setWindowTitle('0-бед or 0-bet')
        self.VBox=QVBoxLayout(self)
        self.VBox.setContentsMargins(5, 5, 5, 5)
        self.restText=QLabel(self)
        self.restText.setText("Список заведений: ")
        self.restTable=QTableView(self)
        self.sep1 = QFrame(self)
        self.sep1.setFrameShape(QFrame.HLine)
        self.sep1.setFrameShadow(QFrame.Sunken)
        self.restUnitName=QLineEdit(self)
        self.restAddButt=QPushButton(self)
        self.restAddButt.setText('Добавить заведение')
        self.restRmvButt=QPushButton(self)
        self.restRmvButt.setText('Удалить заведение')
        self.sep2 = QFrame(self)
        self.sep2.setFrameShape(QFrame.HLine)
        self.sep2.setFrameShadow(QFrame.Sunken)
        self.restLotteryButt=QPushButton(self)
        self.restLotteryButt.setText('Лотерея')        
       
        self.VBox.addWidget(self.restText)
        self.VBox.addWidget(self.restTable)
        self.VBox.addWidget(self.sep1)
        self.VBox.addWidget(self.restUnitName)
        self.VBox.addWidget(self.restAddButt)
        self.VBox.addWidget(self.restRmvButt)
        self.VBox.addWidget(self.sep2)
        self.VBox.addWidget(self.restLotteryButt)
        self.setLayout(self.VBox)
        
        self.restAddButt.clicked.connect(self.addRestItem)
        self.restLotteryButt.clicked.connect(self.startLottery)
        self.restRmvButt.clicked.connect(self.removeRestItem)
        self.restTable.clicked.connect(self.selectRest)
        
        self.name_list=[]
        self.reqCount_list=[]
        self.sg=Sig()
        parent.sg.updateTable.connect(self.updTbl)      
        
        
    def addRestItem(self):
            name=self.restUnitName.text()
            if name in self.name_list:
                self.reqCount_list[self.name_list.index(name)]=self.reqCount_list[self.name_list.index(name)]+1
            else:
                self.name_list.append(name)
                self.reqCount_list.append(1)
            table_model=RestaurantTableModeL(self.name_list, self.reqCount_list)
            self.restTable.setModel(table_model)
            self.restTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.restTable.horizontalHeader().setStretchLastSection(True)
              
    def startLottery(self):
        self.sg.lists.emit(self.name_list, self.reqCount_list)
        
    def selectRest(self):
        self.idx=self.restTable.currentIndex()
        self.restTable.selectRow(self.idx.row())
    
    def removeRestItem(self):
        self.idx=self.restTable.currentIndex()
        if self.reqCount_list[self.idx.row()] > 1:
            self.reqCount_list[self.idx.row()]-=1
        else:
            self.name_list.pop(self.idx.row())
            self.reqCount_list.pop(self.idx.row())
        table_model=RestaurantTableModeL(self.name_list, self.reqCount_list)
        self.restTable.setModel(table_model)
        self.restTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.restTable.horizontalHeader().setStretchLastSection(True)
        
    
    @Slot(list)
    def updTbl(self, cnt):
        table_model=RestaurantTableModeL(self.name_list, self.reqCount_list, cnt)
        self.restTable.setModel(table_model)
        self.restTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.restTable.horizontalHeader().setStretchLastSection(True)
            
class RestaurantTableModeL(QAbstractTableModel):
    def __init__(self, name_list, reqCount_list, counter=None):
        super().__init__()
        self.name_list=name_list
        self.reqCount_list=reqCount_list
        self.counter=counter
    def rowCount(self, parent):
        return len(self.name_list)
    def columnCount(self, parent):
        return 3
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if col == 0:
                return "Название заведения"
            if col == 1:
                return "Количество заявок"
            if col == 2:
                return "Результат"
    def data(self, idx = QModelIndex(), role=None):
        c=idx.column()
        r=idx.row()
        if c == 0 and role == Qt.DisplayRole:
            return self.name_list[r]
        if c == 1 and role == Qt.DisplayRole:
            return self.reqCount_list[r]
        if c == 2 and self.counter != None and role == Qt.DisplayRole:
            return '+'*self.counter[r]