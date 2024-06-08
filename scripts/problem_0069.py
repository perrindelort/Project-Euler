from primePy import primes
from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def calc_phi(n):
    factors = list(set(primes.factors(n)))
    p = n
    for factor in factors:
        p *= 1 - 1 / factor
    return p


class Problem69(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"n/phi(n) n ≤ {format_number(kwargs['upper_bound'])} is maximum for n = {format_number(self.answer[0])} and takes for value {format_number(self.answer[1])}"

        # We returned two values for detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        phi = {2: 1, 3: 2}
        best_n = 1
        best_value = 0
        for n in range(2, upper_bound + 1):
            phi_n = calc_phi(n)
            if n / phi_n > best_value:
                best_n = n
                best_value = n / phi_n
        return best_n, best_value


if __name__ == "__main__":
    problem = Problem69(upper_bound=1_000_000)
    problem.print_problem()
