def addition(a: int, b: int) -> int:
    return a + b


def subtraction(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    return a / b


PI = 3.14

if __name__ == "__main__":
    print(f"Calculator file __name__ = {__name__}")
    print("Testing this code - START")
    result = addition(10, 20)
    print(f"Addition answer = {result}")
    print("Testing this code - END")
