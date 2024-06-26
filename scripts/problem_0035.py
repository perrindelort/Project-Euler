from util.util import timing, format_number
from util.funct import isprime
from scripts.abstract_problem import Problem


class Problem35(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"There are {format_number(self.answer)} circular primes below {format_number(kwargs['upper_bound'])}"

    # TODO : move function to utils
    def is_circular_prime(self, integer):
        if isprime(integer):
            integer_string = str(integer)
            for i in range(len(integer_string)):
                integer_string = integer_string[1:] + integer_string[0]
                if isprime(int(integer_string)) == False:
                    return False
            return True
        return False

    @timing
    def solve(self, upper_bound: int) -> int:
        circular_primes_list = []
        for integer in range(1, upper_bound + 1):
            if integer % 2 == 0 or integer % 5:
                pass
            if self.is_circular_prime(integer):
                circular_primes_list.append(integer)
        return len(circular_primes_list)


if __name__ == "__main__":
    problem = Problem35(upper_bound=1_000_000)
    problem.print_problem()
