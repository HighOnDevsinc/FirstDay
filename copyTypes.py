''' deep and shallow copy '''


import copy


class Copy:
    def __init__(self, a, b) -> None:
        self.model = a
        self.colors = b


c = Copy(2012, ["Red", "Yellow"])

deepCopy = copy.deepcopy(c)
deepCopy.colors.append("Green")
print("Original colors ", c.colors)
print("Deep copied colors", deepCopy.colors)

shallowCopy = copy.copy(c)
shallowCopy.colors.append("Green")
print("Original colors ", c.colors)
print("Shallow copied colors", shallowCopy.colors)
