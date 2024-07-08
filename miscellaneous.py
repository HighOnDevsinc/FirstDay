from collections import namedtuple

''' decorators '''


def myOwnDecorator(fun):
    def wrapper():
        print("start of function")
        fun()
        print("end of function")
    return wrapper


@myOwnDecorator
def program() -> None:
    print("middle of function")


a = program()


''' named tuples '''


Point = namedtuple("coordinates", ["x", "y"])
s = Point(0, 0.5)
print(s.y)
