from math import floor
import decimal

from util.util import timing, format_number
from util.funct import is_perfect_square
from scripts.abstract_problem import Problem

# TODO : move function to utils
"""
   https://fr.wikipedia.org/wiki/Fraction_continue#Fraction_continue_d'un_r%C3%A9el
"""


def calc_length_period(sqrt_integer):

    a_0 = floor(sqrt_integer)
    a_n = a_0
    h_n2, h_n1 = 0, 1
    k_n2, k_n1 = 1, 0
    length = 0

    while a_n != a_0 * 2:

        h_n = a_n * h_n1 + h_n2
        k_n = a_n * k_n1 + k_n2

        k_n1, k_n2 = k_n, k_n1
        h_n1, h_n2 = h_n, h_n1
        a_n = int(-(sqrt_integer * k_n2 - h_n2) / (sqrt_integer * k_n1 - h_n1))
        length += 1

    return length


class Problem64(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        if "precision" not in kwargs.keys():
            raise ValueError("precision not specified")

        self.answer, self.time_taken = self.solve(
            upper_bound=kwargs["upper_bound"], precision=kwargs["precision"]
        )

        self.detailed_answer = f"The number of continued fraction that have an odd period for N ≤ {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int, precision: int) -> int:
        decimal.getcontext().prec = precision
        count = 0
        for integer in range(2, upper_bound + 1):
            if is_perfect_square(integer) == False:
                length = calc_length_period(
                    decimal.Decimal(integer) ** decimal.Decimal(0.5)
                )
                if length % 2 == 1:
                    count += 1
        return count


if __name__ == "__main__":
    problem = Problem64(upper_bound=10_000, precision=215)
    problem.print_problem()
