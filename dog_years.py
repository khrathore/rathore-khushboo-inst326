import random as rand
import sys

def dog_years(dog_age):
    """
    This is a function to calculate the age of a dog in dog years

    Args:
        dog_age (integer): The provided number that tells the program how old the dog is in human years

    Raises:
        ValueError: This error happens if the age is negative

    Returns:
        int: The age of the dog in dog years
    """
    if dog_age < 0:
        raise ValueError("Age cannot be a negative number")
    elif dog_age == 0:
        human_age = 0
    elif dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 24
    else:
        human_age = 24 + (dog_age-2)*5
    return human_age

#In-class example
def dog_years(dog_age):
    human_age = 0
    if dog_age < 0:
        raise ValueError("Age cannot be a negative number")
    if dog_age > 0:
        human_age += 15
    if dog_age > 1:
        human_age += 9
    if dog_age > 2:
        human_age += (dog_age - 2) * 5
    return human_age

if __name__ == "__main__":
    #Thing in index 0 is the name of our program, 1 is a string
    dog_age = int(sys.argv[1])
    print(dog_years(dog_age))

#Run the program using python3 dogyrs.py on Mac, python dogyrs.py on Windows

#doggy = rand.randint(-10, 20)
#print(dog_years(doggy))

