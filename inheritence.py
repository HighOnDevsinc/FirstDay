''' object oriented programming '''


class parent():
    def __init__(self, a, b) -> None:
        self.name = a
        self.blood = b

    def displayParent(self) -> None:
        return f"The parents name is {self.name} and their blood is " \
            f"{self.blood}"


class child(parent):
    def __init__(self, a, b, c) -> None:
        super().__init__(a, b)
        self.education = c

    def displayParent(self):
        return f"{super().displayParent()}, and education as {self.education}"


obj1 = child("Waleed", "B+", "Bachelors")
obj1.displayParent()
