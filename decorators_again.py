# what's if you want to create decorators on the fly? voodoo session yay
def decorator_creator():
    def my_decorator(func):
        def wrapper():
            print "-- before call --"
            func()
            print "-- after call --"
        return wrapper
    return my_decorator

# let's create a decorator, using the decorator_creator function
brand_new_decorator = decorator_creator()

#decorate
@brand_new_decorator
#function to decorate
def function_to_decorate():
    print "I should be decorated"

# we can go faster
@decorator_creator()
def other_function_to_decorate():
    print "Me too I should be decorated"

#infamous
def main():
    function_to_decorate()
    other_function_to_decorate()

if __name__ == "__main__":
    main()


