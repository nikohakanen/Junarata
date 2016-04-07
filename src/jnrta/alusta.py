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
        qp.setPen(QColor(0,0,0))
        qp.drawLine(0,0,999,999)
        
        qp.drawRect(200,50,80,20)
        
        qp.drawRect(350,50,100,100)
        qp.drawRect(0,0,200,200)
        
        qpp3 = QPainterPath()
        qpp3.moveTo(430,100)
        qpp3.arcTo(350,50,100,100,0,45)
        
        qp.drawPath(qpp3)
        
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
        
        if self.buttonklik == 0: #Simuloi ratakappaleen lisäämistä
            qpp = QPainterPath()
            qp.setBrush(color)
            
            for ratapala in self.lista:
                if ratapala.tyyppi == 1:
                    qpp.addRect(60,60,100,20)
            
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

        self.buttonklik = 0
        self.lista[0].tyyppi = 1
        self.update()

            
    def button2Clicked(self):

        self.buttonklik = 1
        self.update()
    
        
        