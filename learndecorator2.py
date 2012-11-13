# let's import our new_decorator
from learndecorator import new_decorator

#let's create another decorator
def another_nice_decorator(function_to_decorate):
    def wrapper():
        print "****"
        function_to_decorate()
        print "****"

    return wrapper

# this is the sexiest??? way to decorate a function,
@new_decorator
def another_untouchable_function():
    print "please, don't touch"

#notice: we can use more than one decorator
@another_nice_decorator
@new_decorator
def weird_untouchable_function():
    print "absolutely nothing to change here"

#infamous main function, let's see the output
def main():
    another_untouchable_function()
    weird_untouchable_function()


if __name__ == '__main__':
    main()
