def hello_decorator(func):

    def inner1():
        print('before')
        func()
        print('after')

    return inner1

@hello_decorator
def function_to_be_used():
    print('initial function')

function_to_be_used()


