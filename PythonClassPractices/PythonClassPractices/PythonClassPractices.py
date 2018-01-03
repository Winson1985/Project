# The code is for the Python class practces
# Issued by Yongxing 2018/01/03
# Last modified 2018/01/03

import sys
sys.path.append('C:\\Users\\qiuyo\\Documents\\Projects\\Codes\\Project\\ \
                 Project\\PythonClassPractices\\PythonClassPractices')

from classes import *

geodata = GeoData()
geodata.diameter = 2.1
geodata.height = 7.8

twr = Tower(geodata, density = 0.22)

twr_volume = twr.volume_calc()
twr_mass = twr.mass_calc()
print("Tower volume:")
print(twr_volume)
print("Tower mass:")
print(twr_mass)

