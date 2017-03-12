'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import QGraphicsItem, QPen, QBrush, QColor, QGraphicsRectItem, QPainterPath, QGraphicsPathItem, QPolygonF, QGraphicsPolygonItem
from PyQt4.QtCore import QRectF, QPointF
from liitoskohta import *
import math

class Ratakappale(QGraphicsItem):
    '''
    "Grandparent" luokka varsinaisille QGraphicsItem ratakappaleille.
    Tämän luokan alaluokan Stopperi jne. ovat "parent" luokkia varsinaisille QGraphicsItem ratakappaleille.
    Sisältää kaikille ratakappaleille yhteiset tiedot ja metodit.
    '''

    def __init__(self, sijainti, tyyppi):
        '''
        Constructor
        '''
        super(Ratakappale, self).__init__()
        self.kierto = 0
        self.sijainti = sijainti
        self.tyyppi = tyyppi       #{0:'Stopperi', 1:'Suora1' ...}
        self.liitoskohdat = []
        self.naapurikappaleet = []

        self.pen = QPen(QColor(0,0,0))
        self.brush = QBrush(QColor(0, 110, 10))

    def pyorita(self, kulma):
        self.kierto = self.kierto + kulma
        self.kierto = self.kierto % 360
        for liitoskohta in self.liitoskohdat:
            liitoskohta.suunta = liitoskohta.suunta + kulma
            liitoskohta.suunta = liitoskohta.suunta % 360
        self.item.setRotation(self.kierto)

    def poista(self):
        self.scene().view().kappalelista.remove(self)
        self.scene().removeItem(self)

    def palautaNaapuri(self, nro):
        return self.naapurikappaleet[nro]

    def loopFound(self, previous, looper):
        'Etsii rekursiivisesti itseään (looper) kaikista linkittyneistä kappaleista'
        'Palauttaa true jos silmukka löytyy muuten false'
        try:
            nmax = len(self.naapurikappaleet)
            if nmax > 1:
                for n in range(0,nmax):
                    while self.palautaNaapuri(n) != previous:
                        if self.palautaNaapuri(n) == looper:
                            return True
                        else:
                            loopfound = self.palautaNaapuri(n).loopFound(self,looper)
                            if loopfound:
                                return True
                            else:
                                return False
            else:
                return False
        except RuntimeError:
            return True

    def boundingRect(self):
        pass

    ### Tästä alkaa Ratakappaleen alaluokat. Ne voisi toteuttaa tehokkaammin esim kaarteet yhdellä luokalla eri parametreilla

class Stopperi(Ratakappale):

    def __init__(self, sijainti):

        super(Stopperi, self).__init__(sijainti, 0)

        self.item = QGraphicsRectItem(-10,-10,20,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta = Liitoskohta(12,0,0,self.item)
        self.liitoskohdat.append(liitoskohta)

        stopbar = QGraphicsRectItem(-10,-10,7,20,self.item)
        stopbar.setBrush(QColor(170,0,0))

    def boundingRect(self):
        return QRectF(-11,-11,22,22)

    def paint(self, painter, options, widget):
        pass


class Suora1(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 1)

        self.item = QGraphicsRectItem(-10,-10,20,20)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta1 = Liitoskohta(-12,0,180,self.item)
        liitoskohta2 = Liitoskohta(12,0,0,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)

    def boundingRect(self):
        return QRectF(-11,-11,22,22)

    def paint(self, painter, options, widget):
        pass

class Suora2(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 2)

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

    def __init__(self, sijainti):

        super().__init__(sijainti, 3)

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

        self.x = 0
        self.y = 0
        self.a = 20
        self.r = 100
        self.ang = 45
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)

        super().__init__(sijainti, 4)



        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)

        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)


        self.item.setPos(sijainti[0],sijainti[1])
        self.item.setFlag(0x2,True)

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


        self.x = 0
        self.y = 0
        self.a = 20
        self.r = 100
        self.ang = 30
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)

        super().__init__(sijainti, 5)



        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)

        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)


        self.item.setPos(sijainti[0],sijainti[1])
        self.item.setFlag(0x2,True)

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

        self.x = 0
        self.y = 0
        self.a = 20
        self.r = 50
        self.ang = 45
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)

        super().__init__(sijainti, 6)



        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)

        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)


        self.item.setPos(sijainti[0],sijainti[1])
        self.item.setFlag(0x2,True)

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

        self.x = 0
        self.y = 0
        self.a = 20
        self.r = 50
        self.ang = 30
        ang_rad = math.radians(self.ang)
        arc_x = self.x + self.r + (self.r-self.a/2)*math.cos(ang_rad/2)
        arc_y = self.y + self.r - (self.r-self.a/2)*math.sin(ang_rad/2)

        super().__init__(sijainti, 7)



        qpp = QPainterPath()
        qpp.moveTo(self.x+2*self.r-self.a-arc_x,self.y+self.r-arc_y)
        qpp.arcTo(self.x-arc_x,self.y-arc_y,2*self.r,2*self.r,0,self.ang)
        qpp.arcTo(self.x+self.a-arc_x,self.y+self.a-arc_y,2*(self.r-self.a),2*(self.r-self.a),self.ang,-self.ang)

        self.item = QGraphicsPathItem()
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setPath(qpp)


        self.item.setPos(sijainti[0],sijainti[1])
        self.item.setFlag(0x2,True)

        liitoskohta1 = Liitoskohta(self.r*(math.cos(math.radians(0))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(0))),90,self.item)
        liitoskohta2 = Liitoskohta(self.r*(math.cos(math.radians(self.ang))-math.cos(math.radians(self.ang/2))),self.r*(math.sin(math.radians(self.ang/2))-math.sin(math.radians(self.ang))),-(90+self.ang),self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)


    def boundingRect(self):
        return QRectF(-25,-25,self.r,self.r)

    def paint(self, painter, option, widget):
        pass


