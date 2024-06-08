from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def is_solution(number):
    number_string = str(number)
    number_string6 = str(number * 6)
    if len(number_string) != len(number_string6):
        return False
    else:
        set_number = set(number_string)
        multiplier = 2
        while multiplier < 7:
            if set_number != set(str(number * multiplier)):
                return False
            multiplier += 1
        return True


class Problem52(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = (
            f"The smallest integer x satisfying the problem is {format_number(self.answer)} as "
            + " ".join(
                [f"{idx}x = {format_number(idx * self.answer)}" for idx in range(2, 7)]
            )
        )

    @timing
    def solve(self) -> int:
        # No particular optimisation needed
        number = 1
        while True:
            if is_solution(number):
                return number
            number += 1


if __name__ == "__main__":
    problem = Problem52()
    problem.print_problem()
