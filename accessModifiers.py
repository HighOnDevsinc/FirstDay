''' access modifiers '''


class Test:
    def __init__(self, a) -> None:
        self.__name = a

    def _test(self):
        pass


t = Test("Waleed")
# print(t.__name)
print(t._test())


''' getters setters '''


class GetterSetters:
    def __init__(self, a) -> None:
        self.__name = a

    def _test(self):
        pass

    @property
    def name(self):
        return self.__name + " Bin Osama"

    @name.setter
    def name(self, a):
        self.__name = a


gs = GetterSetters("Waleed")
print(gs.name)
gs.name = "Subhan"
print(gs.name)
