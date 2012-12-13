class UpperAttrMetaclass(type):
    # __new__ is called before __init__
    # you rarely use __new__, except when you want to control object creation
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name, value) for name, value in attrs)
        return super(UpperAttrMetaclass, upperattr_metaclass).__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = UpperAttrMetaclass

class Baz():
    baz = 'bazz'
