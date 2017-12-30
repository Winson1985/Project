# Functions definitions

import math

# Damping converter 20170720
def LogDamp2DampRatio(dec):
    return dec / math.sqrt(math.pow(2.0*math.pi, 2) + math.pow(dec, 2))

def DampRatio2LogDamp(dr):
    return 2.0*math.pi*dr / math.sqrt(1.0-math.pow(dr, 2))