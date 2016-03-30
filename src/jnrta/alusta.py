'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from pkt.kappale import *

class Alusta(QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        super(Alusta, self).__init__()
        
        self.lista = []
        
        
        self.buttonklik = False
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        
        btn = QPushButton("Testi", self)
        btn.move(300,300)
        btn.clicked.connect(self.buttonClicked)
        
        self.show()
    
    def paintEvent(self, e):
        
        qp = QPainter()
        qp.begin(self)
        color = QColor(130, 80, 0)
        qp.setPen(QColor(0,0,0))
        qp.drawLine(0,0,999,999)
        
        qp.drawRect(200,50,80,20)
        
        qp.drawRect(350,50,100,100)
        qp.drawRect(450,50,200,200)
        
        qpp3 = QPainterPath()
        qpp3.moveTo(430,100)
        qpp3.arcTo(350,50,100,100,0,45)
        
        qpp3.moveTo(450+180,50+100)
        qpp3.arcTo(450,50,200,200,0,45)
        
        qpp3.arcTo(470,70,160,160,45,-45)
        
        qp.drawPath(qpp3)
        
        
        if self.buttonklik == True:
            qpp2 = QPainterPath()
            qpp2.addRect(50,50,60,90)
            qpp2.addRect(200,50,50,100)
            qpp2.moveTo(200,150)
            qpp2.arcTo(200,50,50,100,-90,100)
            qp.fillRect(50,50,60,90,color)
            qp.drawPath(qpp2)
        
        qpp = QPainterPath()
        qpp.addRect(0,0,60,60)
        
        
        for x in self.lista:
            if x.tyyppi == 1:
                qpp.addRect(60,60,100,100)
        
        qp.drawPath(qpp)       
        
        qp.end()
        
    def lisaaKpl(self, Ratakappale):
        
        self.lista.append(Ratakappale)
        
        
    def buttonClicked(self):
        
        self.buttonklik = True
        self.lista[1].tyyppi = 1
        self.update()
        
        
        
        
        
        
        