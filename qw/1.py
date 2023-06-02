# some = """some value
#           to print"""

# print(some)

"some value to print"
"""some value to print"""
# import copy
# # print("hello")

# list_1 = [1, 2, 3, [1, 2, 3]]

# def some(list_1):
#     list_1.append("some")
#     list_1[-2][0] = "ahahah"


# # some(list(list_1))
# some(copy.deepcopy(list_1))


# print(list_1)



# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# some_func = outer(10)
# print(type(some_func))
# print(some_func(20))


# some_var = 10

# def some_func():
#     global some_var

#     print(some_var)
#     some_var = 111

# some_func()

# print("our var now is:", some_var)


# x = 10

# def some_func():
    
#     x = 666
    
#     def second_func():
#         nonlocal x
#         print(x)
#         x = 111
#     second_func()
#     print(x)
#     x = 11111111

# some_func()
# print(x)


# def counter():
#     cnt = 0
#     def inner():
#         nonlocal cnt
#         cnt += 1
#         return cnt
#     return inner

# some_func = counter()

# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())


# config = {
#     "language" : "kz",
#     "timezone" : "UTC"
# }

# def get_info(key):
#     def inner():
#         return config.get(key, None)
#     return inner

# get_to = get_info("language")

# print(get_to())
# print(get_to())
# print(get_to())
# print(get_to())



# def func(x):
#     return -x


# list_1 = [1, 3, 2, 4, 23, 325, 432, 23]

# # list_1.sort(key = lambda x: -x)
# list_1.sort(key = func)

# print(list_1)

# print(1 + (lambda x: x + 100)(100) + 3)


# def call(num):
#     return lambda x : x(num)

# some = call(100)

# print(some(float))

# print("hello")

# def wrapper(func):
#     def inner():
#         print("hello")
#         func()
#     # yield inner
#     return 5


# @wrapper 

# def some_f():
#     print("halo rebatya")

# # next(some_f)()
# print(some_f)

# def wrapper(x):
#     # return 5
#     # return x
#     # def inner(x):
#     #     return x(5) + 1
#     return x

# @wrapper

# def some(var):
#     print("hi")
#     return var

# print(some(10))


# def debag_dec(func):
#     def wrapper(args, kwargs):
#         print("func called:", func.__name__)
#         print("args:", args, kwargs)
#         result = func(args, kwargs)
#         print("result:", result)
#         return result

#     return wrapper


# @debag_dec


# def some_f(x: list, y: list) -> int:
#     x = sum(x)
#     y = sum(y)
#     return x - y

# some_f([1, 2, 3, 4], [5])

# a = some_f([1, 2, 3, 4], [5])
# print(a)





# @debag_dec
# @debag_dec

# def some_f(x: list, y: list) -> int:
#     x = sum(x)
#     y = sum(y)
#     return x - y

# some_f([1, 2, 3, 4], [5])



# def counter_of_function(func):
#     cnt = 0

#     def wrapper(*args, **kwargs):
#         nonlocal cnt
#         cnt += 1
#         print(f"function is work about {cnt} times")
#         func(*args, **kwargs)

#     return wrapper

# def debag_dec(func):
#     def wrapper(*args, **kwargs):
#         print("func called:", func.__name__)
#         print("args:", args, kwargs)
#         result = func(*args, *kwargs)
#         print("result:", result)
#         return result

#     return wrapper

# @counter_of_function
# @debag_dec
# def some_func(*args, **kwargs):
#     sum_ = sum(args)
#     print(sum_)
#     return sum_

# some_func(1, 2, 3, 4, 5)
        
# some_func(1, 2, 3, 4, 5)

# some_func(1, 2, 3, 4, 5)

# some_func(1, 2, 3, 4, 5)



# def check_args(predicate, error_msg):
#     def wrapper(func):
#         def inner(arg):
#             if not predicate(arg):
#                 raise ValueError(error_msg)
#             return func(arg)
#         return inner
#     return wrapper

# def greater_than(val):
#     def predicate(arg):
#         return arg > val
#     return predicate

# def in_(*values ):
#     def predicate(args):
#         return args in values
#     return predicate

# def not_(predicate_):
#     def predicate(arg):
#         return not predicate_(arg)
#     return predicate


# @check_args(greater_than(0), "non-positive")

# @check_args(not_(in_(1, 2, 3, 4, 5)), "BAD VALUE")

# def foo(arg):
#     return arg

# foo(1)


# dynamic programming
# def cache(some_func):
#     dict_1 = {}
#     def wrapper(args):
#         if args in dict_1.keys():
#             return dict_1[args]
            
#         else:
#             dict_1[args] = some_func(args)
#             return dict_1[args]
#     return wrapper

# @cache

# def add(x):
#     return x * 100

# print(add(5))

# print(add(5))
            


# def rec():
#     rec()

# rec()
# stack_overflow


# raise Exception("Some opps")
# raise "some ups"
# if type(text) != type("str"):
#     raise Exception("Eroroororororor")

# i = input()

# print(i)





            
# for i in range(12):
#     print("Hello ti")

 




