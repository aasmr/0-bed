import requests, sys
import gui
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot, Signal, QObject

@Slot(list, list)
class Signals(QObject):
    updateTable = Signal(list)
    def __init__(self):
        super().__init__()    

class Body():
    def __init__(self):
        self.sg=Signals()
        self.app=QApplication(sys.argv)
        self.window=gui.MainWindow(self)
        self.window.sg.lists.connect(self.get_rest)
        
            
    def get_rest(self, name, req_count):
        counter=[0 for i in range(len(name))]
        max=0
        cnt=1
        cnt_=0
        lot_dict={}
        
        for i in req_count:
            max=max+i
            if i ==1:
                lot_dict[cnt]=name[cnt_]
                cnt+=1
            else:
                for l in range(cnt, cnt+i):
                    lot_dict[l]=name[cnt_]
                cnt+=i
            cnt_+=1
        while (3 in counter) != True:
            rand=self.req(1, 1, max)
            counter[name.index(lot_dict[rand])]+=1
            print(counter)
            self.sg.updateTable.emit(counter)
    
    def req(self, num, min, max):
        res=requests.get('https://www.random.org/integers/?num='+str(num)+'&min='+str(min)+'&max='+str(max)+'&col=1&base=10&format=plain&rnd=new')
        res_seq=res.content.decode('utf-8').split('\n')
        res_seq=[int(i) for i in res_seq[:-1]][0]
        return res_seq

if __name__=='__main__':
    app=Body()
    app.window.show()
    app.app.exec_()
