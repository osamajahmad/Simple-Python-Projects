import pytest
from polygon import Polygon

"""Checking if the polygon object is initialized correctly with valid name and sides"""
def test_polygon_initialization():
    triangle = Polygon("Triangle", [3, 3, 3])           #Creates the polygon with a name and side
    assert triangle.get_name() == "Triangle"            #Checks if the name matches 
    assert triangle.get_sides() == [3, 3, 3]            #Checks if the sides match


"""Testing the getters for name and sides"""
def test_getters():
    square = Polygon("Square", [4, 4, 4, 4])            #Creates a polygon with a name and sides
    assert square.get_name() == "Square"                #Checks if its the same
    assert square.get_sides() == [4, 4, 4, 4]           #Checks if they match


"""Testing the setters for name and sides"""
def test_setters():
    pentagon = Polygon("Pentagon", [5, 5, 5, 5, 5])     #Create sa polygon
    pentagon.set_name("Hexagon")                        #Sets the name / changes it
    pentagon.set_sides([6, 6, 6, 6, 6, 6])              #Same with sides
    assert pentagon.get_name() == "Hexagon"             #Checks if its the same
    assert pentagon.get_sides() == [6, 6, 6, 6, 6, 6]   #Checks if it matches


"""Testing that set_sides does not accept 0 or lesser."""
def test_set_sides_invalid():
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])  # Polygon with sides
    try:
        hexagon.set_sides([6, -6, 6, 6, 6, 6])        # Tries to set invalid value
        assert False, "Expected ValueError was not raised"  # Fail the test if no exception occurs
    except ValueError:
        pass  # Exception was correctly raised
    assert hexagon.get_sides() == [6, 6, 6, 6, 6, 6]  # Makes sure it remains unchanged

"""Test to verify that both class objects are equal with respect to type,name and sides"""
def test_polygon_equality():
    triangle = Polygon("Triangle", [3, 3, 3])         
    triangle2 = Polygon("Triangle", [3, 3, 3])         
    assert triangle == triangle2                        #Compare polygons with same name and sides


"""Test to verify class objects with different sides and/or name are unequal"""
def test_polygon_inequality():
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4, 4, 4, 4])            #Object with different name and sides
    triangle2 = Polygon("Triangle", [7, 3, 3])          #Object with same name but different sides
    square2 = Polygon ("Squaare",[4, 4 ,4 ,4 ])         #Object with different name but same sides
    triangle3 = Polygon("Triangle", [3, 3, 3])          #Object with same name and same sides
    assert triangle != square
    assert triangle != triangle2
    assert square != square2
    assert triangle == triangle3

"""Test string representation of a Polygon object"""
def test_polygon_str():
    triangle = Polygon("Triangle", [3, 3, 3])  # Create a triangle polygon
    assert str(triangle) == "Triangle with sides: [3, 3, 3]"  # Verify string representation


"""Test to calculate the circumference of different polygons"""
def test_calculate_circumference_triangle():
    
    #Test calculate_circumference for a triangle
    triangle = Polygon("Triangle", [3.0, 4.0, 5.0])
    assert triangle.calculate_circumference() == pytest.approx(12.0)

    #Test calculate_circumference for a square
    square = Polygon("Square", [4.0, 4.0, 4.0, 4.0])
    assert square.calculate_circumference() == pytest.approx(16.0)
    
    #Test calculate_circumference for a rectangle
    rectangle = Polygon("Rectangle", [5.0, 3.0, 5.0, 3.0])
    assert rectangle.calculate_circumference() == pytest.approx(16.0)