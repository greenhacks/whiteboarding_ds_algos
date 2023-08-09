"""Create a Vector class with x and a y attributes that represent component magnitudes in the x and y directions.

Your vectors should handle vector addition with an .add() method that takes a second vector as an argument and returns a new vector equal to the sum of the vector you call .add() on and the vector you pass in.

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y
        return Vector(new_x, new_y)