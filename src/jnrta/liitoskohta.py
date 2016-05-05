'''
Created on Apr 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Liitoskohta(QGraphicsRectItem):
    '''
    classdocs
    '''


    def __init__(self, x, y, kierto, parent):
        '''
        Constructor
        '''
        
        super(Liitoskohta, self).__init__(-3,-10,6,20,parent)
        
        self.suunta = kierto % 360
        self.vapaa = True
        self.vastapala = None
        
        self.setBrush(QColor(0,200,250))
        self.setOpacity(0.5)
        self.setRotation(self.suunta)
        self.setPos(x,y)
        arrow = QGraphicsRectItem(2,-2,10,4,self)
        arrow.setBrush(QColor(0,0,250))
        
    def isFree(self):
        return self.vapaa
    
    def setFree(self):
        self.vastapala.ratakappale().naapurikappaleet.remove(self.ratakappale())
        self.ratakappale().naapurikappaleet.remove(self.vastapala.ratakappale())
        self.vapaa = True
        self.vastapala.vapaa = True
        self.vastapala.vastapala = None
        self.vastapala = None
        
    def ratakappale(self):
        # Returns the Ratakappale grandparent item
        return self.parentItem().parentItem()
        
    def liita(self, vastaliitos):
        self.vastapala = vastaliitos
        self.vastapala.vastapala = self
        self.vapaa = False
        self.vastapala.vapaa = False
        
        self.ratakappale().naapurikappaleet.append(vastaliitos.ratakappale())
        self.vastapala.ratakappale().naapurikappaleet.append(self.ratakappale())
        #print(self.ratakappale().naapurikappaleet)
        
        loopfound = self.ratakappale().loopFound(self.ratakappale(),self.ratakappale())
        if loopfound:
            self.ratakappale().scene().view().LoopText()
        
        
        
        
        
        
        
            
        
        