# # ! "Dunder" is a short form for "double underscore". In Python, dunder methods are also called "magic methods" or "special methods". These methods are identified by double underscores on both sides of the method name, such as __init__ or __len__.

#! Dunder methods provide a way to define behavior for built-in Python operations, such as object creation, object comparison, object representation, and more.
# @ Dunder methods are called implicitly when certain operations are performed on objects of a class. For example, when an object is compared using the == operator, Python looks for the __eq__ method to determine how the comparison should be done.

#! Here are some examples of dunder methods and their purposes:
# all the respective result need to be retuned from them
# ~ __init__(self, args...): This method is called when an object of a class is created. It initializes the object's attributes and sets its initial state.

# ~ __str__(self): This method is called when an object needs to be converted to a string. It should return a string that represents the object.

# ~ __len__(self): This method is called when the built-in len() function is called on an object. It should return the number of items in the object.

# ~ __eq__(self, other): This method is called when two objects need to be compared using the == operator. It should return True if the objects are equal, and False otherwise.

# ~ __lt__(self, other): This method is called when two objects need to be compared using the < operator. It should return True if the object is less than the other object, and False otherwise.

# ~ __add__(self, other): This method is called when two objects need to be added using the + operator. It should return a new object that represents the sum of the two objects.

# ~ __new__() method :Languages such as Java and C# use the new operator to create a new instance of a class. In Python the __new__() magic method is implicitly called before the __init__() method. The __new__() method returns a new object, which is then initialized by __init__().

# ~ __call__() : method enables Python programmers to write classes where the instances behave like functions and can be called like a function. When the instance is called as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...). object() is shorthand for object.__call__()

# ~ __repr__() : is one of the magic method that returns a printable representation of an object in Python that can be customized or predefined, i.e. we can also create the string representation of the object according to our need.
# Python __repr__() magic method Syntax:
# Syntax: object.__repr__()
# object: The object whose printable representation is to be returned.
# Return: Simple string representation of the passed object.
# @ __repr__ vs __str__ :  __repr__() magic method returns a printable representation of the object. The __str__() magic method returns the string representation which is more user-friendly i.e. easy to understand, whereas __repr__() representation contains information about the object so that it can be reconstructed.

# @ Dunder methods can be very powerful and allow for a lot of flexibility in defining how objects behave in Python. However, it's important to use them judiciously and with care, as they can also make code more difficult to understand and maintain.


class Employee:
    def __init__(self, name, code):
        self.name = name
        self.code = code


e1 = Employee("Vaskar", 25)
