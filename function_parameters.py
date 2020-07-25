'''
:param is the variable in the declaration of the function
:arg is the value of :param
'''



''' variable length args'''
def foo(f_arg, *args):
    print ("first arg: ", f_arg)
    for _ in args:
        print("further arg: ", _)


foo('one', 'two', 'three')


# TODO *args is positional .. i.e. with a= ??


def foo2(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s is %s" % (key, value))


foo2(a= 'a' , b = 'b')


def foo3(first_arg, second_arg, *args, **kwargs):

    print('first_arg', first_arg)
    print('second_arg', second_arg)
    print('*args', args)
    print('**kwargs', kwargs)






foo3('a', 'b' , 'c', 'd',  e='e', f='f')

