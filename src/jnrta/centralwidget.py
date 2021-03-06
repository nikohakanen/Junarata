'''
Created on Apr 15, 2016

@author: hakanen1
'''
from PyQt4.QtGui import QDialog, CentralWidget
from myview import MyView
from myscene import MyScene

class CentralWidget(QDialog):
    '''
    QMainWindow luokan CentralWidget
    '''


    def __init__(self, parent, kappalelista):
        '''
        Constructor
        '''
        super(CentralWidget, self).__init__(parent)
        self.view = MyView(kappalelista)
        self.scene = MyScene(self)
        self.scene.setSceneRect(0,0,900,700)
        self.view.setScene(self.scene)
