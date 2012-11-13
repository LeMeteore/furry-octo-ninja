def benchmark(func):
    """
    decorator which print time execution of function
    """
    import time
    def wrapper(*args, **kwargs):
        #time before
        t = time.clock()
        #execute and store result
        res = func(*args, **kwargs)
        # print time delta
        print func.__name__, time.clock()-t
        # return result waited
        return res
    return wrapper
 
def logging(func):
    """
    decorator which prints activity script
    """
    def wrapper(*args, **kwargs):
        # execute function
        res = func(*args, **kwargs)
        # print some informations
        print func.__name__, args, kwargs
        # return result
        return res
    return wrapper
 
def counter(func):
    """
    a counter which counts and prints the number of time a function was called
    """
    def wrapper(*args, **kwargs):
        # inc counter
        wrapper.count = wrapper.count + 1
        # execute function
        res = func(*args, **kwargs)
        # print 
        print "{0} was called {1} times".format(func.__name__, wrapper.count)
        # return result
        return res
    # reset counter
    wrapper.count = 0
    return wrapper
 
@counter
@benchmark
@logging
def reverse_string(string):
    return string[::-1]
 
def main():
    print reverse_string("Karine alla en Irak")
    print reverse_string("Sa nana snob porte de trop bons ananas")

if __name__ == "__main__":
    main()
