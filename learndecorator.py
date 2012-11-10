# a decorator, is just a function waiting a function as argument...
def new_decorator(function_to_decorate):
    # where everything is done
    def wrapper():
        # what do you want to do before executing function_to_decorate
        print "before execution"
        # call your function
        function_to_decorate()
        # something else to do? after execution of function_to_decorate
        print "after execution"

    # ... and returning another function,
    # containing your initial function, with some code to execute before and after
    return wrapper

# imagine you don't want to  modify this function
def untouchable_function():
    print "I am untouchable, you should not modify me"

# the infamous main function
def main():
    # call the untouchable function
    untouchable_function()

    # now, "decorate" the untouchable function, store it inside a variable
    decorated_untouchable_function = new_decorator(untouchable_function)

    # with python, you can store a function inside a variable, and call it like this:
    decorated_untouchable_function() 

if __name__ == '__main__':
    main()
