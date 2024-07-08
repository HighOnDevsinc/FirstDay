''' diamond problem '''


class A:
    pass


class B(A):
    def flower(self):
        return "this is flower B"


class C(A):
    pass


class D(B, C):
    pass


d = D()
print(d.flower())
print(D.__mro__)
