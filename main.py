import math


def get_factors(n: int):
    return [i for i in range(2, n - 1) if n % i == 0]


def get_perfect_squares(factors: list):
    return [i for i in factors if i == int(math.isqrt(i) ** 2)]


def get_greatest_factor(factors: list):
    return sorted(factors, reverse=True)[0]


def simplify(n: int):
    #check if number is a square root
    if n == math.isqrt(n) ** 2:
        return f"{int(math.sqrt(n))}"

    #check if there are any factors
    factored = get_factors(n)
    if len(factored) == 0:
        return f"√{n}"

    #check if there are any perfect squares in the factors
    squares = get_perfect_squares(factored)

    if len(squares) == 0:
        #find greatest factor in factors and simplify
        greatest_factor = get_greatest_factor(factored)
        return "*".join((simplify(greatest_factor), simplify(int(n / greatest_factor))))

    #find greatest factors in the perfect squares and simplify
    greatest_factor = get_greatest_factor(squares)
    return "*".join((simplify(greatest_factor), simplify(int(n / greatest_factor))))


def main():
    print(simplify(int(input("Enter a number: "))))


if __name__ == "__main__":
    main()
