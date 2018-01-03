# Functions definitions

import math

def LogDamp2DampRatio(dec): 
    """This function converts Log damping to damping ratio"""
    return dec / math.sqrt(math.pow(2.0*math.pi, 2) + math.pow(dec, 2))

def DampRatio2LogDamp(dr):
    """This function converts damping ratio to Log damping"""
    return 2.0*math.pi*dr / math.sqrt(1.0-math.pow(dr, 2))