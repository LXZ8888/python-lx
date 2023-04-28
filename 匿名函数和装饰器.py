import logging


# def fun1(m):
#     return m**2
# print(fun1(10))
#
# def fun2(a,b):
#     return a+b
# print(fun2(1,2))
#
# # 匿名函数1
# res =lambda m:m**2
# print(res(10))
#
# # 匿名函数2
# res1=lambda a,b:a+b
# print(res1(1,2))
#
# # 匿名函数结合内置函数使用
# l=[10,20,30]
# res2=lambda l:sum(l)
# print('内置函数和匿名函数：',res2(l))
#
# res3=lambda *args:sum(args)
# print('不定长参数和匿名函数：',res3(1,3,5,7,8))

# 装饰器的原理和应用场景
# 让其他函数或类在不需要做任何代码修改的前提下增加额外功能。
# 作用：为已经存在的对象添加额外的功能。
# 1、函数可以作为另外一个函数的参数
# 2、 函数可以作为另外一个函数的返回值
# 3、当函数返回多个值的时候会组成元祖

# 需求：每个函数执行的时候打印日志，函数的运行时间
import time


def logging_fun(fun):
    # 封装一个打印函数执行的方法，执行方法之前先打印日志，再执行这个方法
    # logging.warning('{}函数开始执行'.format(fun.__name__))
    start_time=time.time()  #获取函数执行之前的时间
    fun()
    end_time=time.time()  #获取函数执行之后的时间
    run_time=end_time-start_time
    # 1:.2  取2位小数
    logging.warning('执行了{0}函数，执行时间{1:.2}'.format(fun.__name__,run_time))
# 获取方法名称:方法名称.__name__
def fun1():
    print('函数1')
    time.sleep(3)  # 等待3分钟
    # logging.warning('{}函数开始执行'.format(fun1.__name__))
    #     打印日志：WARNING:root:fun1函数开始执行
 # 空函数在Python2.x版本中pass是必须的
# 在Python3.x的时候pass可以写或不写

def fun2():
    # print(name)

    print('函数2')
    time.sleep(4)  # 等待3分钟
    # logging.warning('{}函数开始执行'.format(fun2.__name__))
    # # 打印日志: WARNING:root:fun2函数开始执行
    # return name
    # 返回值 <function fun1 at 0x0000018533E763A0>

def fun3():
    print('函数3')

# fun1()

# print(fun1)
#打印结果参数 <function fun1 at 0x0000020D7C0D63A0>
# fun1()
# res=fun2(fun1)
# print(res)
#
logging_fun(fun1)   #   函数1   WARNING:root:执行了fun1函数，执行时间3.0

logging_fun(fun2)  #   函数2   WARNING:root:执行了fun1函数，执行时间3.0
# logging_fun(fun3)   # WARNING:root:fun3函数开始执行
# 解决：装饰器。use_ logging破坏了原有的代码结构，  现在我们不得不每次都要把原来的 那个 fun1 函数作为参数传递给 use_ logging 函数


