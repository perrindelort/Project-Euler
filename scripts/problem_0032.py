from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem32(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The sum of of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is {format_number(self.answer)}"

    # TODO : move function to utils
    def is_pan_digital(self, string):
        if len(string) != 9:
            return False
        for i in range(1, 10):
            if string.count(str(i)) != 1:
                return False
        return True

    @timing
    def solve(self, upper_bound: int) -> int:
        L = []
        for i in range(1, upper_bound):
            for j in range(1, upper_bound // i):
                a = i * j
                string = str(a) + str(i) + str(j)
                if len(string) > 10:
                    break
                if self.is_pan_digital(string):
                    L.append(a)
        return sum(list(set(L)))


if __name__ == "__main__":
    problem = Problem32(upper_bound=9876)
    problem.print_problem()
