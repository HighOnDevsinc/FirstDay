''' object orientd methods of different types '''


class objectOrientedMethods():
    def __init__(self, a, b) -> None:
        self.name = a
        self.number = b

    def __repr__(self) -> str:
        return (f"Methods({self.name, self.number})")

    @classmethod
    def classMethod(cls):
        return cls("Waleed", 123)


# calling from class


print(objectOrientedMethods.classMethod())


# calling from object


obj = objectOrientedMethods("hello", 321)
print(obj)
print(obj.classMethod())

del obj
