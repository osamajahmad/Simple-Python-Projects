"""Constructor method class, with two attributes which are name and side"""

class Polygon:
    def __init__(self, name, sides):
        self.name = name
        for s in sides:
            if s <= 0:
                raise ValueError ("Enter positive values greater than 0") #Checks if all elements in side are positive numbers, if all sides are positive is assigns self.the value of side
        self.sides = sides

    """Returns the name of the polygon"""
    def get_name(self):
        return self.name  


    """Sets the name attribute of the object"""
    def set_name(self, name):
        self.name = name     


    """Returns the sides"""
    def get_sides(self):
        return self.sides   


    """Sets the sides attribute"""
    def set_sides(self, sides):
        for s in sides:
            if s <= 0:
                raise ValueError ("Enter positive values greater than 0")
        self.sides = sides
        

    """Checks if two class objects are equal in terms of type, name and sides """
    def __eq__(self, other):
        if type(self) == type(other):
            return self.name == other.get_name() and self.sides == other.get_sides()
        else: 
            return False
        

    """Checks if two class objects are unequal and returns logical negation of eq() in the case it is; They are considered unequal if they have different types, name or sides."""
    def __ne__(self, other):
        return not self.__eq__(other)


    """Return the string representation of the polygon with its name and sides."""
    def __str__(self):
        return f"{self.name} with sides: {self.sides}"


    """Calculate and return the circumference of the polygon as the sum of all sides."""
    def calculate_circumference(self):
        return sum(self.sides)


"""Main function that calls the class and prints the string representation and the cricumference of the polygons"""
def main():
    t1 = Polygon("Triangle",[3.0 , 0.0, 9.0])
    s1 = Polygon("Square",[4.0 , 4.0, 4.0, 4.0])
    h1 = Polygon("Hexagon",[6.0 , 4.0, 1.0, 9.0, 3.0, 2.0])
    print("\n")
    print (t1)
    print(f"Area of {t1.get_name()} is {t1.calculate_circumference()} \n")
    print(s1)
    print(f"Area of {s1.get_name()} is {s1.calculate_circumference()} \n")
    print (h1)
    print(f"Area of {h1.get_name()} is {h1.calculate_circumference()} \n")



if __name__ == "__main__":
    main()