# The code is for the Python class practces
# Issued by Yongxing 2018/01/03
# Last modified 2018/01/03

'''The module saved some help classes'''

from math import *

class GeoData():
    '''The geometry data struct'''
    def __init__(self):
        self.height = 0.0
        self.diameter = 0.0

class CompBase():
    '''Base class of Component'''
    def __init__(self, geodata):
        self.geodata = geodata # geodata = GeoData()

    def volume_calc(self):
        '''Calculate volume'''
        return pow(self.geodata.diameter*0.5*pi, 2)*self.geodata.height

class Tower(CompBase):
    '''Tower componenet class'''
    def __init__(self, geodata, density):
        super().__init__(geodata) # geodata = GeoData()
        self.density = density

    def mass_calc(self):
        '''Returns Tower mass'''
        return self.volume_calc()*self.density
        






