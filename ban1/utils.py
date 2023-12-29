# coding utf-8

# *args表示任意个位置参数,会以tuple的形式保存。**kwargs表示关键字参数,会以dict的形式保存。
# def func(a, b, c):
#   print(a, b, c)

# func(1, c=3, b=2) # 正确
# func(1, b=2, c=3) # 正确
# func(c=3, 1, b=2) # 错误,位置参数不能在关键字参数后面
# func(1, b=2) # 错误,缺少一个位置参数c
# 位置参数要先于关键字参数指定
# 所有的位置参数必须要指定,否则会报错
# 关键字参数可以不按顺序指定
def log(*args, **kwargs):
  print('log',*args, **kwargs)

