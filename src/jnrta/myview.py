'''
Created on Apr 20, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyView(QGraphicsView):
    '''
    classdocs
    '''


    def __init__(self, kappalelista):
        '''
        Constructor
        '''
        super(MyView, self).__init__()
        self.kappalelista = kappalelista
        self.setMouseTracking(True)
        self.liitosOk = False
        self.tempLiitos = []
        self.tempVastin = []
        self.textItem = None
        
    def mousePressEvent(self, event):
        selected_items = self.scene().selectedItems()
        
        if not selected_items:
                currentItem = self.itemAt(event.pos())

                if currentItem is not None:
                    if currentItem.brush().color() == QColor(170,0,0) or currentItem.brush().color() == QColor(150,210,230):
                        currentItem = currentItem.parentItem()
                    currentItem.setSelected(True)
                    currentItem.parentItem().setZValue(1)
                    for liitoskohta in currentItem.parentItem().liitoskohdat:
                        if not liitoskohta.isFree():
                            liitoskohta.setFree()
                
        else:
            currentItem = selected_items[0]
            #print("Item:",currentItem.pos().x(),currentItem.pos().y())
            #print("Scene:",currentItem.scenePos().x(),currentItem.scenePos().y())
            #print("event.pos():",event.pos().x(),event.pos().y())
            collision = False
            
            for anotherItem in self.kappalelista:
                if anotherItem.item != currentItem:
                    if currentItem.collidesWithItem(anotherItem.item,0x1):
                        collision = True
                    
            if collision == False:
                currentItem.setSelected(False)
                currentItem.parentItem().setZValue(0)
                if self.liitosOk:
                    n = len(self.tempLiitokset)
                    for i in range(0,n):
                        self.tempLiitokset[i].liita(self.tempVastineet[i],0)
                #currentItem.setPos(event.pos())
        #self.pathitem.setFlag(0x1,True) #ItemIsMovable
        #self.pathitem.setFlag(0x2,True)
                                
            #print("##",event.pos().x(),event.pos().y(),"##")
            #print(currentItem.mapToScene(QPoint(0,0)).x(),currentItem.mapToScene(QPoint(0,0)).y())
        
    def keyPressEvent(self, event):
        selected_items = self.scene().selectedItems()
        if selected_items:
            key = event.key()
            currentItem = selected_items[0]
            
            if key == 0x01000014: #Key_Right
                currentItem.parentItem().pyorita(5)
                
            if key == 0x01000012: #Key_Right
                currentItem.parentItem().pyorita(-5)
                
            if key == 0x01000007: #Delete
                currentItem.parentItem().poista()
                
    def rakenna(self):
        for currentItem in self.kappalelista:
            for anotherItem in self.kappalelista:
                if anotherItem != currentItem:
                    for liitoskohta in currentItem.liitoskohdat:
                        if liitoskohta.vapaa:
                            for vastakohta in anotherItem.liitoskohdat:
                                if vastakohta.vapaa:
                                    if liitoskohta.collidesWithItem(vastakohta,0x1):
                                        liitoskohta.liita(vastakohta,1)
                                        
    def LoopText(self):
        self.textItem = QGraphicsTextItem()
        self.textItem.setPlainText('Muodostui silmukka')
        self.scene().addItem(self.textItem)
        self.textItem.setZValue(2)
        self.textItem.setPos(200,0)
        
        fontti = QFont()
        fontti.setPointSize(40)
        
        self.textItem.setFont(fontti)
        
        timer = QTimer()
        timer.singleShot(3000,self.removeLoopText)
        
    def removeLoopText(self):
        self.scene().removeItem(self.textItem)
                
        
        
        
        
        
        
        