# Various object-oriented languages like C++, Java, Python control access modifications which are used to restrict access to the variables and methods of the class. Most programming languages has three forms of access modifiers, which are Public, Protected and Private in a class.

# Python uses ‘_’ symbol to determine the access control for a specific data member or a member function of a class. Access specifiers in Python have an important role to play in securing data from unauthorized access and in preventing it from being exploited.
# A Class in Python has three types of access modifiers:
# Public Access Modifier - it is by default , all the properties which are declare in init fn using self.property name
# Private Access Modifier - using __ double underscore , before property name
# Protected Access Modifier - using single underscore before property name


# #! Protected
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age


# p1 = Person("Vaskar", 25)
# # print(p1.name) # not exist

# print(p1._name)  # can be access like this
# print(p1.get_name())


#! Private
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


p1 = Person("Vaskar", 25)
# print(p1.__age) # cannot access like this directly
print(p1._Person__age)
