from argparse import ArgumentParser
import re
import sys

class Address:
    """
    This class creates an address object and has methods to use on those objects.
    
    Attributes:
        address (str): The full address of the home
        house_number (str): the house's number
        street (str): The street the house is on
        city (str): The city the house is in
        state(str): The state the house is in
        zip(str): The zip code of the home
        
    Methods:
        __repr__(): A function that returns a formal representation of the Address object
    """
    
    def __init__(self, address):
        """
        Create an instance of the Address class

        Args:
            address (string): The full address of the location
            
        Side effects:
            Creates an address object with multiple attributes and creates a regex pattern
            
        Raises:
            ValueError if the pattern does not match the address
        """
        patt = re.compile(r"""
            (?x)
            ^(?P<house_number>\S+)
            \s
            (?P<street>[^,]+)
            ,\s
            (?P<city>.*)
            \s
            (?P<state>[A-Z]{2})
            \s
            (?P<zip>\d{5})"""
            )
        match = patt.search(address)
        if match == None:
            raise ValueError("The address string could not be parsed.")
        else:
            self.address = match.group(0)
            self.house_number = match.group("house_number")
            self.street = match.group("street")
            self.city = match.group("city")
            self.state = match.group("state")
            self.zip = match.group("zip") 

    def __repr__(self):
        """Return a formal representation of the Address object."""
        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )

def read_addresses(filepath):
    """A function that reads the addresses and converts them into a new list of Address objects

    Args:
        filepath (string): Path to the file that contains all of the addresses

    Returns:
        list: A list of the addresses in the form of address objects
    """
    with open(filepath, 'r', encoding="utf-8") as adds:
        alladd = []
        for line in adds:
            line = line.strip()
            addy = Address(line)
            alladd.append(addy)
    return alladd
        

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
