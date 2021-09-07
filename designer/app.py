from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog
from stylesheets import main_style_sheet
class Dialog(QDialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
       
    

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_stuff)
        self.done = []
        self.not_done = []
        self.pushButton_3.clicked.connect(self.do_task)
        self.pushButton_2.clicked.connect(self.undo_task)
        self.setStyleSheet(main_style_sheet)
    def add_task(self,task):
        if bool(task) != False:
            self.remaining_list.addItem(task)
    
    def do_task(self):
        task=self.remaining_list.takeItem(self.remaining_list.currentRow())
        if bool(task)!=False:
             self.finished_list.addItem(task.text())
    
    def undo_task(self):
        task=self.finished_list.takeItem(self.finished_list.currentRow())
        if bool(task)!=False:
             self.remaining_list.addItem(task.text())
    
    def add_stuff(self):
        dig= Dialog()
        dig.ui.buttonBox.accepted.connect(
            lambda: self.add_task(dig.ui.new_task_input.text())
        )
        dig.exec()
        


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
