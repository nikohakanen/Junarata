'''
Created on Apr 15, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
from jnrta.myview import *
from jnrta.myscene import *

class CentralWidget(QDialog):
    '''
    classdocs
    '''


    def __init__(self, parent, kappalelista):
        '''
        Constructor
        '''
        super(CentralWidget, self).__init__(parent)
        self.view = MyView(kappalelista)
        self.scene = MyScene(self)
        self.scene.setSceneRect(0,0,900,700)
        
        color = QColor(0, 110, 10)
        pen = QPen(QColor(0,0,0))
        brush = QBrush(color)
        
        self.view.setScene(self.scene)
        self.view.centerOn(QPointF(450,350))
