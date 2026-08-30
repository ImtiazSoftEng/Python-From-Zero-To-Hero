#Example: Python User-Defined Exception
#define Python user-defined exceptions
class InvalidAgeError(Exception):
    """Raised when the input value is less than 18."""
    pass
#you need to guess this number
number = 18

try:
    input_num=int(input("Enter a number:"))

    if input_num < number:
        raise InvalidAgeError
    else:
        print("You are eligible to vote.")
except InvalidAgeError:
    print("Exception occurred: Invalid Age")

    # Customizing Exception Classes
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary."""
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

# Safe execution with try...except
try:
    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)
    print(f"Salary ${salary} accepted.")
except SalaryNotInRangeError as err:
    print(f"Exception occurred: {err}")