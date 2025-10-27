#Sum and difference
num_a = 5
num_b = 2
sum = num_a + num_b
difference = num_a - num_b

# Float division
division = num_a / num_b

#Integer division
division = num_a // num_b

# Powerful operations
multiply_numbers = num_a * num_b
power = num_a ** num_b
remainder = num_a % num_b

#Find average
average = (num_a + num_b) / 2

#Area of a circle
def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = round(math.pi * radius**2, 2)
    return circle_area

#Area of an equilateral triangle
def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = round((math.sqrt(3) / 4) * side_length ** 2)
    return triangle_area

#Calculate discriminant
def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    print(discriminant)
    return discriminant

#Calculate hypotenuse length
def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a**2 + b**2)
    return c

#Calculate cathetus length
def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c**2 - a**2)
    return b

