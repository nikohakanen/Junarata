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
    Pääluokka joka rakentaa käyttöliittymän.
    '''


    def __init__(self):
        super(User, self).__init__()
        
        self.kappalelista = []
        self.initUI()
        
    def initUI(self):      

        mb = self.menuBar()
        fileMenu = mb.addMenu('Tiedosto')
        
        tb = QToolBar()
        self.addToolBar(0x1,tb)

        self.cw = CentralWidget(self, self.kappalelista)
        
        self.setGeometry(0, 0, 1200, 800)
        self.setWindowTitle('Pienoisrautatie')
        
        
        self.setCentralWidget(self.cw.view)
        self.show()
        
        #QActionit voisi tehdä lyhyemmin
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
        
        action1 = QAction("MiniSuora",self)
        self.connect(action1, SIGNAL("triggered()"), self.setValitseKpl1)
        tb.addAction(action1)
        
        action2 = QAction("Suora",self)
        self.connect(action2, SIGNAL("triggered()"), self.setValitseKpl2)
        tb.addAction(action2)
        
        action3 = QAction("IsoSuora",self)
        self.connect(action3, SIGNAL("triggered()"), self.setValitseKpl3)
        tb.addAction(action3)
        
        action4 = QAction("Kaarre45",self)
        self.connect(action4, SIGNAL("triggered()"), self.setValitseKpl4)
        tb.addAction(action4)
        
        action5 = QAction("Kaarre30",self)
        self.connect(action5, SIGNAL("triggered()"), self.setValitseKpl5)
        tb.addAction(action5)
        
        action6 = QAction("MiniKaarre45",self)
        self.connect(action6, SIGNAL("triggered()"), self.setValitseKpl6)
        tb.addAction(action6)
        
        action7 = QAction("MiniKaarre30",self)
        self.connect(action7, SIGNAL("triggered()"), self.setValitseKpl7)
        tb.addAction(action7)
        
        action8 = QAction("Risteys",self)
        self.connect(action8, SIGNAL("triggered()"), self.setValitseKpl8)
        tb.addAction(action8)
        
        action9 = QAction("Vinoristeys",self)
        self.connect(action9, SIGNAL("triggered()"), self.setValitseKpl9)
        tb.addAction(action9)
        
        action10 = QAction("3-vaihde",self)
        self.connect(action10, SIGNAL("triggered()"), self.setValitseKpl10)
        tb.addAction(action10)
        
        action11 = QAction("3-vaihde (peili)",self)
        self.connect(action11, SIGNAL("triggered()"), self.setValitseKpl11)
        tb.addAction(action11)
        
        action12 = QAction("4-vaihde",self)
        self.connect(action12, SIGNAL("triggered()"), self.setValitseKpl12)
        tb.addAction(action12)
        
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
        try:
            fileName = QFileDialog.getOpenFileName(self, 'Open File','jnrta','*.txt')
            if fileName:
                self.uusiRata()
                f = open(fileName)
                line = f.readline().rstrip('\n')
                while line != '':
                    tyyppi = int(line)
                    x = float(f.readline().rstrip('\n'))
                    y = float(f.readline().rstrip('\n'))
                    kierto = float(f.readline().rstrip('\n'))
                    line = f.readline().rstrip('\n')
                    self.valitseKpl(tyyppi, x, y, kierto, 0)
                self.cw.view.rakenna()
        except:
            print('User tried to open corrupt data. Closing program.')
            self.sulje()
        
    def sulje(self):
        self.close()
    
    # Liittyy QActioneihin, voisi mahdollisesti tehdä tehokkaammin
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
    def setValitseKpl8(self):
        self.valitseKpl(8, -1000, -1000, 0, 1)
    def setValitseKpl9(self):
        self.valitseKpl(9, -1000, -1000, 0, 1)
    def setValitseKpl10(self):
        self.valitseKpl(10, -1000, -1000, 0, 1)
    def setValitseKpl11(self):
        self.valitseKpl(11, -1000, -1000, 0, 1)
    def setValitseKpl12(self):
        self.valitseKpl(12, -1000, -1000, 0, 1)
        
        
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
        if nro == 8:
            rist = Risteys([x,y])
            self.lisaaKpl(rist, kierto, selected)
        if nro == 9:
            vrist = vinoRisteys([x,y])
            self.lisaaKpl(vrist, kierto, selected)
        if nro == 10:
            v3 = vaihde3([x,y])
            self.lisaaKpl(v3, kierto, selected)
        if nro == 11:
            v3p = vaihde3peili([x,y])
            self.lisaaKpl(v3p, kierto, selected)
        if nro == 12:
            v4 = vaihde4([x,y])
            self.lisaaKpl(v4, kierto, selected)
        
    def lisaaKpl(self, ratakappale, kierto, selected):
        self.kappalelista.append(ratakappale)
        ratakappale.item.setParentItem(ratakappale)
        self.cw.scene.addItem(ratakappale)
        if selected == 1:
            ratakappale.item.setSelected(True)
        if selected == 0:
            ratakappale.pyorita(kierto)

def main():
    
        app = QApplication(sys.argv)
        usr = User()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()