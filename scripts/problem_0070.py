from primePy import primes
from collections import Counter
from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def calc_phi(n):
    factors = list(set(primes.factors(n)))
    p = n
    for factor in factors:
        p *= 1 - 1 / factor
    return int(p)


class Problem70(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The value of n, 1 < n < 10^7 for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum is n = {format_number(self.answer[1])} for which n/phi(n) = {format_number(self.answer[0])}"

        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        # Ugly solution
        best_n = 2
        best_value = 5
        for n in range(2, upper_bound):
            phi_n = calc_phi(n)
            if n / phi_n < best_value:
                counter_n = Counter(str(n))
                counter_phi_n = Counter(str(phi_n))
                if counter_phi_n == counter_n:
                    best_value = n / phi_n
                    best_n = n
        return (
            best_n,
            best_value,
        )


if __name__ == "__main__":
    problem = Problem70(upper_bound=10_000_000)
    problem.print_problem()
