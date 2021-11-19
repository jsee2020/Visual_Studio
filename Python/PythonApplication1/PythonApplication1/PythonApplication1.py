import pymysql 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType("Test.ui")[0]

class MyWindow(QDialog, form_class):
   def __init__(self):
       super().__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.btn_clicked)
       self.pushButton_2.clicked.connect(self.btn2_clicked)

   def btn_clicked(self):
       self.textEdit.setText("Hello World!")

   def btn2_clicked(self):
       conn = pymysql.connect(host='jsee.ipdisk.co.kr', user='root', password='whdtnsql!', db='test', charset='utf8') 
       cursor = conn.cursor() 
       sql = "SELECT * FROM qry_test" 
       cursor.execute(sql) 
       res = cursor.fetchall() 
       conn.commit() 
       conn.close()
       #return res
       #setTables(res)

       self.textEdit_2.setText(res)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   app.exec_()