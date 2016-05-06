'''
Created on May 5, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyScene(QGraphicsScene):
    '''
    Scene.
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        super(MyScene, self).__init__(parent)
        
    def view(self):
        views = self.views()
        return views[0]
        
    def mouseMoveEvent(self, event): #Tämä olisi muuten toteutettu MyView luokassa, mutta MyView luokan mouseMoveEvent ei osaa antaa scenen koordinaatteva event.scenePos()
        selected_items = self.selectedItems()
        if selected_items:
            currentItem = selected_items[0]
            currentItem.setBrush(QColor(0, 110, 10))
            currentItem.setPos(event.scenePos())
            self.view().liitosOk = False
            self.view().tempLiitokset = []
            self.view().tempVastineet = []
            for anotherItem in self.view().kappalelista:
                if anotherItem.item != currentItem:
                    if currentItem.collidesWithItem(anotherItem.item,0x1):
                        currentItem.setBrush(QColor(250, 0, 0))
                    for liitoskohta in currentItem.parentItem().liitoskohdat:
                        for vastakohta in anotherItem.liitoskohdat:
                            if vastakohta.isFree():
                                if liitoskohta.collidesWithItem(vastakohta,0x1):
                                    dxy = liitoskohta.scenePos()-vastakohta.scenePos()
                                    vastakierto = vastakohta.suunta + 180 - liitoskohta.suunta
                                    
                                    
                                    currentItem.parentItem().pyorita(vastakierto)
                                    currentItem.setPos(currentItem.scenePos()-dxy)
                                    
                                    self.view().liitosOk = True
                                    if not liitoskohta in self.view().tempLiitokset:
                                        self.view().tempLiitokset.append(liitoskohta)
                                    if not vastakohta in self.view().tempVastineet:
                                        self.view().tempVastineet.append(vastakohta)