






'''CLASS METHOD
Annotation that makes method reference class ('cls') instead of instance ('self').
Can be use to create alternative constructors, e.g. for different input formats.
'''
class Foo:
    def __init__(self, number :int ):
        self.bar=number

    @classmethod
    def from_string(cls, string : str):
        cls.bar = int(string)


_= Foo(1)               # default constructor
_= Foo.from_string('1') # alternative constructor


'''STATIC METHOD
Annotaton that makes method reference noting.
If you do not reference 'self' in method, make it static '''
class Foo2:
    def __init__(self):
        pass

    @staticmethod
    def bar(number :int):
        pass



'''PROPERTY ANNOTATION
 Bar1
    using property(self, fget, fset, fdel, doc)
        fset, fdel, doc are optional
 Bar2
    doing the same with annotations(also called decorators)
    notice same name for getter @property and setter @foo.setter
    this probably means you can use
        foo = 3 to invoke @foo.setter
        and 
        qux = foo to invoke @property
'''

class Bar1:
    def __init__(self, foo = 0):
        self.foo = foo

    def get_foo(self):
        return self._foo

    def set_foo(self, value):
        self._foo = value

    foo = property(get_foo,set_foo)


class Bar2:
    def __init__(self, foo = 0):
        self._foo = foo


    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value







