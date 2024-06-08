from typing import Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem26(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The value of d < {format_number(kwargs['upper_bound'])} for which 1/d contains the longest recurring cycle in its decimal fraction part is {format_number(self.answer[0])} with a {format_number(self.answer[1])}-long cycle "

        # Because we returned 2 values for the detailed_answer
        self.answer = self.answer[0]

    # TODO : move function to utils
    def find_cycle_length(self, integer):
        remainder_list = []
        stop = False
        remainder = 1
        while stop == False:
            remainder = remainder % integer
            if remainder not in remainder_list:
                remainder_list.append(remainder)
                remainder = remainder * 10
            else:
                stop = True
        return len(remainder_list)

    @timing
    def solve(self, upper_bound: int) -> Tuple[int, int]:
        longest_cycle = 0
        integer = 0
        for i in range(1, upper_bound):
            if (
                i % 2 != 0 and i % 5 != 0
            ):  # Sinon, on a déjà obtenu la longueur précédemment
                length_cycle = self.find_cycle_length(i)
                if length_cycle > longest_cycle:
                    integer = i
                    longest_cycle = length_cycle
        return (integer, longest_cycle)


if __name__ == "__main__":
    problem = Problem26(upper_bound=1_000)
    problem.print_problem()
