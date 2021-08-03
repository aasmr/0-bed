#import requests, sys
import urllib.request as reqq
import gui, sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot, Signal, QObject

#объявление сигналов Qt
class Signals(QObject):
    updateTable = Signal(list) #сигнал на обновление таблицы для записи результатов, также передающий список
    def __init__(self):
        super().__init__()    
#основное тело программы
class Body():
    def __init__(self):
        self.sg=Signals() #инициализируем сигналы
        self.app=QApplication(sys.argv) #создаем экземпляр приложения
        self.window=gui.MainWindow(self) #подгружаем итерфейс окна из gui.py
        self.window.sg.lists.connect(self.get_rest) #подключаем слот-функцию get_rest на появление сигнала sg.list из gui.py
        
    """
    объявляем слот-функцию, принимающю в качестве аргументов два списка:
    список названий заведений и список количества заявок на каждое заведение
    """
    @Slot(list, list)        
    def get_rest(self, name, req_count):
        counter_win=[0 for i in range(len(name))] #счетчик побед для каждого заведения
        max=sum(req_count) #подсчет суммы всех заявок
        cnt=1 #Вспомогательный счетчик 1
        cnt_=0 #Вспомогательный счетчик 2
        lot_dict={} #Вспомогательный словарь для сопоставления индексов заявок соответсвующему заявлению
        for i in req_count:
            if i ==1: #если колличество заявок на конкретное заведения равно 1
                lot_dict[cnt]=name[cnt_] #просто присваиваем индекс этой заявки этому заведению
                cnt+=1
            else: #иначе (если заявок на одно заведение больше одной)
                for l in range(cnt, cnt+i): #присвоим индексы каждой заявки
                    lot_dict[l]=name[cnt_]  #этому заведению
                cnt+=i
            cnt_+=1
        while (3 in counter_win) != True: #пока среди счетчиков побед нет хотя бы одной тройки
            rand=self.req(1, 1, max) #получаем одну рандомную цифру от 1 до max (сумма всех заявок)
            counter_win[name.index(lot_dict[rand])]+=1 #смотрим какое заведение соответствует рандомной цифре, смотрим индекс этого заведения в списке названий и по этому индксу увеличиваем счетчик побед
        self.sg.updateTable.emit(counter_win) #испускаем сигнал, передающий список счетчиков
    """
    объявлем функцию связи с космосом
    принимаемые параметры
    num - количество чисел, которые надо получить
    min - от...
    max - ...до...
    """
    """
    КОТ, ЭТОТ КОММЕНТ ДЛЯ ТЕБЯ
    def req(num, min, max):
        #делаем гет-запрос
        res=reqq.urlopen('https://www.random.org/integers/?num='+str(num)+'&min='+str(min)+'&max='+str(max)+'&col=1&base=10&format=plain&rnd=new')
        #дешефруем и создаем список
        res_seq=res.read().decode('utf-8').split('\n')
        #переводим из str в int
        res_seq=[int(i) for i in res_seq[:-1]]
        return res_seq
    ПРОСТО КОПИРУЙ. У МЕНЯ РАБОТАЕТ. К ТОМУ ЖЕ И ВЫДАЧА НЕСКОЛЬКИХ ЧИСЕЛ
    """
    
    def req(self, num, min, max):
        #делаем гет-запрос
        #res=requests.get('https://www.random.org/integers/?num='+str(num)+'&min='+str(min)+'&max='+str(max)+'&col=1&base=10&format=plain&rnd=new')
        res=reqq.urlopen('https://www.random.org/integers/?num='+str(num)+'&min='+str(min)+'&max='+str(max)+'&col=1&base=10&format=plain&rnd=new')
        #дешефруем и создаем список
        res_seq=res.read().decode('utf-8').split('\n')
        #переводим из str в int
        res_seq=[int(i) for i in res_seq[:-1]]
        return res_seq

if __name__=='__main__':
    app=Body() #запускаем прогу
    app.window.show() #показываем окошко
    app.app.exec_() #и ждем, пока закроем
