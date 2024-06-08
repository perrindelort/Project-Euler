import numpy as np

from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """Input n>=6, Returns a array of primes, 2 <= p < n"""
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3) :: 2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3 :: 2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


class Problem50(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The prime below {format_number(kwargs['upper_bound'])} which can be written as the sum of the most consecutive primes is {format_number(self.answer[0])} as it is the sum of {format_number(self.answer[1])} consecutive primes !"

        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        prime_list = primesfrom2to(upper_bound)
        max_numbers_of_terms = 6
        best_prime = 41
        for index_prime in range(0, len(prime_list)):
            new_prime_list = prime_list[: index_prime + 1]
            prime = prime_list[index_prime]
            for i in range(len(new_prime_list)):
                numbers_of_terms = max_numbers_of_terms
                sum_prime = sum(new_prime_list[i : i + numbers_of_terms])
                if sum_prime > prime:
                    break
                while sum_prime < prime:
                    numbers_of_terms += 1
                    sum_prime = sum(new_prime_list[i : i + numbers_of_terms])
                    if sum_prime == prime:
                        best_prime = prime
                        max_numbers_of_terms = numbers_of_terms
        return best_prime, max_numbers_of_terms


if __name__ == "__main__":
    problem = Problem50(upper_bound=1_000_000)
    problem.print_problem()
