# Rational Number Class in Python  

## Overview  
This project implements a `Rational` class that represents fractions (rational numbers) in simplified form.  
It supports arithmetic operations such as addition, subtraction, multiplication, division, and equality comparison.  

---

## Features  
- Stores rational numbers in reduced form using **GCD (Euclidean Algorithm)**.  
- Ensures denominator is always positive.  
- Prevents invalid cases such as division by zero.  
- Operator overloading for natural arithmetic (`+`, `-`, `*`, `/`).  
- Equality check (`==`) between fractions.  
- Clean string representation (`__str__`).  

---

## Example Usage  

```python
from rational import Rational  

# Creating rational numbers
r1 = Rational(2, 4)   # Simplified to 1/2
r2 = Rational(3, 6)   # Simplified to 1/2
r3 = Rational(5, 2)   # 5/2

# Addition
print(r1 + r3)   # 12/4 → 3

# Subtraction
print(r3 - r1)   # 8/4 → 2

# Multiplication
print(r1 * r2)   # 1/4

# Division
print(r3 / r1)   # 10/2 → 5

# Equality
print(r1 == r2)  # True
