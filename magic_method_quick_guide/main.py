class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.family = None
        self.cousins = []

    def __repr__(self):
        fam_name = ""
        if self.family:
            fam_name = f"{self.family.name}"
        return f"{self.name} {fam_name} - {self.age}"


class Family:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __repr__(self):
        return "\n".join(str(x) for x in self.members)


jake = Person(name="jake", age=12)
amanda = Person(name="Amanda", age=29)
kiara = Person(name="Kiara", age=13)

my_family = Family(name="Callahan")

print(jake)
print(amanda)
print(kiara)
print(my_family)
