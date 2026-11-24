import math
import time
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import Three_sum
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Util import random_list
from sort_algorithms import Bubble_sort
from sort_algorithms import insertion_sort
from sort_algorithms import merge_sort_slow
from sort_algorithms import quick_sort
from sort_algorithms import Selection_sort
from sort_algorithms import bucket_sort
from sort_algorithms import radix_sort


def lin_reg(x, y):  # denna funktion tar reda på lutningen av en graf
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum(i * i for i in x)
    sxy = sum(x[i] * y[i] for i in range(n))
    denominator = n * sxx - sx ** 2
    m = (sxx * sy - sx * sxy) / denominator
    k = (n * sxy - sx * sy) / denominator
    return m, k


def time_test_sort(randomlst, alg):  # Tar tiden
    time1 = time.time()
    alg(randomlst.copy())
    time2 = time.time()
    return time2 - time1


def test_sort(algs, lists, runs):
    sizes = []
    for lst in lists:  # sparar storlekar för matplot
        sizes.append(len(lst))

    results = {}
    for alg in algs:
        all_runs = []
        for lst in lists:  # loopar alla random listor
            run_times = []
            for _ in range(runs):  # loopar flera gånger, för att säkerställa
                run_times.append(time_test_sort(lst, alg))
            all_runs.append(run_times)
        results[alg.__name__] = all_runs  # sparar med namet
        print(alg.__name__, "klar")
    return sizes, results


def test_three_sum(algs, sizes_for, repeat, target):
    results = []
    for name, threesum in algs:  # kör alla algs repeat gånger
        for run in range(1, repeat + 1):
            for size in sizes_for(name):
                data = random_list.random_list(size)
                before = time.time()
                threesum(data, target)  # kör själva algen
                results.append((name, size, time.time() - before, run))
    return results


def group_three_sum(results, names):  # grupperar tider med alg o list sorlek
    grouped = {}
    for name, size, run_time, run in results:
        grouped.setdefault(name, {}).setdefault(size, []).append(run_time)
    return {name: grouped[name] for name in names}


def three_sum_averages(grouped):  # Räknar ut medeltiden för varje liststorlek
    averages = {}
    for name, by_size in grouped.items():
        sizes = sorted(by_size)  # o sorterar
        averages[name] = (sizes, [sum(by_size[s]) / len(by_size[s]) for s in sizes])
    return averages


def plot_sort_average(sizes, results, title="Sortering - snittid"):  # graf för snitt på sort
    for name in results:
        averages = []
        for run_times in results[name]:
            averages.append(sum(run_times) / len(run_times))
        plt.plot(sizes, averages, marker="o", label=name)
    plt.title(title)
    plt.xlabel("Listlängd")
    plt.ylabel("Snittid i sekunder")
    plt.legend()
    plt.show()


def plot_sort_all_runs(sizes, results, title="Sortering - alla körningar"):
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]  # graf på alla runs i sort

    for color_index, name in enumerate(results):
        color = colors[color_index % len(colors)]
        runs = len(results[name][0])  # antal körningar per lista

        for r in range(runs):
            times = [run_times[r] for run_times in results[name]]
            plt.plot(sizes, times, marker="o", color=color,
                     alpha=0.6, label=name if r == 0 else None)

    plt.title(title)
    plt.xlabel("Listlängd")
    plt.ylabel("Tid i sekunder")
    plt.legend()
    plt.show()


def plot_sort_loglog(sizes, results):  # graf för lutning på sort
    for name, all_runs in results.items():
        averages = [
            sum(run_times) / len(run_times)
            for run_times in all_runs
        ]
        _, exponent = lin_reg(
            [math.log(size) for size in sizes],
            [math.log(time) for time in averages],
        )
        plt.loglog(sizes, averages, marker="o", label=f"{name} (k={exponent:.3f})")
        print(f"{name}: uppskattad exponent ≈ {exponent:.2f}")
    plt.title("Sortering - log-log")
    plt.xlabel("Listlängd (logaritmisk skala)")
    plt.ylabel("Snittid (logaritmisk skala)")
    plt.legend()
    plt.show()


