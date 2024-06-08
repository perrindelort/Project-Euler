from util.util import timing, format_number
from util.funct import is_pan_digital
from scripts.abstract_problem import Problem


class Problem38(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        self.answer, self.time_taken = self.solve()

        self.detailed_answer = f"The largest 1 to 9 pandigital digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1 is {format_number(self.answer)}"

    @timing
    def solve(self) -> int:
        largest_pandecimal_number = 0
        """
        • n>1 => the base number must have less than 5 digits
        • the example starts with 9 => the base number must also start with 9
        • starting with a 2-digit number => we cannot make 9-digit numbers
        • starting with a 3-digit number => we cannot make 9-digit numbers
        => we search between 9123 and 9876
        We can further reduce this range, but this is sufficient...
        Time taken initially: 542 seconds (supremum = 987654321//3)
        """
        for integer in range(9123, 9876 + 1):
            concatenated_product = ""
            for n in range(1, 10):
                concatenated_product += str(integer * n)
                if is_pan_digital(concatenated_product):
                    if largest_pandecimal_number < int(concatenated_product):
                        largest_pandecimal_number = int(concatenated_product)
                if len(concatenated_product) > 9:
                    break

        return largest_pandecimal_number


if __name__ == "__main__":
    problem = Problem38()
    problem.print_problem()
