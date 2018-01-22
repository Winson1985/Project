
# Gets output file name
filename = ""
#filename = input("Input enFAST output file:\n")
filename = "EN30_LM120_90HH.out"

# Save data into data struct
from PlotIO import *
data = OutputData(filename)

# Output data as Gunplot files
si = True
data.plot_channels(si)



import os
