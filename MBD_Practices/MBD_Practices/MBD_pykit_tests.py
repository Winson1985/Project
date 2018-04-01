from mbd_lib import *

# Unit test
def unit_test0():
    print("unit_test0:")
    # Method 1
    v0 = ColVector([0.5,-1.2,3.1])
    A1 = RotQuatern(np.radians(90.0),ey).RotMat
    A2 = RotQuatern(np.radians(90.0),ez).RotMat
    method1 = A2 * A1 * v0

    # Method 2
    A10 = RotQuatern(np.radians(90.0),ey).RotMat
    A21 = RotQuatern(np.radians(-90.0),ex).RotMat
    method2 = A10 * A21 * v0

    if np.max(method2 - method1) >= 1e-5:
        return False
    else:
        return True

# Unit test for operator * over loaded
def unit_test1():
    print("unit_test1:")
    v0 = ColVector([0.5,-1.2,3.1])
    # Method 1
    A10 = RotQuatern(np.radians(90.0),ey).RotMat
    A21 = RotQuatern(np.radians(-90.0),ex).RotMat
    method1 = A10 * A21 * v0

    # Mehod 2
    method2 = RotQuatern(np.radians(90.0),ey) * RotQuatern(np.radians(-90.0),ex) * v0

    if np.max(method2 - method1) >= 1e-5:
        return False
    else:
        return True

# Unit test for getting iterable items
def unit_test2():
    print("unit_test2:")
    a01 = RotQuatern(np.radians(90.0),ey)

    if a01[0,1] == RotQuatern(np.radians(90.0),ey).RotMat[0,1]:
        return True
    else:
        return False

def unit_test3():
    print("unit_test3:")
    a01 = RotQuatern(np.radians(90.0),ey)
    a02 = RotQuatern(np.radians(-90.0),ex)
    a03 = RotQuatern(np.radians(90.0),ez)
    a = a01.RotMat * a02.RotMat * a03.RotMat
    b = a01 * a02 * a03
    if a.all() == b.all():
        return True
    else:
        return False

# Unit tests
print(unit_test0())

print(unit_test1())

print(unit_test2())

print(unit_test3())