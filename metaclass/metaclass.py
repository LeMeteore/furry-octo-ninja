#! /usr/bin/python

# a class is just a piece of code that produce an object

class ObjectCreator(object):
    """creates in memory, an object named ObjectCreator"""
    pass

# this object (the class) is also capable of creating objects (instances), this is why it is a class
my_object = ObjectCreator()
print my_object

# classes are objects, you can assign it to a variable
ObjectCreatorMirror = ObjectCreator

# you can print a class
print ObjectCreator

def echo(o): print o

# you can pass a class as a parameter
echo(ObjectCreator)

# you can add attributes to a class
ObjectCreator.new_attribute = 'foo'
print hasattr(ObjectCreator, 'new_attribute')

# you can create class on the fly
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return bar

# creates a class named foo, do assign it to MyClass variable
MyClass = choose_class('foo')

# the function returns a class, not an instance
print MyClass

# you can create an object: instanciate an object of class foo
print MyClass()

# do you remember the function type?
print type(1)
print type(ObjectCreator)

# type can take description of class as parameters and return a class
MyShinyClass = type('MyShinyClass', (), {})
print MyShinyClass
print MyShinyClass()

# this one: 
class FooBaz(object):
    foobaz = True

# can be translated to this one
FooBaz = type('FooBaz', (), {'foobaz' = True})

# you can inherit from it
FooBazChild = type('FooBazChild', (FooBaz,), {})
print FooBazChild.foobaz

# add methods to class
def echo_bar(self): prit self.bar
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

hasattr(Foo, 'echo_bar')
hasattr(FooChild, 'echo_bar')

# everythng is an object in python
class Bar(object): pass
b = Bar()
b.__class__

# class of any class ???
b.__class__.__class__

