'''
Created on Mar 17, 2016

@author: hakanen1
'''
import sys
from PyQt4.QtGui import *
from pkt.alusta import *
from pkt.kappale import *

class User(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        super(User, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        mb = self.menuBar()
        mb.addMenu('Tiedosto')
        mb.addMenu('Kappale')
        
        tb = QToolBar()
        self.addToolBar(tb)
        
        wg = Alusta() #set Alusta as wg
        self.setCentralWidget(wg)
        
        kpl1 = Ratakappale()
        kpl2 = Ratakappale()
        wg.lisaaKpl(kpl1)
        wg.lisaaKpl(kpl2)
        
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('Pienoisrautatie')
        self.show()

def main():
    
        app = QApplication(sys.argv)
        usr = User()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()