class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # @ acting as a additional constructor - it first manipulate the string and then call the main constructor using cls()
    @classmethod
    def fromStr(cls, inputStr):
        name = inputStr.split("-")[0]
        salary = int(inputStr.split("-")[1])
        return cls(name, salary)


t1 = Teacher("Rahul", 25000)
t2 = Teacher.fromStr("Prashant-30000")

print(t1.__dict__)
print(t2.__dict__)
