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
        
        btn2 = QPushButton("pyöritä", self)
        btn2.move(600,300)
        btn2.clicked.connect(self.button2Clicked)
        
        self.show()
    
    def paintEvent(self, e):
        
        qp = QPainter()
        qp.begin(self)
        color = QColor(0, 110, 10)
        qp.setBrush(color)
        
        qp.end()
        
        x = 0
        y = 0
        r = 100
        ang = 45
        ang_rad = math.radians(ang)
        a = 20
        arc_x = x + r + (r-a/2)*math.cos(ang_rad/2)
        arc_y = y + r - (r-a/2)*math.sin(ang_rad/2)
        
        if self.buttonklik == -1: #piirtää kaarteen
            qp2 = QPainter() ###
            qp2.begin(self)
            
            qpp4 = QPainterPath()        
            
            qpp4.moveTo(x+2*r-a,y+r)
            qpp4.arcTo(x,y,2*r,2*r,0,ang)
            
            qpp4.arcTo(x+a,y+a,2*(r-a),2*(r-a),45,-45)
        
            qp2.setBrush(color);
            qp2.drawPath(qpp4)
    
            qp2.end()
            
        if self.buttonklik == 1: #pyörittää kaarretta 33 astetta
            qp2 = QPainter() ###
            qp2.begin(self)
        
            #origo pitää siirtää kappaleen keskikohtaan
            
            qpp4 = QPainterPath()        
            
            qp2.translate(arc_x,arc_y)
            qp2.rotate(33)
            
            qpp4.moveTo(x+2*r-a-arc_x,y+r-arc_y)
            qpp4.arcTo(x-arc_x,y-arc_y,2*r,2*r,0,ang)
            
            qpp4.arcTo(x+a-arc_x,y+a-arc_y,2*(r-a),2*(r-a),45,-45)
        
            qp2.setBrush(color);
            qp2.drawPath(qpp4)
    
            qp2.end()
        
        qp.begin(self)
        qp.setBrush(color)
        
        if self.buttonklik == 0: #Simuloi ratakappaleen lisäämistä
            qpp = QPainterPath()
            
            for ratapala in self.lista: 
                if ratapala.tyyppi in (1,2,3,4): #piirtää suorakulmaiset ratakappaleet
                    qpp.addRect(ratapala.sijainti[0],ratapala.sijainti[1],ratapala.leveys,ratapala.korkeus)
                
                if ratapala.tyyppi in (5,6,7,8): #piirtää kaarteet
                    
                    ###KESKEN###
                    
                    #qpp.moveTo(ratapala.sijainti[0]+2*r-a,ratapala.sijainti[1]+r)
                    #qpp.arcTo(x,y,2*r,2*r,0,ang)
                    
                    #qpp.arcTo(x+a,y+a,2*(r-a),2*(r-a),45,-45)
                    xasd = 1
                    
            qp.drawPath(qpp)    
            
            qpp4 = QPainterPath()        
            
            qpp4.moveTo(x+2*r-a,y+r)
            qpp4.arcTo(x,y,2*r,2*r,0,ang)
            
            qpp4.arcTo(x+a,y+a,2*(r-a),2*(r-a),45,-45)
            qp.drawPath(qpp4) 
        
        qp.end()
        
    def lisaaKpl(self, Ratakappale):
        
        self.lista.append(Ratakappale)
        
        
    def buttonClicked(self):

        #lisätään muutama kappale alustalle

        stopperi = Stopperi([750,600])
        minisuora = Suora1([780,600])
        normisuora = Suora2([750,650])
        
        self.lisaaKpl(stopperi)
        self.lisaaKpl(minisuora)
        self.lisaaKpl(normisuora)

        self.buttonklik = 0
        self.update()

            
    def button2Clicked(self):

        self.buttonklik = 1
        self.update()
    
        
        