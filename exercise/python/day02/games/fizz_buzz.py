from typing import Optional

MIN = 1
MAX = 100
FIZZ = 3
BUZZ = 5


class FizzBuzz:
    @staticmethod
    def convert(input: int) -> Optional[str]:
        if FizzBuzz.is_out_of_range(input):
            return None
        else:
            return FizzBuzz.convert_safely(input)

    @staticmethod
    def convert_safely(input: int) -> str:
        result = ''
        if FizzBuzz.is_divisible_by(FIZZ, input):
            result += "Fizz"
        if FizzBuzz.is_divisible_by(BUZZ, input):
            result += "Buzz"
        if result == "":
            result = str(input)
        return result

    @staticmethod
    def is_divisible_by(divisor: int, input: int) -> bool:
        return input % divisor == 0

    @staticmethod
    def is_out_of_range(input: int) -> bool:
        return input < MIN or input > MAX
