from typing import Any


class get_all_attr:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)


class Utils:
    @classmethod
    def from_dict(cls, args_dict):
        return cls(**args_dict)


class CleanRepresenting(Utils):
    def __repr__(self) -> str:
        output = ""
        for key, value in self.__dict__.items():
            output += f"{key} : {value},  "

        return output


class ChildClass(get_all_attr, CleanRepresenting):
    pass


data = {"one": "1", "two": "2"}
# here instead of passing data in. parameter  directly i used ** to load the data from a dictionary
passing_multiple_value_undocumented = get_all_attr(**data)
# #  here am getting this error as i am setting the class attribute dynamiclaly during run time which in pylance is giving warning
print(passing_multiple_value_undocumented.one)


child_1 = ChildClass(**data)
child_2 = ChildClass.from_dict(data)
print(child_1)
