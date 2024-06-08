import decimal

from math import floor
from typing import Tuple

from util.util import timing, format_number
from util.funct import is_perfect_square
from scripts.abstract_problem import Problem


# TODO : move function to utils
# From Problem 66
# And https://fr.wikipedia.org/wiki/%C3%89quation_de_Pell-Fermat#Cas_m_=_1
def get_fundamental_solution(sqrt_integer):

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

    if length % 2 == 0:
        return h_n, k_n

    else:
        for _ in range(length):
            h_n = a_n * h_n1 + h_n2
            k_n = a_n * k_n1 + k_n2

            k_n1, k_n2 = k_n, k_n1
            h_n1, h_n2 = h_n, h_n1

            a_n = int(-(sqrt_integer * k_n2 - h_n2) / (sqrt_integer * k_n1 - h_n1))

        return h_n, k_n


class Problem66(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        if "precision" not in kwargs.keys():
            raise ValueError("precision not specified")

        self.answer, self.time_taken = self.solve(
            upper_bound=kwargs["upper_bound"], precision=kwargs["precision"]
        )

        self.detailed_answer = f"The value of D ≤ {format_number(kwargs['upper_bound'])} for which the largest value of x obtained is {format_number(self.answer[0])} \nThe corresponding Diophantine - or rather Pell's - equation is : {format_number(self.answer[1])}^2 - {format_number(self.answer[0])} × {format_number(self.answer[1])}^2 = 1"

        # We returned 3 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, upper_bound: int, precision: int) -> Tuple[int, int, int]:
        decimal.getcontext().prec = precision
        x = 0
        y = 0
        d = 0
        for integer in range(2, upper_bound + 1):
            if is_perfect_square(integer) == False:
                h, k = get_fundamental_solution(
                    decimal.Decimal(integer) ** decimal.Decimal(0.5)
                )
                if h > x:
                    x, y, d = h, k, integer
        return d, x, y


if __name__ == "__main__":
    problem = Problem66(upper_bound=1_000, precision=75)
    problem.print_problem()
