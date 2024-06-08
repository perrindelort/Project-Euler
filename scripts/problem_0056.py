from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def sum_integers(number):
    s = 0
    for integer in str(number):
        s += int(integer)
    return s


class Problem56(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound_a" not in kwargs.keys():
            raise ValueError("upper_bound_a not specified")

        if "upper_bound_b" not in kwargs.keys():
            raise ValueError("upper_bound_b not specified")

        self.answer, self.time_taken = self.solve(
            upper_bound_a=kwargs["upper_bound_a"], upper_bound_b=kwargs["upper_bound_b"]
        )

        self.detailed_answer = f"The maximal digit sum of a^b with a < {format_number(kwargs['upper_bound_a'])} and b < {format_number(kwargs['upper_bound_b'])} is obtained with a = {format_number(self.answer[1])} and b = {format_number(self.answer[2])} \na^b = {format_number(self.answer[3])}.\nThe value of the sums of digits of this number is {format_number(self.answer[0])}"

        # We returned 3 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(
        self, upper_bound_a: int, upper_bound_b: int
    ) -> Tuple[int, int, int, int]:
        max_sum = 0
        max_number = 0
        for a in range(1, upper_bound_a):
            for b in range(1, upper_bound_b):
                number = a**b
                s_integers = sum_integers(number)
                if s_integers > max_sum:
                    max_sum = s_integers
                    max_a = a
                    max_b = b
                    max_number = number
        return max_sum, max_a, max_b, max_number


if __name__ == "__main__":
    problem = Problem56(upper_bound_a=100, upper_bound_b=100)
    problem.print_problem()
