x = "hello"


def funct0():
    def funct1():
        x = "test"
        print(x)

    global x
    x = "world"
    funct1()


print(x)
funct0()
print(x)
