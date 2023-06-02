"""
Exercise-1: First-class Function Operation
Write a function "operation(func, x: int, y: int) -> int" that takes in a function 'func' and two integers, 'x' and 'y'. Apply the function to the two numbers and return the result. 

Example:
def multiply(a, b):
    return a * b
operation(multiply, 5, 3) -> 15
"""

def operation(func, *args) -> int:
    # pass
    # return func(x, y)
    def dec(*args):
        c = 1
        for x in args:
            c *= x
        return c
    return dec

@operation
def multiply(a, b):
    return a * b

# print(multiply(3, 4))




"""
Exercise-2: Implement Map Function
Write a function "my_map(func, my_list: list) -> list" that mimics the built-in Python 'map' function. It should take a function and a list as input, applying the function to each element of the list.

Example:
my_map(lambda x: x**2, [1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

def my_map(func, *args) -> list:
    # pass
    def some_func(args):
        return list(map(func, args))
    
    return some_func

@my_map

def some_f(x):
    return x * x
    
# print(some_f(some_f, [1, 2, 3, 4]))
# print(some_f([1, 2, 3, 4]))

"""
Exercise-3: Lambda Function with Filter
Write a function "filter_even_numbers(numbers: list) -> list" that uses 'filter' and a lambda function to filter out all even numbers from the list.

Example:
filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]) -> [1, 3, 5, 7]
"""

def filter_even_numbers(numbers: list) -> list:
    # pass
    return list(filter(lambda x: not x % 2 == 0, numbers))


"""
Exercise-4: Recursive Factorial
Write a function "recursive_factorial(n: int) -> int" that calculates the factorial of a number recursively.

Example:
recursive_factorial(5) -> 120
"""

def recursive_factorial(n: int) -> int:
    # pass 
    if n == 1:
        return 1
    else:
        return recursive_factorial(n - 1) * n

# print(recursive_factorial(5))

"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""
import time

def timeit_decorator(func):
    # pass 
    
    x = time.time()
    # x = datetime.datetime.now()
    list_1 = func()
    # print("Our series:", list_1)
    # return datetime.datetime.now().second - x.second
    return time.time() - x

@timeit_decorator

def sample_func():
    return [i**2 for i in range(10000)]

# print(sample_func())

# print(sample_func)

# def func():
#     return("hello")

# print(func)
    


"""
Exercise-6: Function Composition
Write a function "compose(*funcs)" that takes a series of functions and returns a new function that composes them. The returned function should take an input and apply each function to the result of the previous function.

Example:
def double(x):
    return 2 * x
def square(x):
    return x ** 2
