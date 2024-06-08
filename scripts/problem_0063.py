from typing import List, Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem63(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"There are {format_number(self.answer[0])} n-digit positive integers that exist which are also an nth power \nThe complete list being {self.answer[1]}"

        # We returned two values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self) -> Tuple[int, List[int]]:
        count = 0
        numbers = []
        for integer in range(1, 10):
            # Kind of bruteforcing or I don't remember how I ended-up with this bound honestly
            for power in range(50):
                number_string = str(integer**power)
                if len(number_string) == power:
                    count += 1
                    numbers.append(int(number_string))
        numbers = sorted(numbers)
        return count, numbers


if __name__ == "__main__":
    problem = Problem63()
    problem.print_problem()
