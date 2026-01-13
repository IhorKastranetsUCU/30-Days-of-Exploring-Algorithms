def binary_exponentiation(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1

    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base

        exponent //= 2

    return result

if __name__ == "__main__":
    print(binary_exponentiation(2, 10))
    print(binary_exponentiation(3, 5))
