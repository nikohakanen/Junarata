'''
Created on Mar 29, 2016

@author: hakanen1
'''
from PyQt4.QtGui import *
import math

class Ratakappale:
    '''
    classdocs
    '''

    def __init__(self, keskikohta, kierto, leveys, korkeus, sijainti, tyyppi):
        '''
        Constructor
        '''
        self.keskikohta = keskikohta
        self.kierto = kierto
        self.leveys = leveys
        self.korkeus = korkeus
        self.sijainti = sijainti    # esim. neliöllä vasen ylänurkka
        self.tyyppi = tyyppi       #{0:'None', 1:'Stopperi', 2:'Suora' ...}
        self.liitoskohdat = []
        self.naapurikappaleet = []
        
    def lisaaNaapuri(self, naapurikappale):
        self.naapurikappaleet.append(naapurikappale)
        
    def lisaaLiitos(self, liitoskohta):
        self.liitoskohdat.append(liitoskohta)
        
    def pyorita(self, kulma):
        self.kierto = kulma
        
class Stopperi(Ratakappale):
    '''
    classdocs
    '''
    def __init__(self, sijainti):
       
        super().__init__([sijainti[0]+10,sijainti[1]+10], 0, 20, 20, sijainti, 1)
        
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
        r = 100
        a = 20
        ang = 45
        ang_rad = math.radians(ang)
        arc_x = x + r + (r-a/2)*math.cos(ang_rad/2)
        arc_y = y + r - (r-a/2)*math.sin(ang_rad/2)
        
        super().__init__([arc_x,arc_y], 0, 200, 200, sijainti, 5)
    
    
    
    
    
    
    
    
    
    
    
    
        