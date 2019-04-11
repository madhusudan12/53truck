#This program gets two values from a DB into lineEdits.
import sys
from body import *
from PyQt5 import QtWidgets, QtGui, QtCore

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'tpptfr1'); 
import sqlite3
con = sqlite3.connect('tpptfr1')

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
      noofdoors = str(self.ui.lineEdit_4.text())
      bodystyle = str(self.ui.lineEdit_5.text())
      make = str(self.ui.lineEdit_6.text())
      englocn = str(self.ui.lineEdit.text())	
      cur.execute('INSERT INTO body VALUES(?,?,?,?,?)',([cid,noofdoors,bodystyle,make,englocn]))
      con.commit()
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
