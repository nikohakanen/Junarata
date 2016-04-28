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


    def __init__(self):
        '''
        Constructor
        '''
        super(MyView, self).__init__()
        self.setMouseTracking(True)
        
    def mousePressEvent(self, event):
        selected_items = self.scene().selectedItems()
        
        if not selected_items:
                currentItem = self.itemAt(event.pos())
                if currentItem is not None:
                    currentItem.setSelected(True)
                    currentItem.parentItem().setZValue(1)
                
        else:
            currentItem = selected_items[0]
            #print("Item:",currentItem.pos().x(),currentItem.pos().y())
            #print("Scene:",currentItem.scenePos().x(),currentItem.scenePos().y())
            #print("event.pos():",event.pos().x(),event.pos().y())
            collision = False
            
            for anotherItem in self.items():
                if anotherItem != currentItem:
                    if currentItem.collidesWithItem(anotherItem,0x1):
                        collision = True
                    
            if collision == False:
                currentItem.setSelected(False)
                currentItem.parentItem().setZValue(0)
                #currentItem.setPos(event.pos())
        #self.pathitem.setFlag(0x1,True) #ItemIsMovable
        #self.pathitem.setFlag(0x2,True)
    
    def mouseMoveEvent(self, event):
        selected_items = self.scene().selectedItems()
        if selected_items:
            currentItem = selected_items[0]
            currentItem.setBrush(QColor(0, 110, 10))
            currentItem.setPos(event.pos())
            for anotherItem in self.items():
                if anotherItem != currentItem:
                    if currentItem.collidesWithItem(anotherItem,0x1):
                        currentItem.setBrush(QColor(250, 0, 0))
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
                
        
        
        
        
        
        
        