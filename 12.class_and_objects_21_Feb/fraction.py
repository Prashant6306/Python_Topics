class Fraction:
  def __init__(self, x, y):
    self.numerator = x
    self.denominator = y

  def __str__(self):
    return '{}/{}'.format(
      self.numerator,
      self.denominator)

  def __add__(self, other):
    n = (self.numerator *
         other.denominator +
         other.numerator *
         self.denominator)
    d = (self.denominator *
         other.denominator)
    return Fraction(n, d)

  def __sub__(self, other):
    n = (self.numerator *
         other.denominator -
         other.numerator *
         self.denominator)
    d = self.denominator * other.denominator
    return Fraction(n, d)
  
  def __mul__(self, other):
    n = (self.numerator *
         other.numerator)
    d = (self.denominator *
         other.denominator)
    return Fraction(n, d)

  def __truediv__(self, other):
    n = (self.numerator *
         other.denominator)  # flip
    d = (self.denominator *
         other.numerator)    # flip
    return Fraction(n, d)

  def convert_to_decimal(self):
    return (self.numerator /
            self.denominator)

# ── Test ──────────────────
fr1 = Fraction(1, 2)
fr2 = Fraction(7, 11)
print(fr1)                 # 1/2
print(fr1 + fr2)           # 25/22
print(fr1 - fr2)           # -3/22
print(fr1 * fr2)           # 7/22
print(fr1 / fr2)           # 11/14
print(fr1.convert_to_decimal()) # 0.5