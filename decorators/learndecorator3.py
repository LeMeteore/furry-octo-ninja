from functools import wraps

#let's define a useless decorator
def useless_decorator(func):
    # decorate the wrapper with wraps (wraps will copy all the informations concerning the function to decorate)
    @wraps(func)
    # if you want to pass args to the function to decorate, it's the wrapper who passes this args
    def wrapper(*args):
        # what args were passed? let's see them before executing the function
        print "** before call, this is args passed: ", args
        # call the function to decorate
        func(*args)
        # if you want to do some after ...
        print "++ after call ++"

    return wrapper

# decorate
@useless_decorator
def a_useless_function(a,b,c):
    """
        This is such a nice function
    """
    pass

def main():
    a_useless_function(1,2,3)
    

if __name__ == "__main__":
    main()