def plot_three_sum_average(averages):  # graf för snitt tre sum
    for name, (sizes, avg) in averages.items():
        plt.plot(sizes, avg, marker="o", label=name)
    plt.title("Three-sum - snittid")
    plt.xlabel("Listlängd")
    plt.ylabel("Snittid i sekunder")
    plt.legend()
    plt.show()


def plot_three_sum_loglog(averages):  # graf på tre sum lutning
    for name, (sizes, avg) in averages.items():
        _, exponent = lin_reg(
            [math.log(size) for size in sizes],
            [math.log(time) for time in avg],
        )
        plt.loglog(sizes, avg, marker="o", label=f"{name} (k={exponent:.3f})")

        print(f"{name}: uppskattad exponent ≈ {exponent:.2f}")
    plt.title("Three-sum - log-log")
    plt.xlabel("Listlängd (logaritmisk skala)")
    plt.ylabel("Snittid (logaritmisk skala)")
    plt.legend()
    plt.show()


def plot_three_sum_all_runs(grouped, repeat):  # graf alla tre sum
    for name, by_size in grouped.items():
        sizes = sorted(by_size)
        for run in range(repeat):
            run_times = [by_size[size][run] for size in sizes]
            plt.plot(sizes, run_times, marker="o", alpha=0.6,
                     label=name if run == 0 else None)
    plt.title("Three-sum - alla körningar")
    plt.xlabel("Listlängd")
    plt.ylabel("Tid i sekunder")
    plt.legend()
    plt.show()


def run_three_sum():
    target = 0  # Vilken summa vi vill ha o hur många gånger den körs
    repeat = 5
    size = range(2500, 10000, 500)
    brute_size = range(100, 1000, 50)
    algs_three = [("brute", Three_sum.three_sum_brute),
                  ("pointers", Three_sum.three_sum_pointers),
                  ("caching", Three_sum.three_sum_caching)]

    def sizes_for(name):  # Om brute force kör mindre storlek
        return brute_size if name == "brute" else size
    # hanterar data o sparar den
    results = test_three_sum(algs_three, sizes_for, repeat, target)
    grouped = group_three_sum(results, [name for name, _ in algs_three])
    averages = three_sum_averages(grouped)
    # skickar till plot
    plot_three_sum_average(averages)
    plot_three_sum_loglog(averages)
    plot_three_sum_all_runs(grouped, repeat)


def run_sorting():  # Kör sort n^2
    algs_n2 = [Bubble_sort.bubble_sort,
               insertion_sort.insertion_sort,
               Selection_sort.selction_sort]
    lists_n2 = [random_list.random_list(length) for length in range(2000, 9001, 1000)]
    sort_sizes, sort_results = test_sort(algs_n2, lists_n2, 3)
    # lite storlekar på listor och sparar data samt skickar vidare till plot
    plot_sort_average(sort_sizes, sort_results)
    plot_sort_all_runs(sort_sizes, sort_results)
    plot_sort_loglog(sort_sizes, sort_results)


def run_sorting_nlogn():  # kör sort n*log(n) i tidskompexitet
    algs_nlogn = [merge_sort_slow.merge_sort_slow,
                  quick_sort.quick_sort_slow]
    lists_nlogn = [random_list.random_list(length) for length in range(20000, 200001, 20000)]
    sort_sizes, sort_results = test_sort(algs_nlogn, lists_nlogn, 3)
    # Sparar data och skickar vidare
    plot_sort_average(sort_sizes, sort_results)
    plot_sort_all_runs(sort_sizes, sort_results)
    plot_sort_loglog(sort_sizes, sort_results)


def run_sorting_speed():  # kör de absolut snabbaste
    algs = [quick_sort.quick_sort_mean,  # den förbättrade quick med snitt
            bucket_sort.bucket_sort,
            radix_sort.radix_sort]
    lists = [random_list.random_list(length) for length in range(100000, 500001, 100000)]
    sort_sizes, sort_results = test_sort(algs, lists, 3)
    # spara data o skickar vidare
    plot_sort_average(
        sort_sizes,
        sort_results,
        "Sortering - quick_sort_mean, bucket och radix",
    )


def main():
    run_three_sum()
    run_sorting()
    run_sorting_nlogn()
    run_sorting_speed()


main()  # Drar igång festen yippie
