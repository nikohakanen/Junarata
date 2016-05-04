'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from jnrta.liitoskohta import *
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
        self.tyyppi = tyyppi       #{0:'Stopperi', 1:'Suora' ...}
        self.liitoskohdat = []
        self.naapurikappaleet = []
        self.tila = 0 #{0: None, 1: Alustalla, 2: Poimittu}
        
        self.pen = QPen(QColor(0,0,0))
        self.brush = QBrush(QColor(0, 110, 10))
        
    def pyorita(self, kulma):
        self.kierto = self.kierto + kulma
        self.kierto = self.kierto % 360
        for liitoskohta in self.liitoskohdat:
            liitoskohta.suunta = liitoskohta.suunta + kulma
            liitoskohta.suunta = liitoskohta.suunta % 360
        #self.item.setTransformOriginPoint(QPointF(self.keskikohta[0],self.keskikohta[1]))
        self.item.setRotation(self.kierto)
        #self.item.setTransformOriginPoint(QPointF(0,0))
    
    def palautaNaapuri(self, nro):
        return self.naapurikappaleet[nro]
    
    def loopFound(self, previous, looper):
        nmax = len(self.naapurikappaleet)
        if nmax > 1:
            for n in range(0,nmax):
                while self.palautaNaapuri(n) != previous:
                    if self.palautaNaapuri(n) == looper:
                        return True
                    #if self.palautaNaapuri(n).tyyppi == 0: #stopper
                        #return False
                    else:
                        loopfound = self.palautaNaapuri(n).loopFound(self,looper)
                        if loopfound:
                            return True
                        else:
                            return False
        else:
            return False
        
    def boundingRect(self):
        pass
    
    def item(self):
        pass
        
class Stopperi(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super(Stopperi, self).__init__([sijainti[0]+10,sijainti[1]+10], 0, 20, 20, sijainti, 0)
        
        self.item = QGraphicsRectItem(-10,-10,20,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])
        
        liitoskohta = Liitoskohta(12,0,0,self.item)
        self.liitoskohdat.append(liitoskohta)

    def boundingRect(self):
        return QRectF(-11,-11,22,22)
    
    def paint(self, painter, options, widget):
        pass
        
        
class Suora1(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+20,sijainti[1]+10], 0, 40, 20, sijainti, 1)
        
        self.item = QGraphicsRectItem(-20,-10,40,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])
        
        liitoskohta1 = Liitoskohta(-22,0,180,self.item)
        liitoskohta2 = Liitoskohta(22,0,0,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)

    def boundingRect(self):
        return QRectF(-21,-11,42,22)
    
    def paint(self, painter, options, widget):
        pass
        
class Suora2(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+30,sijainti[1]+10], 0, 60, 20, sijainti, 2)
        
        self.item = QGraphicsRectItem(-30,-10,60,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])
        
        liitoskohta1 = Liitoskohta(-32,0,180,self.item)
        liitoskohta2 = Liitoskohta(32,0,0,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)

    def boundingRect(self):
        return QRectF(-31,-11,62,22)
    
    def paint(self, painter, options, widget):
        pass
        
class Suora3(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+45,sijainti[1]+10], 0, 90, 20, sijainti, 3)
        
        self.item = QGraphicsRectItem(-45,-10,90,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])
        
        liitoskohta1 = Liitoskohta(-47,0,180,self.item)
        liitoskohta2 = Liitoskohta(47,0,0,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)

    def boundingRect(self):
        return QRectF(-46,-11,92,22)
    
    def paint(self, painter, options, widget):
        pass

