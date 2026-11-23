import time
import sys
import matplotlib.pyplot as plt
import Three_sum
sys.path.append("Assignment_1")
from Util import random_list


def time_test_three_sum(randomlst, alg):
    time1 = time.time()
    alg(randomlst, 0)
    time2 = time.time()
    return time2 - time1


def main():
    lists = random_list.random_list(300, 800, 50, 10)
    algs = [Three_sum.three_sum_brute,
            Three_sum.three_sum_pointers,
            Three_sum.three_sum_caching]
    for alg in algs:
        for run in range(3):
            sizes = []
            times = []
            for lst in lists:
                t = time_test_three_sum(lst, alg)
                sizes.append(len(lst))
                times.append(t)
            
    plt.plot(sizes, times, marker="o", label=alg.__name__)
    plt.xlabel("Listlängd")
    plt.ylabel("Tid (s)")
    plt.legend()
    plt.show()


main()
