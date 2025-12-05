# had to start this bcz it is used in generator quick guide


nums = [1, 2, 3]

# for n in nums:
#     print(n)
# print(dir(nums))

# what can we what is iterabale
#  the function should have __iter__ method that return an iterator


# iterator is an object with a state so that it remembers where it is during iteration
#  and it has a __next__ method that return the next value when called and raise StopIteration when there is no more value to return


# so in a list there is no __next__ method but it has __iter__ method that return an iterator object  so the list itself cant return the next value but the iterator object returned by the __iter__ method can return the next value using its __next__ method


i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))


#  creating our own iterable and iterator


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # Signal that iteration is complete

        value = self.current
        self.current += 1
        return value


# Usage
counter = Counter(1, 5)
for num in counter:
    print(num)  # Prints 1, 2, 3, 4, 5