class Kaarre45(Ratakappale):

    def __init__(self, sijainti):

        self.x = 0 #sijainti[0]
        self.y = 0 #sijainti[1]
        self.a = 20
        self.r = 100
        self.ang = 45
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 4)
        

        
        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)
        
        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)
        
        #self.item.setTransformOriginPoint(QPointF(arc_x,arc_y))
        
        self.item.setPos(sijainti[0],sijainti[1]) #items must be drawn in origin and moved
        #self.item.setFlag(0x1,True) #ItemIsMovable
        self.item.setFlag(0x2,True) #ItemIsSelectable
        #self.item.setAcceptDrops(True)
        
        liitoskohta1 = Liitoskohta(self.r*(math.cos(math.radians(0))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(0))),90,self.item)
        liitoskohta2 = Liitoskohta(self.r*(math.cos(math.radians(self.ang))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(self.ang))),-(90+self.ang),self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        
        
    def boundingRect(self):
        return QRectF(-50,-50,self.r,self.r)
    
    def paint(self, painter, option, widget):
        pass
        
    
class Kaarre30(Ratakappale):

    def __init__(self, sijainti):


        self.x = 0 #sijainti[0]
        self.y = 0 #sijainti[1]
        self.a = 20
        self.r = 100
        self.ang = 30
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 5)
        

        
        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)
        
        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)
        
        #self.item.setTransformOriginPoint(QPointF(arc_x,arc_y))
        
        self.item.setPos(sijainti[0],sijainti[1]) #items must be drawn in origin and moved
        #self.item.setFlag(0x1,True) #ItemIsMovable
        self.item.setFlag(0x2,True) #ItemIsSelectable
        #self.item.setAcceptDrops(True)
        
        liitoskohta1 = Liitoskohta(self.r*(math.cos(math.radians(0))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(0))),90,self.item)
        liitoskohta2 = Liitoskohta(self.r*(math.cos(math.radians(self.ang))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(self.ang))),-(90+self.ang),self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        
        
    def boundingRect(self):
        return QRectF(-50,-50,self.r,self.r)
    
    def paint(self, painter, option, widget):
        pass
        
class Kaarre45mini(Ratakappale):

    def __init__(self, sijainti):

        self.x = 0 #sijainti[0]
        self.y = 0 #sijainti[1]
        self.a = 20
        self.r = 50
        self.ang = 45
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 6)
        

        
        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)
        
        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)
        
        #self.item.setTransformOriginPoint(QPointF(arc_x,arc_y))
        
        self.item.setPos(sijainti[0],sijainti[1]) #items must be drawn in origin and moved
        #self.item.setFlag(0x1,True) #ItemIsMovable
        self.item.setFlag(0x2,True) #ItemIsSelectable
        #self.item.setAcceptDrops(True)
        
        liitoskohta1 = Liitoskohta(self.r*(math.cos(math.radians(0))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(0))),90,self.item)
        liitoskohta2 = Liitoskohta(self.r*(math.cos(math.radians(self.ang))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(self.ang))),-(90+self.ang),self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        
        
    def boundingRect(self):
        return QRectF(-25,-25,self.r,self.r)
    
    def paint(self, painter, option, widget):
        pass
        
        
        
class Kaarre30mini(Ratakappale):

    def __init__(self, sijainti):

        self.x = 0 #sijainti[0]
        self.y = 0 #sijainti[1]
        self.a = 20
        self.r = 50
        self.ang = 30
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 2*self.r, 2*self.r, sijainti, 7)
        

        
        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)
        
        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)
        
        #self.item.setTransformOriginPoint(QPointF(arc_x,arc_y))
        
        self.item.setPos(sijainti[0],sijainti[1]) #items must be drawn in origin and moved
        #self.item.setFlag(0x1,True) #ItemIsMovable
        self.item.setFlag(0x2,True) #ItemIsSelectable
        #self.item.setAcceptDrops(True)
        
        liitoskohta1 = Liitoskohta(self.r*(math.cos(math.radians(0))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(0))),90,self.item)
        liitoskohta2 = Liitoskohta(self.r*(math.cos(math.radians(self.ang))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(self.ang))),-(90+self.ang),self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        
        
    def boundingRect(self):
        return QRectF(-25,-25,self.r,self.r)
    
    def paint(self, painter, option, widget):
        pass
    
    
    
    
    
    
    
    
        