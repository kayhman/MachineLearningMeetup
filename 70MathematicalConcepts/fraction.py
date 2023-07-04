# Definition of a class managing fractions
class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # Implementation of addition
    def __add__(self, b):
        if self.den == b.den:
            return Fraction(self.num + b.num, self.den)
        else:
            return Fraction(self.num * b.den + b.num * self.den,
                            self.den * b.den)

    # Implementation of subtraction
    def __sub__(self, b):
        if self.den == b.den:
            return Fraction(self.num - b.num, self.den)
        else:
            return Fraction(self.num * b.den - b.num * self.den,
                            self.den * b.den)

    # Implementation of multiplication
    def __mul__(self, b):
        return Fraction(self.num * b.num, self.den * b.den)

    # Implementation of division
    def __truediv__(self, b):
        return Fraction(self.num * b.den, self.den * b.num)

    def __str__(self):
        return f"{self.num}/{self.den}"


a = Fraction(1, 2)
print(a)
#> 1/2
b = Fraction(1, 4)
print(b)
#> 1/4
c = a + b
print(c)
#> 6/8
d = a - b
print(d)
#> 2/8
e = a * b
print(e)
#> 1/8
f = a / b
print(f)
#> 4/2


# Finding the greatest common
# denominator using Euclid's algorithm.
def gcd(d, n):
    if d == n:
        return d
    if d > n:
        return gcd(d - n, n)
    else:
        return gcd(d , n - d)

# Testing on two pairs of numbers.
print(gcd(18, 12))
#> 6
print(gcd(217 * 19, 456 * 19))
#> 19