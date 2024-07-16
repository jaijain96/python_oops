x = "hello"


def funct0():
    def funct1():
        print(x)

    funct1()


print(x)
funct0()
print(x)
