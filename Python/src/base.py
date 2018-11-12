import time
def bench_mark(func):
    def bm(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print("Function {} took {} seconds to complete".format(func.__name__, execution_time))
        return res
    return bm
