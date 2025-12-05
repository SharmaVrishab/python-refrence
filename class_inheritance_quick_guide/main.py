class Nothing:
    pass


class LooseInit:
    # dynamic attribute assignment
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


class StrictInit(LooseInit):
    def __init__(self, **kwargs) -> None:
        sanitised_args = {
            key: value for key, value in kwargs.items() if not key.startswith("bad")
        }
        super().__init__(**sanitised_args)

    def print_cls(self):
        print("STRICT_INIT")


class Utils:
    @classmethod
    def from_dict(cls, arg_dict):
        return cls(**arg_dict)

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            # this remove private methods
            if not key.startswith("_")
        }


class BetterRepr(Utils):
    def __repr__(self):
        output = ""
        for key, value in self.to_dict().items():
            output += f"{key} : {value}, "
        return f"<{output[:-2]}>"

    def print_cls(self):
        print("BETTER_REPR")


class ChildClass(StrictInit, BetterRepr):
    pass


sister = ChildClass(name="oink1", age="10")
# below is used for example class StrictInit(LooseInit):
bad_sister = ChildClass(name="bad_oink1", age="10", bad_args="dwaklnawklnadwk")
brother = ChildClass(name="oink2", age="11")
cousin = ChildClass.from_dict({"name": "oink3", "age": 12})
print(f"{sister.name} is {sister.age} years old")  # type: ignore
print(f"{brother.name} is {brother.age} years old")  # type: ignore
print(f"{cousin.name} is {cousin.age} years old")  # type: ignore
print({f"{sister.to_dict()}"})


print(f"{bad_sister.name} is {bad_sister.age} years old")  # type: ignore


print(bad_sister)
bad_sister.new_value = ":wakndadwnawdklnkln"
print(bad_sister)


bad_sister.print_cls()
