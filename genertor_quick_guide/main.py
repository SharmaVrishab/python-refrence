"""
generator quick_guide.main.py
===========================
This module serves as the main entry point for the generator quick guide application.
"""

# import sys


# def make_list(stop):
#     result = []
#     for i in range(stop):
#         result.append(i)
#     return result


# test_list = make_list(10)
# print("Test List:", test_list)


# def genertor_list(stop):
#     for i in range(stop):
#         yield i**3


# test_generator = genertor_list(10)
# print("Test Generator:", list(test_generator))


# big_list = [x**3 for x in range(1_000_000)]
# big_generator = (x**3 for x in range(1_000_000))


# print(sys.getsizeof(big_list))
# print(sys.getsizeof(big_generator))


# def gen_Demo():
#     print("Start")
#     yield 1
#     print("Continue")
#     yield 2
#     print("End")
#     yield 3


# demo = gen_Demo()
# print(next(demo))
# print(next(demo))
# print(next(demo))
# print("-----")


# # Using a list comprehension
# import timeit

# # List comprehension
# list_time = timeit.timeit("[x**2 for x in range(10000)]", number=100)
# print("List comprehension time:", list_time)

# # Generator expression
# gen_time = timeit.timeit("sum(x**2 for x in range(10000))", number=100)
# print("Generator expression time:", gen_time)


#  generator simplest example


def my_gen():
    yield 1
    yield 2
    yield 3


g = my_gen()
print(next(g))  # Output: 1
print(next(g))  # Output: 2
print(next(g))  # Output: 3


# geneator using a loop
def my_gen_loop(end):
    for i in range(1, end):
        yield i


for num in my_gen_loop(4):
    print(num)  # Output: 1 2 3


def gen_list(stop):
    for i in range(stop):
        yield i**2
