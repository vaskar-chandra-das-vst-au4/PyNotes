# Instance method performs a set of actions on the data/value provided by the instance variables. If we use instance variables inside a method, such methods are called instance methods.
##~ Bound to the object of a class ,
##~ it can modify a object state. ,
##~ can access and modify both class and instance variables.

# Class method is method that is called on the class itself, not on a specific object instance. Therefore, it belongs to a class level, and all class instances share a class method. -
##~ bound to the class ,
##~ it can modify a class state,
##~ can access only class variable , used to create factory methods

# Static method is a general utility method that performs a task in isolation. This method doesn’t have access to the instance and class variable. -
##~ bound to the class ,
##~ it cant modify a class or object ,
##~ cant access or modify the class and instance variables.

#! Difference #1: Primary Use
# Class method Used to access or modify the class state. It can modify the class state by changing the value of a class variable that would apply across all the class objects.

# The instance method acts on an object’s attributes. It can modify the object state by changing the value of instance variables.

# Static methods have limited use because they don’t have access to the attributes of an object (instance variables) and class attributes (class variables). However, they can be helpful in utility such as conversion form one type to another.

# Class methods are used as a factory method. Factory methods are those methods that return a class object for different use cases. For example, you need to do some pre-processing on the provided data before creating an object.

#! Difference #2: Method Defination
# Let’s learn how to define instance method, class method, and static method in a class. All three methods are defined in different ways.

# All three methods are defined inside a class, and it is pretty similar to defining a regular function.

# Any method we create in a class will automatically be created as an instance method. We must explicitly tell Python that it is a class method or static method.

# Use the @classmethod decorator or the classmethod() function to define the class method

# Use the @staticmethod decorator or the staticmethod() function to define a static method.
# Example:
# Use self as the first parameter in the instance method when defining it. The self parameter refers to the current object.

# On the other hand, Use cls as the first parameter in the class method when defining it. The cls refers to the class.

# A static method doesn’t take instance or class as a parameter because they don’t have access to the instance variables and class variables.


class Student:
    # class variables
    school_name = "ABC School"

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print(self.name, self.age, Student.school_name)

    # class method
    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    # static method
    @staticmethod
    def find_notes():
        return print("I am a static method")


#! Difference #3: Method Call
# Class methods and static methods can be called using ClassName or by using a class object.
# The Instance method can be called only using the object of the class.
# vaskar = Student("Vaskar Chandra Das", 25)
# vaskar.show()
# # Student.show() # not possible
# Student.school_name = "KV"
# print(Student.school_name)
# print(vaskar.school_name)
# print(dir(vaskar))
# print(hasattr(vaskar, "__dict__"))
# print(vaskar.__dict__)  # only show own properties


# ! Difference #4: Attribute Access
# Both class and object have attributes. Class attributes include class variables, and object attributes include instance variables.

# The instance method can access both class level and object attributes. Therefore, It can modify the object state.
# Class methods can only access class level attributes. Therefore, It can modify the class state.
# A static method doesn’t have access to the class attribute and instance attributes. Therefore, it cannot modify the class or object state.

#! Difference #5: Class Bound and Instance Bound
# An instance method is bound to the object, so we can access them using the object of the class.
# Class methods and static methods are bound to the class. So we should access them using the class name.
# print(*dir(vaskar), sep=" ")
# OR
# print(vaskar.__dir__())  # dunder methods/magic methods


# @ How to change class variable ? can we change it by calling it on object?
class Employee:
    company_name = "Apple"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"{self.name} of age {self.age} work at {self.company_name}")


e1 = Employee("Vaskar", 25)
e2 = Employee("Rohan", 30)
# e1.company_name = "Wipro" # like this we cant change class variable , actually this is creating new instance variable for e1
Employee.company_name = "WIPRO"  # this is how we can change class variable
print(e1.__dict__)
e1.show_details()
e2.show_details()
