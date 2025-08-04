#solution to 6.1


def convert_distance(distance, unit = "km"):
    if unit != "km":
        return distance*0.621371
    else:
        return distance*1.60934

'''2 - Write a function called sum_coordinates that accepts a variable number of coordinate pairs (tuples) as input. 
The function should return the sum of all
the latitude and longitude values provided.'''

def sum_coordinates(coord_list):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coord_list):
        raise ValueError("All elements must be tuples of two numbers")
    return [x + y for (x, y) in coord_list]

#Giving one tuple - as a list
cord = [(23,43)]
print(f"the sum of coordinates {sum_coordinates(cord)} and type is {type(cord)}")

#Giving a list of tuples
import random
def gen_rand_tuples(n, min_val = 0, max_val = 100):
    return[(random.randint(min_val,max_val),random.randint(min_val,max_val)) for _ in range(n)]

coord_list = gen_rand_tuples(15)

#Use your defined function sum_coordinates
print(f"The sum of all random coordinates are: {sum_coordinates(coord_list)}")

'''Extending the point class'''

class Point:
    def __init__(self, lat, long, name=None):
        self.lat = lat
        self.long = long
        self.name = name

    def __str__(self):
        return f"{self.name or 'Point'} ({self.lat}, {self.long})" 
    
    def distance_to(self, other_point):
        return haversine(
            self.latitude, self.longitude, other_point.latitude, other_point.longitude)

    def move(self,mov_x,mov_y):
        self.lat += mov_y
        self.long += mov_x

# Example usage
point1 = Point(35.6895, 139.6917, "Tokyo")
print(point1)

#Use move function 

point1.move(1,2)

print(f"After moving in a certain direction we have Point new coordinates : {point1}")