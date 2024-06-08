from math import ceil

from util.util import timing, format_number
from util.funct import primesfrom2to
from scripts.abstract_problem import Problem


class Problem87(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"There are {format_number(self.answer)} numbers below {format_number(kwargs['upper_bound'])} that can be written as a sum of a prime square, prime cube, and prime fourth power"

    @timing
    def solve(self, upper_bound: int) -> int:
        primes_list = primesfrom2to(ceil(upper_bound**0.5))
        primes_squares = []
        primes_cubes = []
        primes_hypercubes = []
        add_cubes = True
        add_hypercubes = True
        for p in primes_list:
            if p**2 < upper_bound:
                primes_squares.append(p**2)
            if add_cubes:
                if p**3 < upper_bound:
                    primes_cubes.append(p**3)
                    if add_hypercubes:
                        if p**4 < upper_bound:
                            primes_hypercubes.append(p**4)
                        else:
                            add_hypercubes = False
                else:
                    add_cubes = False

        triplets = []
        for p1 in primes_squares:
            for p2 in primes_cubes:
                for p3 in primes_hypercubes:
                    triplets.append([p1, p2, p3])
        sums = []
        for triplet in triplets:
            s = sum(triplet)
            if s < upper_bound:
                sums.append(s)
        return len(list(set(sums)))


if __name__ == "__main__":
    problem = Problem87(upper_bound=50_000_000)
    problem.print_problem()
