from typing import Union
class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


class C(A):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z


def factory(type: str) -> A:
    if type == "a":
        return B("x", "y")
    elif type == "b":
        return C("x", "z")
    else:
        raise Exception("ASD")


i: B = factory("a")
print(i.y)
