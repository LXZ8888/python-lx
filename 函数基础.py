name, age, shouru = '清风', 30, 1.2
print('我是%s来自于湖南你年龄%d岁收入%s万' % (name, age, shouru))
print('我是{}来自于湖南你年龄{}岁收入{}万'.format(name, age, shouru))


def fun1(*args):
    print(args)
    print(type(args))


fun1(1, 2, 3, 4, 5)


#  *可以接受多个参数，多个参数值存在 一个元组中，调用函数时只能是位置传参
def fun2(**aargs):
    # 函数注释只是规范作用，没其他作用
    print(aargs)
    print(type(aargs))


fun2(name='qing', age=18)


#   **可以里接受多个参数，多个参数值 存在一个字典中，调用函数时只能是指定传 参

# 函数的嵌套
def fun3():
    print('这是方法一')


def fun4():
    fun3()
    print('这是方法二')
    fun3()

    def fun5():
        print('这是方法3')

    fun5()


fun4()


# 递归函数，自己调用自己
# 求阶层 n!=1*2*3*4*5*n-1*1

# def f(n):
#     sum = 1
#     for i in range(1, n + 1):
#         print(i)
#         sum = sum * i
#     return sum
#
#
# res=f(6)
# print(res)


# =1*2*3*4*5*6
# 6!=5!*6
# 4!=4!*5
# 3!=2!*3
# 2!=1!*2
# 递归
# 函数调用自己本身
# 有结束条件
def f(n):
    if n == 1:
        return 1
    else:
        return f(n - 1) * n
res2=f(6)
print(res2)