# the __metaclass__ attribute
# will be used to create the class, otherwise, type will be used

def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    return a class object with the list of its attribute turned into uppercase
    """
    
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    upper_case_attr = dict((name.upper(), value) for name, value in attrs)
    # let `type` do the class creation
    return type(future_class_name, future_class_parents, upper_case_attr)

__metaclass__ = upper_attr # all the classes inside this module, will be created with upper_attr 

class Foo():
    bar = 'bip'
