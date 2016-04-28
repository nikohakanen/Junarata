'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import math

class Ratakappale(QGraphicsItem):
    '''
    classdocs
    '''

    def __init__(self, keskikohta, kierto, leveys, korkeus, sijainti, tyyppi):
        '''
        Constructor
        '''
        super(Ratakappale, self).__init__()
        self.keskikohta = keskikohta
        self.kierto = kierto
        self.leveys = leveys
        self.korkeus = korkeus
        self.sijainti = sijainti    # esim. neliöllä vasen ylänurkka
        self.tyyppi = tyyppi       #{0:'None', 1:'Stopperi', 2:'Suora' ...}
        self.liitoskohdat = []
        self.naapurikappaleet = []
        self.tila = 0 #{0: None, 1: Alustalla, 2: Poimittu}
        
        self.pen = QPen(QColor(0,0,0))
        self.brush = QBrush(QColor(0, 110, 10))
        
    def lisaaNaapuri(self, naapurikappale):
        self.naapurikappaleet.append(naapurikappale)
        
    def lisaaLiitos(self, liitoskohta):
        self.liitoskohdat.append(liitoskohta)
        
    def pyorita(self, kulma):
        self.kierto = self.kierto + kulma
        self.item().setTransformOriginPoint(QPointF(self.keskikohta[0],self.keskikohta[1]))
        self.item().setRotation(self.kierto)
        self.item().setTransformOriginPoint(QPointF(0,0))
        
    def boundingRect(self):
        pass
    
    def item(self):
        pass
        
class Stopperi(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super(Stopperi, self).__init__([sijainti[0]+10,sijainti[1]+10], 0, 20, 20, sijainti, 1)
        
        self.sitem = QGraphicsRectItem(-10,-10,20,20)
        self.sitem.setPen(self.pen)
        self.sitem.setBrush(self.brush)
        self.sitem.setFlag(0x2,True)
        self.sitem.setPos(sijainti[0],sijainti[1])

    def boundingRect(self):
        return QRectF(-11,-11,22,22)
    
    def paint(self, painter, options, widget):
        pass
    
    def item(self):
        return self.sitem
        
        
class Suora1(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+20,sijainti[1]+10], 0, 40, 20, sijainti, 2)
        
class Suora2(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+30,sijainti[1]+10], 0, 60, 20, sijainti, 3)
        
class Suora3(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+45,sijainti[1]+10], 0, 90, 20, sijainti, 4)

class Kaarre45(Ratakappale):

    def __init__(self, sijainti):

        x = sijainti[0]
        y = sijainti[1]
        self.r = 100
        self.ang = 45
        a = 20
        ang_rad = math.radians(self.ang)
        arc_x = x + self.r + (self.r-a/2)*math.cos(ang_rad/2)
        arc_y = y + self.r - (self.r-a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 5)
    
class Kaarre30(Ratakappale):

    def __init__(self, sijainti):


        self.xk = 0 #sijainti[0]
        self.yk = 0 #sijainti[1]
        self.ak = 20
        self.rk = 100
        self.angk = 30
        ang_rad = math.radians(self.angk)
        arc_x = self.xk + self.rk + (self.rk-self.ak/2)*math.cos(ang_rad/2)
        arc_y = self.yk + self.rk - (self.rk-self.ak/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.rk, 2*self.rk, sijainti, 6)
        

        
        qpp = QPainterPath()
        qpp.moveTo(self.xk+2*self.rk-self.ak-arc_x,self.yk+self.rk-arc_y)
        qpp.arcTo(self.xk-arc_x,self.yk-arc_y,2*self.rk,2*self.rk,0,self.angk)
        qpp.arcTo(self.xk+self.ak-arc_x,self.yk+self.ak-arc_y,2*(self.rk-self.ak),2*(self.rk-self.ak),self.angk,-self.angk)
        
        self.pathitem = QGraphicsPathItem()
        self.pathitem.setPen(self.pen)
        self.pathitem.setBrush(self.brush)
        self.pathitem.setPath(qpp)
        
        #self.pathitem.setTransformOriginPoint(QPointF(arc_x,arc_y))
        
        self.pathitem.setPos(sijainti[0],sijainti[1]) #items must be drawn in origin and moved
        #self.pathitem.setFlag(0x1,True) #ItemIsMovable
        self.pathitem.setFlag(0x2,True) #ItemIsSelectable
        #self.pathitem.setAcceptDrops(True)
        
    def boundingRect(self):
        return QRectF(-50,-50,self.rk,self.rk)
    
    def paint(self, painter, option, widget):
        pass

    def item(self):
        return self.pathitem
        
class Kaarre45mini(Ratakappale):

    def __init__(self, sijainti):

        x = sijainti[0]
        y = sijainti[1]
        self.r = 50
        self.ang = 45
        a = 20
        ang_rad = math.radians(self.ang)
        arc_x = x + self.r + (self.r-a/2)*math.cos(ang_rad/2)
        arc_y = y + self.r - (self.r-a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 7)
        
        
        
class Kaarre30mini(Ratakappale):

    def __init__(self, sijainti):

        x = sijainti[0]
        y = sijainti[1]
        self.r = 50
        self.ang = 30
        a = 20
        ang_rad = math.radians(self.ang)
        arc_x = x + self.r + (self.r-a/2)*math.cos(ang_rad/2)
        arc_y = y + self.r - (self.r-a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 8)
    
    
    
    
    
    
    
    
        