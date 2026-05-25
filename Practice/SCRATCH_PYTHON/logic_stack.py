def A():
    B()

def B():
    C()

def C():
    print("Done")

A()



"""
Stack:
A()
B()
C()


After finish:
C removed
B removed
A removed

"""