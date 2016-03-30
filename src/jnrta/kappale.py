'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *

class Ratakappale:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.keskikohta = [0,0]
        self.kierto = 0
        self.alue = None
        self.sijainti = [0,0]
        self.tyyppi = 0           #{0:'None', 1:'Stopperi', 2:'Suora' ...}
        self.liitoskohdat = []
        self.naapurikappaleet = []