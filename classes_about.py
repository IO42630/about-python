# OBJECTS

class BaseClass:
    """
    functions, data -[in class called]-> methods, attributes\n
    duck typing:\n
    check if object quacks like a duck and walks like a duck,\n
    rather than asking whether the object is a duck.
    """


    def __init__(self):
        """
        constructor with vars being passed.\n
        'self' is required, unlike in java.\n
        else error 'method takes 0 params but was given 1'\n
        this happens because method which was defined inside a class\n
        is given the parameter 'self' by default when being called.
        """
        self.name = None

    def set_name(self, name):
        # self is a reference to the class itself
        self.name = name

    def get_name(self):
        return self.name

    def get_type(self):
        return "BaseClass"


class DerivedClass(BaseClass):

    def __init__(self, name=None):
        """
        :param name: 'None' indicates param may be omitted (method overloading).
        """
        super(DerivedClass, self).__init__()

    def get_type(self):
        # Overwrites function in super.
        return "DerivedClass"


# polymorphism
def print_type(_):
    print('type is '+_.get_type())


base_class = BaseClass()
derived_class = DerivedClass()

print(base_class.get_name())
print(derived_class.get_name())
print_type(base_class)
print_type(derived_class)


class Employee:
    # competes class without having to write code
    pass


