"""
💎 Exercise-1: Memoized Fibonacci
Implement a memoized version of the Fibonacci sequence. The function "memoized_fibonacci(n: int) -> int" should return the nth number in the Fibonacci sequence, and it should use a cache to improve performance on subsequent calls.

Example:
memoized_fibonacci(10) -> 55
"""
"0 1 1 2 3 5 8 13 21 34 55 89 144 243"
def memoized_fibonacci(n) -> int:
    # pass 
    some_dict = {}
    def wrapper(ans):
        if ans in some_dict: 
            return some_dict[ans]
        else:
            some_dict[ans] = n(ans)
            return some_dict[ans]
            
    return wrapper

@memoized_fibonacci

def fib_by_mem(var):
    x = 0
    y = 1
    for i in range(var):
        x, y = y, x + y
    return x

# print(fib_by_mem(190000))
# print()
# print(fib_by_mem(190000))
# print()
# print(fib_by_mem(190000))

"""
💎 Exercise-2: Currying Function
Write a function "curry(func, *args)" that implements currying. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = curry(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def curry(func, *args):
    # pass 
    def wrapper(some_arg):
        return func(some_arg, *args)
    return wrapper

# def add_three_numbers(a, b, c):
#     return a + b + c
# add_five_and_six = curry(add_three_numbers, 5, 6)
# print(add_five_and_six(7))



"""
💎 Exercise-3: Implement zip() using map() and lambda
Write a function "my_zip(*iterables)" that takes in multiple iterables and returns an iterator that aggregates elements from each of the iterables.

Example:
my_zip([1, 2, 3], [4, 5, 6]) -> [(1, 4), (2, 5), (3, 6)]
"""

def my_zip(*iterables):
    # pass 
    return list(map(lambda *args: (args), *iterables))
# print(my_zip([1, 2, 3], [4, 5, 6], [1, 2, 232], [23, 232, 32]))
"""
💎 Exercise-4: Caching Decorator
Write a decorator "caching_decorator(func)" that caches the results of the function it decorates.

Example:
@caching_decorator
def expensive_function(x, y):
    # Simulate an expensive function by sleeping
    import time
    time.sleep(5)
    return x + y
"""

def caching_decorator(func):
    def wrapper(*args):
        import time
        time.sleep(5)
        return func(*args)
    return wrapper

@caching_decorator

def some_func(*args):
    return sum(args)

# print(some_func(1, 2, 3, 4))

"""
💎 Exercise-5: Recursive Flattening
Write a function "recursive_flatten(input_list: list) -> list" that takes a nested list and flattens it.

Example:
recursive_flatten([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]
"""

def recursive_flatten(input_list: list) -> list:
    list_ans = []
    def some_rec(input_list):
        for i in input_list:
            int_type = type(1)
            if type(i) == int_type:
                list_ans.append(i)
            else:
                some_rec(i)
    some_rec(input_list)
    return list_ans

# print(recursive_flatten([[[1, [2, [3, 4], 5]], 1, 2, 3], 1, 1232, 2321]))
           
# x = type(17)
# y = type(19)
# print(x)
# print(y)
# print(type(x))
# print(x == y)
"""
💎 Exercise-6: Decorator for Checking Function Arguments
Write a decorator "check_args(*arg_types)" that checks the types of the arguments passed to the function it decorates.

Example:
@check_args(int, int)
def add(a, b):
    return a + b
"""

def check_args(*arg_types):
    def outer(func):
        def wrapper(*args):
            flag = True
            cnt = 0
            for i in arg_types:
                if type(i()) != type(args[cnt]):
                    flag = False
                    yield f"Wrong data in {args[cnt]}"
                cnt += 1
            if flag:
                yield "Successfully all of our data have been wrote"
        return wrapper
    return outer

@check_args(int, int, str, int)

def add(a, b, c, d):
    return a + b + c + d

# print(*(add(1, 2, "3", 4)))












# def check(x, y):
#     return type(y) == type(x())

# print(check(int, 12))