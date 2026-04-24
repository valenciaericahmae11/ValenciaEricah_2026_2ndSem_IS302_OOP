import math

class Shape_EIV:
    def area_EIV(self_EIV):
        pass  # Placeholder for polymorphism

class Rectangle_EIV(Shape_EIV):
    def __init__(self_EIV, width_EIV, height_EIV):
        self_EIV.width_EIV = width_EIV
        self_EIV.height_EIV = height_EIV

    def area_EIV(self_EIV):
        return self_EIV.width_EIV * self_EIV.height_EIV

class Circle_EIV(Shape_EIV):
    def __init__(self_EIV, radius_EIV):
        self_EIV.radius_EIV = radius_EIV

    def area_EIV(self_EIV):
        return math.pi * self_EIV.radius_EIV ** 2

class Triangle_EIV(Shape_EIV):
    def __init__(self_EIV, base_EIV, height_EIV):
        self_EIV.base_EIV = base_EIV
        self_EIV.height_EIV = height_EIV

    def area_EIV(self_EIV):
        return 0.5 * self_EIV.base_EIV * self_EIV.height_EIV

# Example usage
rectangle_EIV = Rectangle_EIV(10, 5)
circle_EIV = Circle_EIV(5)
triangle_EIV = Triangle_EIV(8, 6)

print(f"Rectangle Area: {rectangle_EIV.area_EIV()}")
print(f"Circle Area: {circle_EIV.area_EIV():.1f}")
print(f"Triangle Area: {triangle_EIV.area_EIV()}")

