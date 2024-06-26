from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move function to utils
def is_power(N, n):
    r = round(N ** (1.0 / n))
    return r**n == N


class Problem62(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "number_of_permutations" not in kwargs.keys():
            raise ValueError("number_of_permutations not specified")

        self.answer, self.time_taken = self.solve(
            number_of_permutations=kwargs["number_of_permutations"]
        )

        self.detailed_answer = f"The smalled cube for which exactly {format_number(kwargs['number_of_permutations'])} of its digits are cube is {format_number(self.answer)}"

    # TODO : number_of_permutations needed ?
    @timing
    def solve(self, number_of_permutations: int) -> int:
        cubes = []
        iterator = 0
        while True:
            cube = sorted(list(str(iterator**3)))

            cubes.append(cube)

            if cubes.count(cube) == 5:
                return cubes.index(cube) ** 3
            iterator += 1


if __name__ == "__main__":
    problem = Problem62(number_of_permutations=5)
    problem.print_problem()
