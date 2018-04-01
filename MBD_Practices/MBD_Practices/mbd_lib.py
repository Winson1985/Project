# This lib is used to test equations and theory of MBD
# Issued by Yongxing.Qiu at March 21 2018
# Last modified by Yongxing.Qiu at April 1 2018

import numpy as np
import math as m

# Help functions to construct Matrix types
def ColVector(lst_obj):
    return np.transpose(np.mat(lst_obj))

def RowVector(lst_obj):
    return np.mat(lst_obj)

def GenMatrix(lst_obj):
    return np.mat(lst_obj)

# Axes vectors
ex = ColVector([1.0,0.0,0.0]) # ColVector
ey = ColVector([0.0,1.0,0.0]) # ColVector
ez = ColVector([0.0,0.0,1.0]) # ColVector

# RotQuaternBase class
class RotQuaternBase():
    def __init__(self):
        self.q = np.zeros(4)
        self.rmat = np.mat(np.zeros((3,3)))

    # Update rotation matrix
    # Ref. Dynamics of Multibody Sytems Shabana 4th p31
    def Update(self, a, d):
        theta2 = 0.5*a
        sin_theta2 = np.sin(theta2)
        q = np.zeros(4)
        q[0] = np.cos(theta2)
        q[1] = d[0,0]*sin_theta2
        q[2] = d[1,0]*sin_theta2
        q[3] = d[2,0]*sin_theta2
        self.q = q

        q01 = 2.0 * q[0] * q[1];
        q02 = 2.0 * q[0] * q[2];
        q03 = 2.0 * q[0] * q[3];
        q11 = 2.0 * q[1] * q[1];
        q12 = 2.0 * q[1] * q[2];
        q13 = 2.0 * q[1] * q[3];
        q22 = 2.0 * q[2] * q[2];
        q23 = 2.0 * q[2] * q[3];
        q33 = 2.0 * q[3] * q[3];

        # Calculate the 9 rotation matrix elements
        self.rmat[0,0] = 1.0 - q22 - q33;  # 1st column
        self.rmat[1,0] = q12 + q03;
        self.rmat[2,0] = q13 - q02;
        self.rmat[0,1] = q12 - q03;        # 2nd column
        self.rmat[1,1] = 1.0 - q11 - q33;
        self.rmat[2,1] = q23 + q01;
        self.rmat[0,2] = q13 + q02;        # 3rd column
        self.rmat[1,2] = q23 - q01;
        self.rmat[2,2] = 1.0 - q11 - q22;

# RotQuatern class
class RotQuatern(RotQuaternBase):
    def __init__(self, angle = 0.0, direct = ex,
                 RotMat = None ):
        super().__init__()
        self.angle = angle
        self.direct = direct
        # Returns RotMat from angle and direct
        if RotMat is None:
            self.Update(angle, direct)
            self.RotMat = self.rmat
        else:
            self.RotMat = RotMat

    # Operator *
    def __mul__(self, other):
        return self.RotMat * other.RotMat
    def __rmul__(self, other):
        return other * self.RotMat

    # Returns member of RotQuatern object
    def __getitem__(self, Id):
        return self.RotMat[Id[0], Id[1]]

