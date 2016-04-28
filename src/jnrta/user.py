'''
Created on Mar 17, 2016

@author: hakanen1
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from jnrta.alusta import *
from jnrta.kappale import *
from jnrta.centralwidget import *

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

        self.cw = CentralWidget(self)
        
        self.setGeometry(0, 0, 920, 720)
        self.setWindowTitle('Pienoisrautatie')
        
        
        self.setCentralWidget(self.cw.view)
        self.show()
        
        
        action0 = QAction("Stopperi",self)
        self.connect(action0, SIGNAL("triggered()"), self.setValitseKpl0)
        tb.addAction(action0)
        
        action5 = QAction("Kaarre30",self)
        self.connect(action5, SIGNAL("triggered()"), self.setValitseKpl5)
        tb.addAction(action5)
    
    def test(self):
        color = QColor(0, 110, 10)
        pen = QPen(QColor(0,0,0))
        brush = QBrush(color)
        
        qpp = QPainterPath()
        
        kaarre45 = Kaarre45([700,500])
        xk = kaarre45.sijainti[0]
        yk = kaarre45.sijainti[1]
        ak = 20
        rk = kaarre45.r
        angk = kaarre45.ang
        qpp.moveTo(xk+2*rk-ak,yk+rk)
        qpp.arcTo(xk,yk,2*rk,2*rk,0,angk)
        
        qpp.arcTo(xk+ak,yk+ak,2*(rk-ak),2*(rk-ak),angk,-angk)
        self.cw.scene.addRect(xk+rk,yk,rk,rk)
        
        pathitem = QGraphicsPathItem()
        pathitem.setPen(pen)
        pathitem.setBrush(brush)
        pathitem.setPath(qpp)
        self.cw.scene.addItem(pathitem)

        self.cw.scene.addRect(400,400,200,200)
        self.cw.scene.addRect(400+100,400,100,100)
        
        self.cw.scene.addRect(0,0,200,200)
    
    def setValitseKpl0(self):
        self.valitseKpl(0)
        
    def setValitseKpl5(self):
        self.valitseKpl(5)
        
    def valitseKpl(self, nro):
        if nro == 0:
            stopperi = Stopperi([-100,-100])
            self.lisaaKpl(stopperi)
        if nro == 5:
            kare30 = Kaarre30([-100,-100])
            self.lisaaKpl(kare30)
        
    def lisaaKpl(self, ratakappale):
        ratakappale.item().setParentItem(ratakappale)
        self.cw.scene.addItem(ratakappale)
        ratakappale.item().setSelected(True)
        
    def rotate(self, ratakappale, ang):
        ratakappale.pyorita(ang)
        #ratakappale.item().setTransformOriginPoint(QPointF(ratakappale.keskikohta[0],ratakappale.keskikohta[1]))
        #ratakappale.item().setRotation(ang)
        #ratakappale.item().setTransformOriginPoint(QPointF(0,0))

def main():
    
        app = QApplication(sys.argv)
        usr = User()
        #usr.test()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()