class Rational:
    # Helper function to compute the greatest common divisor (Euclidean Algorithm)
    def gcd(self, a, b):
        while b != 0:             # Keep looping until remainder becomes 0
            a, b = b, a % b       # Update a and b
        return abs(a)             # Return gcd as a positive number
    
    # Constructor (initializer) for Rational numbers
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:   # Denominator can't be 0 (undefined)
            raise ZeroDivisionError("The denominator can't be zero")
        
        # Simplify fraction by dividing numerator & denominator by gcd
        g = self.gcd(numerator, denominator)
        numerator //= g
        denominator //= g     

        # Keep denominator positive (-1/2 instead of 1/-2)
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        # Save values into object attributes
        self.numerator = numerator 
        self.denominator = denominator

    # Addition of two Rational numbers
    def __add__(self, other):
        if isinstance(other, Rational): 
            # Formula: a/b + c/d = (ad + bc) / bd
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator 
            return Rational(new_numerator, new_denominator)
            
    # Subtraction of two Rational numbers
    def __sub__(self, other):
        if isinstance(other, Rational):
            # Formula: a/b - c/d = (ad - bc) / bd
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator 
            new_denominator = self.denominator * other.denominator 
            return Rational(new_numerator, new_denominator)
            
    # Multiplication of two Rational numbers
    def __mul__(self, other):
        if isinstance(other, Rational):
            # Formula: (a/b) * (c/d) = (ac) / (bd)
            new_numerator = self.numerator * other.numerator 
            new_denominator = self.denominator * other.denominator 
            return Rational(new_numerator, new_denominator)
        
    # Division of two Rational numbers
    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("You can't divide by zero")
            # Formula: (a/b) ÷ (c/d) = (a/b) * (d/c)
            new_numerator = self.numerator * other.denominator 
            new_denominator = self.denominator * other.numerator 
            return Rational(new_numerator, new_denominator)

    # Equality check between two Rational numbers
    def __eq__(self, other):
        if isinstance(other, Rational):
            # Since we always store in reduced form, just compare num & den directly
            return self.numerator == other.numerator and self.denominator == other.denominator
        
    # String representation for printing
    def __str__(self):
        if self.denominator == 1:        # If denominator is 1, show only numerator
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"
        
