import numpy as np

from math import ceil
from itertools import permutations
from typing import List, Tuple

from util.util import timing, format_number
from scripts.abstract_problem import Problem


# TODO : move functions to utils
def triangle(n):
    return int(n * (n + 1) / 2)


def square(n):
    return int(n * n)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


def heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def octagonal(n):
    return int(n * (3 * n - 2))


def add(dictionary, number):
    s = number[:2]
    e = number[2:]
    try:
        dictionary["start"][s] = [number]
    except:
        dictionary["start"][s].append(number)
    try:
        dictionary["end"][e] = [number]
    except:
        dictionary["end"][e].append(number)


def verify_condition(L):
    for index in range(len(L)):
        if not L[index - 1][2:] == L[index][:2]:
            return False
    return True


class Problem61(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"The sought set is {self.answer[1]} and the sum of its number is {format_number(self.answer[0])}"

        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]

    @timing
    def solve(self) -> Tuple[int, List[int]]:
        # Ugly Solution but it works ¯\_(ツ)_/¯

        max_int = 10_000
        min_int = 1_000
        coefficients_min = [
            [1 / 2, 1 / 2, -min_int],
            [1 / 2, 0, -min_int],
            [3 / 2, -1 / 2, -min_int],
            [2, -1, -min_int],
            [5 / 2, -3 / 2, -min_int],
            [3, -2, -min_int],
        ]
        coefficients_max = [
            [1 / 2, 1 / 2, -max_int],
            [1 / 2, 0, -max_int],
            [3 / 2, -1 / 2, -max_int],
            [2, -1, -max_int],
            [5 / 2, -3 / 2, -max_int],
            [3, -2, -max_int],
        ]
        roots_min = [ceil(max(np.roots(coeff))) for coeff in coefficients_min]
        roots_max = [ceil(max(np.roots(coeff))) for coeff in coefficients_max]
        infimum = min(roots_min)
        supremum = max(roots_max)
        pentagonals_dict = {"start": {}, "end": {}}
        squares_dict = {"start": {}, "end": {}}
        triangles_dict = {"start": {}, "end": {}}
        hexagonals_dict = {"start": {}, "end": {}}
        heptagonals_dict = {"start": {}, "end": {}}
        octagonals_dict = {"start": {}, "end": {}}
        triangles = []
        squares = []
        pentagonals = []
        hexagonals = []
        heptagonals = []
        octagonals = []
        for n in range(infimum, supremum):
            number = str(pentagonal(n))
            if len(number) == 4:
                add(pentagonals_dict, number)
                pentagonals.append(number)
            number = str(square(n))
            if len(number) == 4:
                add(squares_dict, number)
                squares.append(number)
            number = str(triangle(n))
            if len(number) == 4:
                add(triangles_dict, number)
                triangles.append(number)
            number = str(hexagonal(n))
            if len(number) == 4:
                add(hexagonals_dict, number)
                hexagonals.append(number)
            number = str(heptagonal(n))
            if len(number) == 4:
                add(heptagonals_dict, number)
                heptagonals.append(number)
            number = str(octagonal(n))
            if len(number) == 4:
                add(octagonals_dict, number)
                octagonals.append(number)

        L = [
            triangles_dict,
            squares_dict,
            pentagonals_dict,
            hexagonals_dict,
            heptagonals_dict,
            octagonals_dict,
        ]
        perm = permutations(L, 6)
        for permutation in perm:
            for s1 in permutation[0]["start"].keys():
                for number1 in permutation[0]["start"][s1]:
                    e1 = number1[2:]
                    for e6 in permutation[5]["end"]:
                        if s1 == e6:
                            for number6 in permutation[5]["end"][e6]:
                                s6 = number6[:2]
                                if s6 in permutation[4]["end"].keys():
                                    for number5 in permutation[4]["end"][s6]:
                                        s5 = number5[:2]
                                        if s5 in permutation[3]["end"].keys():
                                            for number4 in permutation[3]["end"][s5]:
                                                s4 = number4[:2]
                                                if s4 in permutation[2]["end"].keys():
                                                    for number3 in permutation[2][
                                                        "end"
                                                    ][s4]:
                                                        s3 = number3[:2]
                                                        if (
                                                            s3
                                                            in permutation[1][
                                                                "end"
                                                            ].keys()
                                                        ):
                                                            for number2 in permutation[
                                                                1
                                                            ]["end"][s3]:
                                                                s2 = number2[:2]
                                                                if s2 == e1:
                                                                    return sum(
                                                                        [
                                                                            int(
                                                                                number1
                                                                            ),
                                                                            int(
                                                                                number2
                                                                            ),
                                                                            int(
                                                                                number3
                                                                            ),
                                                                            int(
                                                                                number4
                                                                            ),
                                                                            int(
                                                                                number5
                                                                            ),
                                                                            int(
                                                                                number6
                                                                            ),
                                                                        ]
                                                                    ), [
                                                                        int(number1),
                                                                        int(number2),
                                                                        int(number3),
                                                                        int(number4),
                                                                        int(number5),
                                                                        int(number6),
                                                                    ]


if __name__ == "__main__":
    problem = Problem61()
    problem.print_problem()
