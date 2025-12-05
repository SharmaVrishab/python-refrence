class Basic:
    test_var = 5

    def __init__(self, a=1, b=2, c=3) -> None:
        self.a = a
        self.b = b
        self.c = c

    def add_all(self):
        return self.a + self.b + self.c

    @staticmethod
    def say_hello(name):
        print(f"say hello {name}")

    #  use can be ie for creating alternate constructor
    @classmethod
    def from_dict(cls, arg_dict):
        return cls(**arg_dict)

    @property
    def rando(self):
        import random

        """
        python object stores its attribute in __dict__
        """
        key = random.choice(list(self.__dict__.keys()))
        return key, self.__dict__[key]


b_inst = Basic(a=10, b=11, c=12)

print(f"{Basic}")
print(f"{b_inst}")
print(f"{b_inst.test_var}")

print(f"{b_inst.a}")
print(f"{b_inst.b}")
print(f"{b_inst.c}")

#  giving issue bcz we are changing the data typew
b_inst.test_var = "dwankdknwd"

print(b_inst.test_var)


b_inst.say_hello("oink")


alt_inst = Basic.from_dict({"a": 1, "b": 2, "c": 3})

print(alt_inst.add_all())

# after making it a property i dont neeed to call it like a function
#  i call like a attribute
print(alt_inst.rando)
