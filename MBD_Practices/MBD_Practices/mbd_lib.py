# This lib is used to test equations and theory of MBD
# Issued by Yongxing.Qiu at March 21 2018
# Last modified by Yongxing.Qiu at March 22 2018

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
    def __init__(self, angle = 0.0, direct = ex, \
                 RotMat = np.mat(np.zeros((3,3))) ):
        super().__init__()
        self.angle = angle
        self.direct = direct
        self.RotMat = RotMat
        # Returns RotMat from angle and direct
        if self.RotMat.all() == 0.0:
            self.Update(angle, direct)

    # Returns RotMat
    def RotMatrix(self):
        if self.RotMat.all() != 0.0:
            return self.RotMat
        else:
            return self.rmat

    # Operator *
    def __mul__(self, other):
        return self.rmat * other.rmat

# Unit test
def unit_test0():
    # Method 1
    v0 = ColVector([0.5,-1.2,3.1])
    print('%s%s'% ("v0=",v0))
    A1 = RotQuatern(np.radians(90.0),ey).RotMatrix()
    A2 = RotQuatern(np.radians(90.0),ez).RotMatrix()
    method1 = A2 * A1 * v0

    # Method 2
    A10 = RotQuatern(np.radians(90.0),ey).RotMatrix()
    A21 = RotQuatern(np.radians(-90.0),ex).RotMatrix()
    method2 = A10 * A21 * v0

    if np.max(method2 - method1) >= 1e-5:
        return False
    else:
        return True

# Unit test for operator * over loaded
def unit_test1():
    v0 = ColVector([0.5,-1.2,3.1])
    print('%s%s'% ("v0=",v0))
    # Method 1
    A10 = RotQuatern(np.radians(90.0),ey).RotMatrix()
    A21 = RotQuatern(np.radians(-90.0),ex).RotMatrix()
    method1 = A10 * A21 * v0

    # Mehod 2
    method2 = RotQuatern(np.radians(90.0),ey) * RotQuatern(np.radians(-90.0),ex) * v0

    if np.max(method2 - method1) >= 1e-5:
        return False
    else:
        return True

