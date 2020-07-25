

def foo():
    # the exception handler catches the thrown error.


    try:
        # thrown an ZeroDivisionError
        i = 1/0


        # would throw AssertionError if False
        assert True

    except FileNotFoundError as e:
        # because `except` does not match thrown error,
        # if there was no other exception handler the default `traceback` is issued instead.
        print(e)
    except ZeroDivisionError as e:
        # catches the ZeroDivisionError
        print(e)
        print('error')
    else:
        # what to do if no exception is raised
        print('no error')
    finally:
        # always do, might be used for cleanup
        # manually raise exception
        raise Exception



class One():

    def __init__(self):
        raise Exception





class Two(One):

    def __init__(self):
        try:
            super.__init__()
        except Exception as e:
            print("caught")








Two()
