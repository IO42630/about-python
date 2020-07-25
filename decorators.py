''''''


def helloplus(original_function):
    """ takes function as parameter """
    def new_function(*args, **kwargs):
        ''' see function_parameters.py for args explanation'''
        print('helloplus ' + args[0])
        original_function("inner world")
    # return executes new_function
    return new_function

@helloplus
def hello( string : str):
    print("hello "+string)


hello("world")







def foo_wrap(func):
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrapped_func



@foo_wrap
def bars(str):
    print(str)



bars('asdf')