class Risteys(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 8)

        listOfPoints = [[-10,-10],[-10,-30],[10,-30],[10,-10],[30,-10],[30,10],[10,10],[10,30],[-10,30],[-10,10],[-30,10],[-30,-10]]
        listOfQPoints = []
        for i in listOfPoints:
            x = i[0]
            y = i[1]
            listOfQPoints.append(QPointF(x,y))

        polygon = QPolygonF(listOfQPoints)
        self.item = QGraphicsPolygonItem(polygon)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta1 = Liitoskohta(-32,0,180,self.item)
        liitoskohta2 = Liitoskohta(32,0,0,self.item)
        liitoskohta3 = Liitoskohta(0,-32,-90,self.item)
        liitoskohta4 = Liitoskohta(0,32,90,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        self.liitoskohdat.append(liitoskohta3)
        self.liitoskohdat.append(liitoskohta4)

    def boundingRect(self):
        return QRectF(-31,-31,62,62)

    def paint(self, painter, options, widget):
        pass

class vinoRisteys(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 9)

        listOfPoints = [[-10,-30],[10,-30],[10,-20],[20,-30],[30,-20],[10,0],[10,30],[-10,30],[-10,20],[-20,30],[-30,20],[-10,0]]
        listOfQPoints = []
        for i in listOfPoints:
            x = i[0]
            y = i[1]
            listOfQPoints.append(QPointF(x,y))

        polygon = QPolygonF(listOfQPoints)
        self.item = QGraphicsPolygonItem(polygon)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta1 = Liitoskohta(-26,26,135,self.item)
        liitoskohta2 = Liitoskohta(26,-26,-45,self.item)
        liitoskohta3 = Liitoskohta(0,-32,-90,self.item)
        liitoskohta4 = Liitoskohta(0,32,90,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        self.liitoskohdat.append(liitoskohta3)
        self.liitoskohdat.append(liitoskohta4)

    def boundingRect(self):
        return QRectF(-31,-31,62,62)

    def paint(self, painter, options, widget):
        pass

class vaihde3(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 10)

        listOfPoints = [[-10,-30],[10,-30],[10,-20],[20,-30],[30,-20],[10,0],[10,30],[-10,30]]
        listOfQPoints = []
        for i in listOfPoints:
            x = i[0]
            y = i[1]
            listOfQPoints.append(QPointF(x,y))

        polygon = QPolygonF(listOfQPoints)
        self.item = QGraphicsPolygonItem(polygon)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta2 = Liitoskohta(26,-26,-45,self.item)
        liitoskohta3 = Liitoskohta(0,-32,-90,self.item)
        liitoskohta4 = Liitoskohta(0,32,90,self.item)
        self.liitoskohdat.append(liitoskohta2)
        self.liitoskohdat.append(liitoskohta3)
        self.liitoskohdat.append(liitoskohta4)

    def boundingRect(self):
        return QRectF(-31,-31,62,62)

    def paint(self, painter, options, widget):
        pass

class vaihde3peili(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 11)

        listOfPoints = [[-10,-30],[10,-30],[10,0],[30,20],[20,30],[10,20],[10,30],[-10,30]]
        listOfQPoints = []
        for i in listOfPoints:
            x = i[0]
            y = i[1]
            listOfQPoints.append(QPointF(x,y))

        polygon = QPolygonF(listOfQPoints)
        self.item = QGraphicsPolygonItem(polygon)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta2 = Liitoskohta(26,26,45,self.item)
        liitoskohta3 = Liitoskohta(0,-32,-90,self.item)
        liitoskohta4 = Liitoskohta(0,32,90,self.item)
        self.liitoskohdat.append(liitoskohta2)
        self.liitoskohdat.append(liitoskohta3)
        self.liitoskohdat.append(liitoskohta4)

    def boundingRect(self):
        return QRectF(-31,-31,62,62)

    def paint(self, painter, options, widget):
        pass

class vaihde4(Ratakappale):

    def __init__(self, sijainti):

        super().__init__(sijainti, 12)

        listOfPoints = [[-10,-30],[10,-30],[10,-20],[20,-30],[30,-20],[10,0],[10,30],[-10,30],[-10,0],[-30,-20],[-20,-30],[-10,-20]]
        listOfQPoints = []
        for i in listOfPoints:
            x = i[0]
            y = i[1]
            listOfQPoints.append(QPointF(x,y))

        polygon = QPolygonF(listOfQPoints)
        self.item = QGraphicsPolygonItem(polygon)
        self.item.setPen(self.pen)
        self.item.setBrush(self.brush)
        self.item.setFlag(0x2,True)
        self.item.setPos(sijainti[0],sijainti[1])

        liitoskohta1 = Liitoskohta(-26,-26,-135,self.item)
        liitoskohta2 = Liitoskohta(26,-26,-45,self.item)
        liitoskohta3 = Liitoskohta(0,-32,-90,self.item)
        liitoskohta4 = Liitoskohta(0,32,90,self.item)
        self.liitoskohdat.append(liitoskohta1)
        self.liitoskohdat.append(liitoskohta2)
        self.liitoskohdat.append(liitoskohta3)
        self.liitoskohdat.append(liitoskohta4)

    def boundingRect(self):
        return QRectF(-31,-31,62,62)

    def paint(self, painter, options, widget):
        pass
