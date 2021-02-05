import requests, sys
import gui
from PySide6.QtWidgets import QApplication
res=requests.get('https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new')
res_seq=res.content.decode('utf-8').split('\n')

res_seq=[int(i) for i in res_seq[:-1]]
print(res_seq)

app=QApplication(sys.argv)
window=gui.MainWindow()
window.show()
app.exec_()

