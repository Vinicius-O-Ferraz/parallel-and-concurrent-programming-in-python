import multiprocessing as mp 
import time
import math

def make_calculation_a(numbers, result_a):
    for n in numbers:
        result_a.append(math.sqrt(n**3))

def make_calculation_b(numbers, result_b):
    for n in numbers:
        result_b.append(math.sqrt(n**4))

def make_calculation_c(numbers, result_c):
    for n in numbers:
        result_c.append(math.sqrt(n**5))

if __name__ == '__main__':
    number_list = list(range(100))

    # Single process
    start = time.time()

    result_a, result_b, result_c = [], [], []
    make_calculation_a(number_list, result_a) 
    make_calculation_b(number_list, result_b)
    make_calculation_c(number_list, result_c)

    end = time.time()
    print(f'The elapsed time (single process) was {end - start}')

    # Multiple processes
    start = time.time()

    # Manager list to share results across processes
    manager = mp.Manager()
    result_a = manager.list()
    result_b = manager.list()
    result_c = manager.list()

    p1 = mp.Process(target=make_calculation_a, args=(number_list, result_a))
    p2 = mp.Process(target=make_calculation_b, args=(number_list, result_b))
    p3 = mp.Process(target=make_calculation_c, args=(number_list, result_c))

    p1.start()
    p2.start()
    p3.start()

    p1.join()  # Wait for p1 to complete
    p2.join()  # Wait for p2 to complete
    p3.join()  # Wait for p3 to complete

    end = time.time()
    print(f'The elapsed time (multiple processes) was {end - start}')

    print(list(result_a))
    print(list(result_b))
    print(list(result_c))
