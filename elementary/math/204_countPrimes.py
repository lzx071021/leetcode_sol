"""Leetcode #204 计数质数"""

import math
import profile
import pstats


class Solution:
    def countPrimes(self, n: int) -> int:
        counter = []
        for j in range(2, n):
            for i in range(2, j):
                if j % i == 0:
                    break
            else:
                counter.append(j)

        return len(counter)

    def better_countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [2]
        for i in range(3, n):
            for prime in primes:
                if not i % prime:
                    break
            else:
                primes.append(i)
        return len(primes)

    def Sieve_of_Eratosthenes(self, n: int) -> int:
        prime_indicator = [i >= 2 for i in range(n)]
        for i in range(2, math.ceil(math.sqrt(n))):
            if prime_indicator[i]:
                for j in range(i**2, n, i):
                    prime_indicator[j] = False

        return sum(prime_indicator)


def print_running_time(func):
    profiler = profile.Profile()
    profiler.runcall(func)
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()


sol = Solution()
n = 49970
# print(sol.better_countPrimes(n))
# print(sol.Sieve_of_Eratosthenes(n))
print_running_time(lambda: sol.countPrimes(n))
print_running_time(lambda: sol.better_countPrimes(n))
print_running_time(lambda: sol.Sieve_of_Eratosthenes(n))
