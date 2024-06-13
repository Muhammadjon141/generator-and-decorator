import time
import generator

def decorator1():
    yield 5*5

def decoratos2():
    yield "Asadbek"
    yield 5263
    for i in generator.Range(-25, -2, 2.5):
        yield(i)
    
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for value in func(*args, **kwargs):
            end_time = time.time()
            print(f"Qiymat {value} {end_time - start_time} soniyada qaytarildi")
            yield value
            start_time = time.time()
    return wrapper

@timer_decorator
def my_generator(n):
    for i in range(n):
        time.sleep(1)
        yield i

gen = my_generator(3)

def main():
    yield decorator1()
    yield decoratos2()
    yield gen
main = main()
if __name__ == "__main__":
    for i in main:
        for j in i:
            print(j)