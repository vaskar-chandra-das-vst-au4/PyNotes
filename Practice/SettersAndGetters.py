# # ! Basic setters and getters
# class Person:
#     def __init__(self, name, age, occupation):
#         self._name = name
#         self._age = age
#         self._occupation = occupation

#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age

#     def get_occupation(self):
#         return self._occupation

#     def set_name(self, name):
#         self._name = name


# vaskar = Person("Vaskar", 25, "Developer")
# print(vaskar.get_name())
# print(vaskar.get_age())
# print(vaskar.get_occupation())
# print(vaskar.set_name("Vaskar Chandra Das"))
# print(vaskar.get_name())


# # ! using python property
# class Javatpoint:
#     def __init__(self):
#         self._age = 0

#     # using the get function
#     def get_age(self):
#         print("getter method")
#         return self._age

#     # using the set function
#     def set_age(self, y):
#         print("setter method")
#         self._age = y

#     # using the del function
#     def del_age(self):
#         del self._age

#     age = property(get_age, set_age, del_age)


# John = Javatpoint()

# John.age = 18
# print(John.age)
# del John.age
# print(John.age)

# ! using python @property decorators


class Person:
    # def __init__(self, name:str, age: int):
    # def __init__(self, name, age: int):
    #     assert isinstance(name, str), f"{name} must be a string!"
    #     assert age > 18, "Age must be greater than 18"
    #     self._name = name
    #     self._age = age
    # ! OR
    def __init__(self, name, age):
        try:
            if isinstance(name, str):
                self._name = name
            else:
                raise ValueError("Name must be a string")

            if isinstance(age, int) and age > 18:
                self._age = age
            else:
                raise ValueError("Age must be an integer which is greater than 18")
        except ValueError as error:
            print(error)

    @property
    def name(self):
        print("I am a getter method")
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 18:
            self._age = age
        else:
            raise ValueError("Enter a age greater than 18!")


# vaskar = Person(12, 16)
# vaskar = Person("Vaskar", 16)
vaskar = Person("Vaskar", 25)

# # vaskar.age = 30
# print(vaskar.age)
print(vaskar.name)
