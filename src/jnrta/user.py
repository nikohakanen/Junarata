'''
Created on Mar 17, 2016

@author: hakanen1
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from jnrta.kappale import *
from jnrta.centralwidget import *

class User(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        super(User, self).__init__()
        
        self.kappalelista = []
        self.initUI()
        
    def initUI(self):      

        mb = self.menuBar()
        fileMenu = mb.addMenu('Tiedosto')
        kappaleMenu = mb.addMenu('Kappale')
        
        tb = QToolBar()
        self.addToolBar(tb)

        self.cw = CentralWidget(self, self.kappalelista)
        
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Pienoisrautatie')
        
        
        self.setCentralWidget(self.cw.view)
        self.show()
        
        newAction = QAction("Uusi", self)
        self.connect(newAction, SIGNAL("triggered()"), self.uusiRata)
        fileMenu.addAction(newAction)
        
        openAction = QAction("Avaa", self)
        self.connect(openAction, SIGNAL("triggered()"), self.avaaRata)
        fileMenu.addAction(openAction)
        
        saveAction = QAction("Tallenna", self)
        self.connect(saveAction, SIGNAL("triggered()"), self.tallennaRata)
        fileMenu.addAction(saveAction)
        
        closeAction = QAction("Sulje", self)
        self.connect(closeAction, SIGNAL("triggered()"), self.sulje)
        fileMenu.addAction(closeAction)
        
        action0 = QAction("Stopperi",self)
        self.connect(action0, SIGNAL("triggered()"), self.setValitseKpl0)
        tb.addAction(action0)
        
        action1 = QAction("suora1",self)
        self.connect(action1, SIGNAL("triggered()"), self.setValitseKpl1)
        tb.addAction(action1)
        
        action2 = QAction("suora2",self)
        self.connect(action2, SIGNAL("triggered()"), self.setValitseKpl2)
        tb.addAction(action2)
        
        action3 = QAction("suora3",self)
        self.connect(action3, SIGNAL("triggered()"), self.setValitseKpl3)
        tb.addAction(action3)
        
        action4 = QAction("kaarre45",self)
        self.connect(action4, SIGNAL("triggered()"), self.setValitseKpl4)
        tb.addAction(action4)
        
        action5 = QAction("Kaarre30",self)
        self.connect(action5, SIGNAL("triggered()"), self.setValitseKpl5)
        tb.addAction(action5)
        
        action6 = QAction("Kaarre45mini",self)
        self.connect(action6, SIGNAL("triggered()"), self.setValitseKpl6)
        tb.addAction(action6)
        
        action7 = QAction("Kaarre30mini",self)
        self.connect(action7, SIGNAL("triggered()"), self.setValitseKpl7)
        tb.addAction(action7)
        
    def uusiRata(self):
        del self.kappalelista[:]
        self.cw.scene.clear()
        
    def tallennaRata(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save File','jnrta','*.txt')
        if fileName:
            if fileName.endswith('.txt'):
                fileName = fileName
            else:
                fileName = fileName + '.txt'
            with open(fileName, mode='w') as f:
                for kpl in self.kappalelista:
                    f.write('{}\n{}\n{}\n{}\n'.format(kpl.tyyppi, kpl.item.pos().x(), kpl.item.pos().y(), kpl.kierto))
    
    def avaaRata(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File','jnrta','*.txt')
        if fileName:
            f = open(fileName)
            line = f.readline().rstrip('\n')
            while line != '':
                tyyppi = int(line)
                x = float(f.readline().rstrip('\n'))
                y = float(f.readline().rstrip('\n'))
                kierto = float(f.readline().rstrip('\n'))
                line = f.readline().rstrip('\n')
                ### IF ERROR RAISE ERROR EXCEPTION ####
                self.valitseKpl(tyyppi, x, y, kierto, 0)
            self.cw.view.rakenna()
        
    def sulje(self):
        self.close()
    
    def setValitseKpl0(self):
        self.valitseKpl(0, -1000, -1000, 0, 1)
    def setValitseKpl1(self):
        self.valitseKpl(1, -1000, -1000, 0, 1)
    def setValitseKpl2(self):
        self.valitseKpl(2, -1000, -1000, 0, 1)
    def setValitseKpl3(self):
        self.valitseKpl(3, -1000, -1000, 0, 1)
    def setValitseKpl4(self):
        self.valitseKpl(4, -1000, -1000, 0, 1)
    def setValitseKpl5(self):
        self.valitseKpl(5, -1000, -1000, 0, 1)
    def setValitseKpl6(self):
        self.valitseKpl(6, -1000, -1000, 0, 1)
    def setValitseKpl7(self):
        self.valitseKpl(7, -1000, -1000, 0, 1)
        
    def valitseKpl(self, nro, x, y, kierto, selected):
        if nro == 0:
            stopperi = Stopperi([x,y])
            self.lisaaKpl(stopperi, kierto,selected)
        if nro == 1:
            suora1 = Suora1([x,y])
            self.lisaaKpl(suora1, kierto, selected)
        if nro == 2:
            suora2 = Suora2([x,y])
            self.lisaaKpl(suora2, kierto, selected)
        if nro == 3:
            suora3 = Suora3([x,y])
            self.lisaaKpl(suora3, kierto, selected)
        if nro == 4:
            k45 = Kaarre45([x,y])
            self.lisaaKpl(k45, kierto, selected)
        if nro == 5:
            k30 = Kaarre30([x,y])
            self.lisaaKpl(k30, kierto, selected)
        if nro == 6:
            k45m = Kaarre45mini([x,y])
            self.lisaaKpl(k45m, kierto, selected)
        if nro == 7:
            k30m = Kaarre30mini([x,y])
            self.lisaaKpl(k30m, kierto, selected)
        
    def lisaaKpl(self, ratakappale, kierto, selected):
        self.kappalelista.append(ratakappale)
        ratakappale.item.setParentItem(ratakappale)
        self.cw.scene.addItem(ratakappale)
        if selected == 1:
            ratakappale.item.setSelected(True)
        if selected == 0:
            ratakappale.pyorita(kierto)
        
    def rotate(self, ratakappale, ang):
        ratakappale.pyorita(ang)
        #ratakappale.item.setTransformOriginPoint(QPointF(ratakappale.keskikohta[0],ratakappale.keskikohta[1]))
        #ratakappale.item.setRotation(ang)
        #ratakappale.item.setTransformOriginPoint(QPointF(0,0))

def main():
    
        app = QApplication(sys.argv)
        usr = User()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()