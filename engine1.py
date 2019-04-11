#This program gets two values from a DB into lineEdits.
import sys
from engine import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('tpptfr1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'cpptfr1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)


  def insertvalues(self):
    with con:
      cur = con.cursor()
      cid = str(self.ui.lineEdit_3.text())
      fueltype = str(self.ui.lineEdit_4.text())
      engntype = str(self.ui.lineEdit_5.text())
      cylndrs = str(self.ui.lineEdit_6.text())
      engnsize = str(self.ui.lineEdit.text())	
      cur.execute('INSERT INTO engine VALUES(?,?,?,?,?)',([cid,fueltype,engntype,cylndrs,engnsize]))
      con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
