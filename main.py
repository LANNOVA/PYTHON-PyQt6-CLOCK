import datetime
from datetime import date,time, datetime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

today = date.today()
print(today)
now = datetime.now()
current_time = time(now.hour, now.minute, now.second)
print(current_time)
x= str(current_time)
y= str(today)

app = QApplication([])

window = QWidget()
window.setWindowTitle("CLOCK")
window.setGeometry(100, 100, 280, 80)
time1 = QLabel(x, parent=window)
day = QLabel(y, parent=window)
day.move(49,30)
time1.move(60, 15)
window.show()
sys.exit(app.exec())
