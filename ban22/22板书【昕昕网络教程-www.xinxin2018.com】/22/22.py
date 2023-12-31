'''
1. iterator

for ?
for (int i = 0; i < i_max ; i ++)
i = 0 i= 1初始化赋值
i++ 递进 i= i + 2

1. iter iter(obj) obj.__iter__()
2. next next(obj) obj.__next__()

(a)
for i in range(10):
    pass


(b)
iter_obj = range(10)
iter(iter_obj)

while True:
    try:
        i = next(iter_obj)
    except StopIteration:
        break
'''

# class Pow2(object):
#     def __init__(self, max):
#         self.max = max
#         self.n = 0
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             self.n += 1
#             return 2 ** self.n
#         else:
#             raise StopIteration
#
#
# p = Pow2(10)
# for i in p:
#     print(i)

'''
2. python instance method, class method, static method
instance method a = A() a.foo() a.bar()
class method bind class
static method
'''

# class A(object):
#     @staticmethod
#     def s_foo():
#         pass
#
#     @classmethod
#     def c_foo(cls):
#         pass
#
#     def foo(self):
#         pass
#
#
# a = A()
# a.foo()
# A.c_foo()

'''
引用类型
[] {}

深拷贝 浅拷贝

from copy import deepcopy
l1 = []
l2 = deepcopy(l1)
l1.append(1)
print(l2)

l1 = [1, [1, 2], 3]
l2 = l1[:]
'''

# def foo(a=[]):
#     a.append(1)
#     print(a)
#
# foo()
# foo()

'''
3. lambda closure closure ref

1. algorithm sort(lambda x : x['key'])
2. map reduce filter
'''
# import functools
# import operator
# mul2 = lambda x: 2 * x
# print(mul2(3))
#
# print(list(map(lambda x: 3 * x, [1, 2, 3, 4])))
# print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4])))
# print(functools.reduce(operator.add, [1, 2, 3, 4, 5], 5))

'''
closure
'''

# def greeting(msg):
#     def hello(name):
#         print(msg, name)
#     return hello
#
# h = greeting("welcome")
# h("akira")

# l = []
# for i in range(10):
#     def _(i=i):
#         print(i)
#     l.append(_)
#
# for f in l:
#     f()

'''
4. args kwargs
tuple
dict
*args  a,b,c,d
**kwargs k = v
'''

# def log(*args, **kwargs):
#     print("args", args)
#     print("kwargs", kwargs)
#
#
# log(1, 2, 3, 4)
# log(1, 2, [1, 2, 3], c=4)

'''
5.
list comprehension
[i for i in range(10)]
dict comprehension
{k:1 for k in range(10)}
list generator
(i for i in range(10))
dict generator
filter method
'''

'''
6. decorator
AOP aspect oriential programming
if debug:
    xxx
else:
    yyy
'''

# def simple_wrapper(fn):
#     def _():
#         #print(fn.__name__)
#         return fn()
#     return _
#
# def fix_arg_wrapper(fn):
#     def _(x):
#         #print(fn.__name__)
#         return fn(x)
#     return _
#
# def all_args_wrapper(fn):
#     def _(*args, **kwargs):
#         print(*args, **kwargs)
#         return fn(*args, **kwargs)
#     return _
#
# @simple_wrapper
# def foo():
#     pass
#
# @all_args_wrapper
# def bar(a, b, c):
#     pass
#
# #foo()
# bar(1, 2, 3)

'''
7. magic method
__xxx__

__getattribute__
__setattribute__

__getattr__
__setattr__

missing method
'''


# class LogAll(object):
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = 3
#     def __getattribute__(self, item):
#         print(item)
#
# l = LogAll()
# print(l.a)
# l.a = 1
# l.b
# l.c

# class Any(object):
#     def __getattr__(self, item):
#         print(item)
#
#     def __setattr__(self, key, value):
#         print("set", key, value)
#
# a = Any()
# a.a
# a.a = 1

# class Any(object):
#     def __getattr__(self, item):
#         def _(*args, **kwargs):
#             print("function name", item)
#             print("args", args)
#             print("kwargs", kwargs)
#
#         setattr(self, item, _)
#
#         return _
#
#
# a = Any()
# a.fuck(1, 2, 3)
# a.shit(1, 2, [1, 2, 3], c=[])

'''
8. mixin
c, c++, java

b -> a
a -> b

a -> a interface
b -> b interface

b->a interface
a->b interface

mixin
Final(A,B,C)
'''


# class A(object):
#     def foo(self):
#         print("foo")
#     def bar(self):
#         print("bar")
#         self.shit()
#
# class B(object):
#     def shit(self):
#         print("shit")
#
# class C(A, B):
#     pass
#
# c = C()
# c.bar()

'''
protocol
rpc

client
    server_client server_client.attack(xxx)
---->
Server
    logic.attack(xxx)

rpyc
'''

'''
1. tcp server tcp client
    tcp server bind accept recv parse call
    tcp client connect send data
2. function name function args function kwargs
    json
    {
        'function_name':name,
        'function_args':args,
        'function_kwargs':kwargs
    }
3. client
    c.foo(1, 2, 3)

    send
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    __getattr__ pack

4. server
    1. recv json
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    getattr(self, 'foo')
    getattr(self, 'foo')(*args, **kwargs)


'''

'''
vagrant

DevOps
虚拟化 虚拟机
1. openstack
2. docker
3. vagrant 开发测试
'''
