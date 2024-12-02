from typing import Optional


MIN = 1
MAX = 100
FIZZ = 3
BUZZ = 5
WHIZZ = 7
BANG = 11



class FizzBuzz:

    def __init__(self, conversions):
        self.conversions = conversions

    def convert(self,input: int) -> Optional[str]:
        if FizzBuzz.is_out_of_range(input):
            return None
        else:
            return self.convert_safely(input)


    def convert_safely(self,input: int) -> str:
        result = ''
        for value,conversion in self.conversions.items():
            if self.is_divisible_by(value, input):
                result += conversion
        if result == "":
            result = str(input)
        return result

    @staticmethod
    def is_divisible_by(divisor: int, input: int) -> bool:
        return input % divisor == 0

    @staticmethod
    def is_out_of_range(input: int) -> bool:
        return input < MIN or input > MAX
