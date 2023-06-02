import functools

# functools.reduce()

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# closer = outer(10)

# print(closer(5))

# def outer():
#     x = 10
#     def inner():
#         # global x
#         nonlocal x
#         x = 11
#         print(x)
#     inner()
#     print(x)

# outer()




# def debug_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("function called: ", func.__name__)
#         print("arguments:", args, kwargs)
#         result = func(*args, **kwargs)
#         print("result", result)
#         return result
#     return wrapper

# @debug_decorator

# def add_nums(x, y):
#     return x + y

# add_nums(1, 2)

# def hey():
#     def jojo():
#         print("hello")
#     return jojo

# hey()



# x = int(input())

# some_range = range(x)

# def is_even(x):
#     return x % 2 == 0

# print(list(filter(is_even, some_range)))



# print(list(x for num in range(100) for x in [num, num] if num % 2 == 0))

# print(list(x for num in range(2_0) for x in range(num, num + 3)))


# print({x : y for x, y in enumerate(range(1_0))})

# def jojo():
#     for x in range(5):
#         yield x
#         # if x == 3:
#         #     return x
# print(*jojo())


# print(dict((x, y) for x, y in enumerate(range(10))))

# print(dict((x, y) for x, y in enumerate(range(10))))

# def f():
#     print("hello world")
#     yield "1"
#     print(1)
#     print(2)
#     print(3)
#     yield "2"

#     print(4)
#     print(5)
#     print(6)

#     yield "3"
#     print("That is all")


# x = f()

# print(next(x))
# # print(next(x))