import math
class Car:
    """A class that models a car.

    Attributes:
        x (float, optional): the x location of the car
            Default: 0
        y (float): the y location of the car
            Default: 0
        heading (float): the direction that the car is facing.
            Default: 0

    """
    def __init__(self, x = 0, y = 0, heading = 0):
        """A method that initializes the car

        Args:
            x (float, optional): the x location of the car
                Default: 0
            y (float, optional): the y location of the car
                Default: 0
            heading (float): the direction that the car is facing.
                Default: 0
        
        Side effects:
            Defines attributes `x`, `y`, `heading`.
        """
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
        """A method that turns the car by a given amount

        Args:
            degrees (float): The number of degrees that the car should turn
            
        Side effects:
            Changes the heading attribute of the object by turning it a 
            certain amount.
        """
        self.heading = ((self.heading + degrees) % 360)
        
    def drive(self, dist):
        """A method that moves the car by a certain amount

        Args:
            dist (float): The distance that the car is moving
            
        Side effects:
            Changes the x and y attributes of the object, therefore moving
            the car around.
        """
        head_rad = (self.heading)/360*math.pi
        self.x += dist*math.sin(head_rad)
        self.y -= dist*math.cos(head_rad)
        
def sanity_check():
    """A function that creates and manipulates a car object
    
    Side effects:
        Instantiate and manipulate a new car object. Prints out the new
        location and direction that the car is facing.
    """
    
    nyoom = Car()
    Car.turn(nyoom, 90)
    Car.drive(nyoom, 10)
    Car.turn(nyoom, 30)
    Car.drive(nyoom, 20)
    print(f"Location: {nyoom.x}, {nyoom.y}")
    print(f"Heading: {nyoom.heading}")
    
if __name__ == "__main__":
    sanity_check()
    