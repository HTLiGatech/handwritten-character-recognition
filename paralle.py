#-*- coding: UTF-8 -*-

# from multiprocessing.dummy import Pool as ThreadPool
# import time
# # global i
# i=0
# def gen():
#     global i
#     i+=1
#     return i

# a = gen()

# example_list = []
# def act(i):
#     example_list.append(gen())
#     # return example_list


# inputs=list(range(10000000))


# # data_gen_train = data_generators.get_anchor_gt(train_imgs, classes_count, C, K.image_dim_ordering(), mode='train')
# start_time = time.time()
# pool = ThreadPool(8)
# pool.map(act,inputs)
# pool.close()
# pool.join()
# print('Elapsed time: {}'.format(time.time() - start_time))

# for i in inputs:
#     example_list.append(gen())
# print('Elapsed time: {}'.format(time.time() - start_time))

# import time
# import multiprocessing

# def f(x):
#     return x * x


# cores = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=cores)
# xs = range(5000000)


# start_time = time.time()
# # method 1: map
# a = pool.map(f, xs)  # prints [0, 1, 4, 9, 16]

# # # method 2: imap
# # for y in pool.imap(f, xs):
# #     print y            # 0, 1, 4, 9, 16, respectively

# # # method 3: imap_unordered
# # for y in pool.imap_unordered(f, xs):
# #     print(y)           # may be in any order

# print('Elapsed time: {}'.format(time.time() - start_time))

# b=[]
# for  i in xs:
# 	b.append(f(i))

# print('Elapsed time: {}'.format(time.time() - start_time))
# 
# 

import math, sys, time
import pp
def IsPrime(n):
    """返回n是否是素数"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True
def SumPrimes(n):
    for i in xrange(15):
        sum([x for x in xrange(2,n) if IsPrime(x)])
    """计算从2-n之间的所有素数之和"""
    return sum([x for x in xrange(2,n) if IsPrime(x)])
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
start_time = time.time()
for input in inputs:
    print SumPrimes(input)
# print '单线程执行，总耗时', time.time() - start_time, 's'
# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("10.0.0.1",)
if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)
# print "pp 可以用的工作核心线程数", job_server.get_ncpus(), "workers"
start_time = time.time()
jobs = [(input, job_server.submit(SumPrimes,(input,), (IsPrime,), ("math",))) for input in inputs]
for input, job in jobs:
    print "Sum of primes below", input, "is", job()
# print "多线程下执行耗时: ", time.time() - start_time, "s"
job_server.print_stats()