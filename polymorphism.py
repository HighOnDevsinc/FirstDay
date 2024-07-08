''' polymorphism basics '''


class A:
    var = "class variable of A"

    def __init__(self) -> None:
        self.var = "instance variable 1 of A"
        self.instance = "instance variable 2 of A"


class B(A):
    var = "class variable of B"

    def __init__(self) -> None:
        self.var = "instance variable 1 of B"
        self.instance = "instance variable 2 of B"
        super().__init__()


b = B()
print(b.var, "\n")


''' monkey patching '''


class MonkeyPatch:
    def func1(self):
        return "This is func1"

    def monkey(self):
        return "This is monkey"


mp = MonkeyPatch()
print(mp.func1())
temp = mp.func1
mp.func1 = mp.monkey
print(mp.func1(), "\n")


''' operator overloading '''


class Employee:

    def __init__(self, sal) -> None:
        self.salary = sal

    def __add__(self, second):
        return self.salary + second.salary


emp1 = Employee(1200)
emp2 = Employee(2500)

print("The salary for both objects is ", emp1 + emp2, "\n")
