
'''The module is used to demo'''

class Display():
    def __init__(self, str):
        self.string = str

    def display(self):
        '''To display the inputted string'''
        print(self.string)

class Gun01():
    def __init__(self):
        print("Gun01 installed")

    def fire(self):
        print("Fire!")

class SuperDisplay(Display):
    def __init__(self, str):
        Display.__init__(self, str)
        self.weapon = Gun01()


    def display(self):
        print ("Derived class:" + self.string)

