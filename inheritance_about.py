class One(object):
    def __init__(self, one:int):
        print( f"One.__init__.{one}")

class Two(One):
    def __init__(self, two:int):
        print(f"Two.__init__.{two}")

class Three(One):
    def __init__(self, three:int):
        print(f"Three.__init__.{three}")

class Four(Two, Three):
    def __init__(self, four:int):
        super(Four, self).__init__(3)
        super(Four, self).__init__(3)
        print(f"Four.__init__.{four}")



test = Four(4)

'''
MRO: Method Resolution Order
old vs new (yes it matters)
if base class A() -> old MRO is used
if base class A(object) -> new MRO is used
'''



class A:
    def who_am_i(self):
        print("I am a A")
    pass

class B(A):
    def who_am_i(self):
        print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")
    pass

class D(B,C):
    def who_am_i(self):
        print("I am a D")
    pass

# D is D
d1 = D()
d1.who_am_i()

#

class A:
    def who_am_i(self):
        print("I am a A")
    pass

class B(A):
    def who_am_i(self):
        print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")
    pass

class D(B,C):
    #def who_am_i(self):
    #   print("I am a D")
    pass


# D is B
d1 = D()
d1.who_am_i()


#

class A:
    def who_am_i(self):
        print("I am a A")
    pass

class B(A):
    #def who_am_i(self):
    #    print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")
    pass

class D(B,C):
    #def who_am_i(self):
    #   print("I am a D")
    pass

# D is C
d1 = D()
d1.who_am_i()

#

class A:
    def who_am_i(self):
        print("I am a A")
    pass

class B(A):
    #def who_am_i(self):
    #    print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")
    pass

class D(B,C):
    #def who_am_i(self):
    #   print("I am a D")
    pass

# D is A
d1 = D()
d1.who_am_i()

'''
model:
D
----------
|       |
B       C
|       |
A       A
old algorithm: depth first, left first
thus DBACA , shortened DBAC
new alorithm: old, but discard if parent 
A is parent of B
thus DBCA
'''
# each time a class is found in search poath, py asks is it a good head,
# if not py removes hte class form the final search path
# good head: no other class in the tail  of the search path which interits from it























