from typing import Tuple

from util.util import timing, format_number
from util.funct import factorial
from scripts.abstract_problem import Problem


class Problem20(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "target" not in kwargs.keys():
            raise ValueError("target not specified")

        self.answer, self.time_taken = self.solve(target=kwargs["target"])

        self.detailed_answer = f"The sum of the digits of {format_number(kwargs['target'])}! is {format_number(self.answer[0])}; \n{format_number(kwargs['target'])}!={format_number(self.answer[1])}"

        # We returned 2 arguments for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self, target: int) -> Tuple[int, int]:
        number = factorial(target)
        string = str(number)
        somme = 0
        for chiffre in string:
            somme += int(chiffre)
        return somme, number


if __name__ == "__main__":
    problem = Problem20(target=100)
    problem.print_problem()
