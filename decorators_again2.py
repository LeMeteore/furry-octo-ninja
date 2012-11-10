# what's if you want to pass args to the decorator itself?
def decorator_creator(param1):
    def my_decorator(func):
        def wrapper():
            print "-- before call, decorator parameters: ", param1
            print "now, give the param %s to the decorated function"%param1
            func(param1)
            print "-- after call --"
        return wrapper
    return my_decorator

#decorate
@decorator_creator("lemeteore")
#function to decorate
def function_to_decorate(arg1):
    print "I should have received a param from my decorator: ", arg1

#infamous
def main():
    #call the function already decorated above
    function_to_decorate()

if __name__ == "__main__":
    main()


