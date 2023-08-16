class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

num1 = ComplexNumber(3, 5)
num2 = ComplexNumber(2, 7)
sum_result = num1 + num2
print(sum_result)