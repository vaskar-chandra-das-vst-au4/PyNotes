class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def show_details(self):
        print(f"Name = {self.name} , Age = {self.age} , Occupation = {self.occupation}")


class Developer(Person):
    def __init__(self, name, age, occupation, role, experience):
        super().__init__(name, age, occupation)
        self.role = role
        self.experience = experience

    def my_details(self):
        print("Hello developer!")
        print("Below are your details")
        print(
            f"Name = {self.name} , Age = {self.age} , Occupation = {self.occupation} , role = {self.role} , experience = {self.experience}"
        )


person1 = Person("Mamata", 20, "Student")
person1.show_details()

developer1 = Developer("Vaskar", 25, "Student", "React-Developer", 0)
developer1.my_details()

# print(dict(developer1)) # this will not work
print(developer1.__dict__)
