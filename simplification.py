import numpy as np
import math

perfect_squares = {1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9, 100: 10, 121: 11, 144: 12, 169: 13, 196: 14, 225: 15, 256: 16, 289: 17, 324: 18, 361: 19}
keys = perfect_squares.keys()

def get_factors(n: int):
        if n in keys: return perfect_squares[n]
        factors = np.array([], int)
        for i in range(1, n+ + 1):
                if i != n and i != 1 and n % i == 0: factors = np.append(factors, [int(i), int(n/i)])
        if np.size(factors) == 0: return n
        return np.reshape(factors, (-1, 2))

def greatest_perfect_square(factors: np.ndarray):
        if type(factors) == int or type(factors) == np.int64: return factors
        squares = np.array([], int)
        for factor in factors:
                if factor[0] in keys: squares = np.append(squares, factor)
        if np.size(squares) == 0:
                return factors[np.argsort(factors[:, 0])[-1]]
        squares = np.reshape(squares, (-1, 2))
        return squares[np.argsort(squares[:, 0])[-1]]

def simplify(n: int):
        squared = greatest_perfect_square(get_factors(n))
        final = []
        if type(squared) == int or type(squared) == np.int64: final.append(squared)
        else: 
                for i in squared: 
                        f = simplify(i)
                        if not type(f) == str and i in keys: final += [f]
                        elif type(f) == list and len(f) > 1: final += f
                        elif i == i: final.append(f"√{f[0]}")
        return final

def finalize_expression(exp: list):
        sqrts, sum = [], 1
        for i in exp:
                if type(i) == list: sum *= i[0]
                if type(i) == str: sqrts.append(i)
        if sum == 1: return '*'.join(sqrts)
        return f"{sum}{'*'.join(sqrts)}"

def main():
        x = int(input())
        y = simplify(x)
        print(finalize_expression(y))
        
if __name__ == "__main__":
        main()
