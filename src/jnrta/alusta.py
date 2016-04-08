'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from jnrta.kappale import *
import math

class Alusta(QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        super(Alusta, self).__init__()
        
        self.lista = []
        
        
        self.buttonklik = -1
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        
        btn = QPushButton("Lisää kpl", self)
        btn.move(300,300)
        btn.clicked.connect(self.buttonClicked)
        self.show()
    
    def paintEvent(self, e):
        
        color = QColor(0, 110, 10)
        
        if self.buttonklik == 0: #Simuloi ratakappaleen lisäämistä
            for ratapala in self.lista: 
                qpx = QPainter()
                qpx.begin(self)
                qpp = QPainterPath()
                qpx.setBrush(color)
                qpx.translate(ratapala.keskikohta[0],ratapala.keskikohta[1])
                qpx.rotate(ratapala.kierto)
                
                if ratapala.tyyppi in (1,2,3,4): #piirtää suorakulmaiset ratakappaleet
                    
                    qpp.addRect(ratapala.sijainti[0]-ratapala.keskikohta[0],ratapala.sijainti[1]-ratapala.keskikohta[1],ratapala.leveys,ratapala.korkeus)
                
                if ratapala.tyyppi in (5,6,7,8): #piirtää kaarteet
                    
                    xk = ratapala.sijainti[0]
                    yk = ratapala.sijainti[1]
                    ak = 20
                    rk = ratapala.r
                    angk = ratapala.ang
                    qpp.moveTo(xk+2*rk-ak-ratapala.keskikohta[0],yk+rk-ratapala.keskikohta[1])
                    qpp.arcTo(xk-ratapala.keskikohta[0],yk-ratapala.keskikohta[1],2*rk,2*rk,0,angk)
                    
                    qpp.arcTo(xk+ak-ratapala.keskikohta[0],yk+ak-ratapala.keskikohta[1],2*(rk-ak),2*(rk-ak),angk,-angk)
                
                qpx.drawPath(qpp)
                qpx.end()
        
    def lisaaKpl(self, Ratakappale):
        
        self.lista.append(Ratakappale)
        
        
    def buttonClicked(self):

        #lisätään muutama kappale alustalle

        stopperi = Stopperi([750,600])
        minisuora = Suora1([780,600])
        normisuora = Suora2([750,650])
        kaarre45 = Kaarre45([700,500])
        kaarre30 = Kaarre30([400,200])
        kaarre45mini = Kaarre45mini([450,250])
        kaarre30mini = Kaarre30mini([350,250])
        normisuora.pyorita(33)
        kaarre45mini.pyorita(-120)
        
        self.lisaaKpl(stopperi)
        self.lisaaKpl(minisuora)
        self.lisaaKpl(normisuora)
        self.lisaaKpl(kaarre45)
        self.lisaaKpl(kaarre30)
        self.lisaaKpl(kaarre45mini)
        self.lisaaKpl(kaarre30mini)

        self.buttonklik = 0
        self.update()
        
        