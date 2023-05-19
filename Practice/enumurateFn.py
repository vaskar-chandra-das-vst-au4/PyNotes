import math


def welcome():
    print("Hello I am module")
    names = ["Vaskar", "Mamata", "Keshab", "Basanti"]
    print(dict(enumerate(names, start=4)))

    for index, name in enumerate(names, start=1):
        print(f"{index} : {name}")


if __name__ == "__main__":
    welcome()


print(*dir(math), sep="\n")
print(len(dir(math)))
