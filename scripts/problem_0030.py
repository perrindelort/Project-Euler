from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem30(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"The sum of all the numbers that can be written as the sum of fifth powers of their digits is {format_number(self.answer)}"

    # TODO : move function to utils
    def is_sum_fifth_power_digits(self, integer):
        digits = str(integer)
        sum_digits = 0
        for digit in digits:
            sum_digits += int(digit) ** 5
        return sum_digits == integer

    @timing
    def solve(self) -> int:
        # I no longer have any idea of what I've done
        # What does max_iter does ??

        max_iter = 4
        sum1 = max_iter * 9**5
        sum2 = 0
        for i in range(max_iter):
            sum2 += 9 * 10**i
        while sum2 < sum1:
            sum2 += 9 * 10**max_iter
            max_iter += 1
            sum1 = max_iter * 9**5
        max_iter = sum1
        L = []
        for i in range(2, max_iter):
            if self.is_sum_fifth_power_digits(i):
                L.append(i)
        return sum(L)


if __name__ == "__main__":
    problem = Problem30()
    problem.print_problem()
