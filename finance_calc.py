from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit
win_width, win_height = 800, 250
win_x, win_y = 200, 200
txt_title = "Финансовый калькулятор"
txt_send = "Отправить"

txt_line1 = "Ставка в процентах"
txt_line2 = "Период (мес.)"
txt_line3 = 'Сумма вклада'
txt_line4 = "На какое время (мес.)"
class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        
        super().__init__(parent=parent, flags=flags)
        
        self.initUI()
        
        self.connects()
        
        self.show()
        self.set_appear()
    def initUI(self):
        
        self.btn_send = QPushButton(txt_send, self)
        
        self.lable_finish = QLabel()
        self.layout_line = QHBoxLayout()

        self.line1 = QLineEdit(txt_line1)
        self.layout_line.addWidget(self.line1, alignment = Qt.AlignLeft)
        
        self.line2 = QLineEdit(txt_line2)
        self.layout_line.addWidget(self.line2, alignment = Qt.AlignLeft)
        
        self.line3 = QLineEdit(txt_line3)
        self.layout_line.addWidget(self.line3, alignment = Qt.AlignLeft)
        
        self.line4 = QLineEdit(txt_line4)
        self.layout_line.addWidget(self.line4, alignment = Qt.AlignLeft)
        
        
        self.layout_line.addWidget(self.btn_send, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lable_finish, alignment =
        Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        s1 = float(self.line1.text())
        s2 = float(self.line2.text())
        s3 = float(self.line3.text())
        s4 = float(self.line4.text())
        self.lable_finish.setText(str((s3*(1+s1/100)**(s4//s2))))
    def connects(self):
        self.btn_send.clicked.connect(self.next_click)
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def scet():
        pass

def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
    
main()


