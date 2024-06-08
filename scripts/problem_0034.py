from util.util import timing, format_number
from util.funct import factorial
from scripts.abstract_problem import Problem


class Problem34(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "upper_bound" not in kwargs.keys():
            raise ValueError("upper_bound not specified")

        self.answer, self.time_taken = self.solve(upper_bound=kwargs["upper_bound"])

        self.detailed_answer = f"The sum of all numbers which are equal to the sum of the factorial of their digits is {format_number(self.answer)}"

    @timing
    def solve(self, upper_bound: int) -> int:
        factorial_value = []
        for i in range(10):
            factorial_value.append(factorial(i))
        numbers_sum_factorial_digits = []
        for integer in range(5, upper_bound + 1, 2):
            integer_string = str(integer)
            sum_factorial_digits = 0
            for digit in integer_string:
                sum_factorial_digits += factorial_value[int(digit)]
            if sum_factorial_digits == integer:
                numbers_sum_factorial_digits.append(integer)
        return sum(numbers_sum_factorial_digits)


if __name__ == "__main__":
    problem = Problem34(upper_bound=9_999_999)  # #9999999 > 6•9!
    problem.print_problem()
