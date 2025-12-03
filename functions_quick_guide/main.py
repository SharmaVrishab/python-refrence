#  working with funtions in python


def hello_world():
    print("Hello, World!")


hello_world()


def return_hello():
    return "Hello, World!"


message = return_hello()
print(message)


def greet(name):
    return f"Hello, {name}!"


personal_greeting = greet("Alice")
print(personal_greeting)


def multiuply(a, b=5):
    return a * b


multiplication_result = multiuply(4)
print(multiplication_result)
multiplication_result_with_b = multiuply(4, 3)
print(multiplication_result_with_b)


def first_last_word(word):
    """
    return first and last character of the word
    :param word: str
    :return: tuple(first_char, last_char)
    """
    return word[0], word[-1]


first_last_word_result = first_last_word("Python")
print(first_last_word_result)


# INTERMEDIATE LEVEL


def add_all(*args):
    """
    *args : packs all positional arguments into a tuple.
    Return the sum of all arguments.
    :param args: ints
    :return: int
    """
    total = 0
    for num in args:
        total += num
    return total


sum_result = add_all(1, 2, 3, 4, 5)
print(sum_result)


# passing like tuple directly
numbers = (10, 20, 30)
sum_result_with_tuple = add_all(*numbers)
print(sum_result_with_tuple)


def print_kwargs(**kwargs):
    """
    **kwargs: packs keyword arguments into a dictionary.
    Print all keyword arguments.w
    :param kwargs: key-value pairs
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=30, city="New York")


def print_all(*args, **kwargs):
    """
    Combines *args and **kwargs to print all positional and keyword arguments.
    :param args: positional arguments
    :param kwargs: keyword arguments
    """
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_all(1, 2, 3, name="Alice", age=30)


#  passing functions as arguments


def apply_function(func, *args, **kwargs):
    """
    Apply a given function to a value.
    :param func: function
    :param value: any
    :return: result of func(value)
    """
    return func(*args, **kwargs)


result = apply_function(print_all, 6, 7, 8, city="Los Angeles", country="USA")
print(result)


#  advanced level

"""
function allow you to be very specific in your api design by enforcing how arguments should be passed.

Symbol	Meaning	Affects
/	positional-only	everything before it
*	keyword-only	everything after it

"""


def func_with_keyword_only_args(a, b, *, c, d):
    """
    Everything after the * must be passed as keyword arguments only.

    a and b are positional or keyword arguments.
    c and d are keyword-only arguments.
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :return: sum of all arguments
    """
    return a + b + c + d


result_keyword_only = func_with_keyword_only_args(1, 2, c=3, d=4)
print(result_keyword_only)


def func_with_positional_only_args(a, b, /, c, d):
    """
    “All parameters before the / can ONLY be passed positionally, never by keyword.”
    a and b are positional-only arguments.
    c and d can be positional or keyword arguments.
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :return: sum of all arguments
    """
    return a + b + c + d


result_positional_only = func_with_positional_only_args(1, 2, c=3, d=4)
print(result_positional_only)