new_func = compose(double, square)
new_func(3) -> 36
"""

def compose(*funcs):
    # pass
    def some_f(arg):
        # return funcs[1](funcs[0](arg))
        for function in funcs:
            arg = function(arg)
        return arg

    
    return some_f

# @compose

def double(x):
    return 2 * x
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
new_func = compose(double, square, cube)
# print(new_func(2))


"""
Exercise-7: Partial Application
Write a function "partial(func, *args)" that implements partial application. 
The function should return a new function that when called will return the result of 
applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = partial(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def partial(func, *args):
    # pass 
    def some_func(*some_args):
        x = sum(some_args) + sum(args)

        return x
    return some_func

def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = partial(add_three_numbers, 5, 6)
# print(add_five_and_six(7))

"""
Exercise-8: Reduce to Compute Factorial
Write a function "factorial_reduce(n: int) -> int" that uses `reduce` to compute the factorial of an integer.

Example:
factorial_reduce(5) -> 120
"""
from functools import reduce
def factorial_reduce(n: int) -> int:
    # pass 
    return reduce(lambda x, y: x * y, list(range(1, n + 1)))

# print(factorial_reduce(5))
"""
Exercise-9: Function Memoization
Write a function "memoize(func)" that takes a function and returns a memoized version of the function. The memoized version should cache the results of the function so that the next time it's called with the same arguments, it returns the cached value instead of calculating the result again.

Example:
def expensive_function(x):
    return x ** x  # expensive calculation
memoized_function = memoize(expensive_function)
memoized_function(5)  # -> This will take some time to compute
memoized_function(5)  # -> This will return the cached result
"""

def memoize(func):
    dict_1 = {}

    def wrapper(x):
        if x not in dict_1:
            result = func(x)
            dict_1[x] = result
            return result
        else:
            return dict_1[x]
    return wrapper

@memoize

def memoized_function(x):
    return x ** x  # expensive calculation
# print(memoized_function(5)) # -> This will take some time to compute
# print(memoized_function(5))  # -> This will return the cached result

"""
Exercise-10: Custom Reduce Function
Implement your own version of Python's 'reduce' function "my_reduce(func, iterable, initializer=None)".

Example:
my_reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> 24
"""

def my_reduce(func, iterable, initializer=0):
    # pass
    for x in iterable:
        initializer = func(initializer, x)
    return initializer




# list_1 = [1, 2, 3, 4]
# print(my_reduce(lambda x, y: x + y, list_1))


"""
Exercise-11: Lambda Function Sort
Write a function "sort_by_last_letter(words: list) -> list" that sorts a list of words in ascending order based on the last letter of each word. Use a lambda function.

Example:
sort_by_last_letter(['apple', 'banana', 'cherry', 'date']) -> ['banana', 'apple', 'date', 'cherry']
"""

def sort_by_last_letter(words: list) -> list:
    # pass
    return list(sorted(words, key = lambda x : x[-1]))
# print(sort_by_last_letter(['apple', 'banana', 'cherry', 'date']))
"""
Exercise-12: Recursive List Reversal
Write a function "recursive_reverse(my_list: list) -> list" that reverses a list using recursion.

Example:
recursive_reverse([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def recursive_reverse(my_list: list) -> list:
    list_1 = []
    def some_rec(cnt):
        if cnt == -1:
            return
        else:
            list_1.append(my_list[cnt])
            cnt -= 1
            some_rec(cnt)
    some_rec(len(my_list) - 1)
    return list_1

# print(recursive_reverse([1, 2, 3, 4, 5]))

"""
Exercise-13: Decorator for Function Counting
Write a decorator function "count_calls(func)" that counts the number of times a function is called.

Example:
@count_calls
def test_function():
    return

test_function()
test_function()
# Output: 'test_function' was called 2 times.
"""

def count_calls(func):
    cnt = 1
    def wrapper(*args):
        nonlocal cnt
        print(f"Function called {cnt} times")
        cnt += 1
        return func(*args)
    return wrapper

@count_calls

def test_function(*args):
    return sum(args)

# print(test_function(1, 2, 3, 4, 5))
# print(test_function(10, 11))
# print(test_function(7, 7, 7))

"""
Exercise-14: Use reduce to Find the Maximum Number
Write a function "find_max(numbers: list) -> int" that uses reduce to find the maximum number in a list.

Example:
find_max([1, 2, 3, 4, 5]) -> 5
"""

def find_max(numbers: list) -> int:
    
    return reduce(lambda x, y: max(x, y), numbers)
# print(find_max([1, 2, 3, 4, 5]))
"""
Exercise-15: Use filter and lambda to Remove Elements
Write a function "remove_elements(my_list: list, element) -> list" that uses filter and a lambda function to remove all instances of a specific element from a list.

Example:
remove_elements([1, 2, 3, 2, 4, 2, 5], 2) -> [1, 3, 4, 5]
"""

def remove_elements(my_list: list, element):
    # pass 
    my_list = enumerate(my_list)
    return [x[1] for x in list(filter(lambda x: (x[0] + 1) % 2, my_list))]

# print(remove_elements([1, 2, 3, 2, 4, 2, 5], 2))
"""
Exercise-16: Higher-Order Function for Repeats
Write a function "repeat(n: int)" that returns a function. The returned function should take a string input and repeat it `n` times.

Example:
repeat_three_times = repeat(3)
repeat_three_times('hello') -> 'hellohellohello'
"""

def repeat(n: int):
    def wrapper(string):
        return n * string
    return wrapper
# repeat_three_times = repeat(3)
# print(repeat_three_times('hello'))


"""
Exercise-17: Recursive List Sum
Write a function "recursive_sum(my_list: list) -> int" that recursively computes the sum of a list of integers.

Example:
recursive_sum([1, 2, 3, 4, 5]) -> 15
"""

def recursive_sum(my_list: list) -> int:
    # pass
    sum_ = 0
    def some_rec(my_list, cnt):
        nonlocal sum_
        if cnt < 0:
            return
        else:
            sum_ += my_list[cnt]
            some_rec(my_list, cnt - 1)
    some_rec(my_list, len(my_list) - 1)
    return sum_

# print(recursive_sum([1, 2, 3, 4, 5]))          

"""
Exercise-18: Map with Multiple Lists
Write a function "add_two_lists(list1: list, list2: list) -> list" that uses `map` and `lambda` to add together corresponding elements of two lists.

Example:
add_two_lists([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
"""

def add_two_lists(list1: list, list2: list) -> list:
    # pass
    return list(map(lambda x, y: x + y, list1, list2))
    
# print(add_two_lists([1, 2, 3], [4, 5, 6]))
