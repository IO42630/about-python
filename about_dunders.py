# flexible call to the class name
class A:
    pass


_=A.__class__.__name__





'''
main check, 
have code only execute when you want to run the module as a program
and not have it execute when someone just wants to import your module and call your functions themselves.
'''
if __name__ == '__main__':
    pass