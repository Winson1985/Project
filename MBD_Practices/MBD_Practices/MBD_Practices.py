from mbd_lib import *

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

print(unit_test0())

print(unit_test1())