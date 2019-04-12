import sys
import os
from tpptfr import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.body)
     self.ui.pushButton_2.clicked.connect(self.params)
     self.ui.pushButton_3.clicked.connect(self.shape)
     self.ui.pushButton_4.clicked.connect(self.predict)
     self.ui.pushButton_5.clicked.connect(self.engine)

  def body(self):
    os.system("python body1.py")

  def engine(self):
    os.system("python engine1.py")

  def params(self):
    os.system("python oparams1.py")

  def shape(self):
    os.system("python shape1.py")

  def predict(self):
    os.system("python samp6.py")

#  def gnrep(self):
#	os.system("python genrep1.py")
       
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
