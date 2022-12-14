from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}


class PhoneNumber:
    
    """
    Creates a phone number objects
    
    Attributes:
        area_code(str): A 3-digit string representing the area code
        exchange_code(str): A 3-digit string representing the exchange code
        line_number(str): A 4-digit string representing the line number
    """
    
    def __init__(self, phnum):
        """Create a phone number objects

        Args:
            phnum (str/int): A string or integer representing a phone number

        Raises:
            TypeError: If the input is not an int or str
            ValueError: If the phone number is not valid for various reasons
            
        Side Effects:
            Creates a phone number object
        """
        # Convert the phone number to a string if it's an integer
        if type(phnum) == int:
            phnum = str(phnum)
        # If the stype is not a string now, it is not valid
        try:
            if type(phnum) != str:
                raise TypeError
        except TypeError:
            print(f"I'm sorry,the number {phnum} is not valid")
        # Remove any characters that are not words or between 0-9
        phnum = re.sub(re.compile(r"[\W_]"),"",phnum)
        # Look through number and replace any letters with their dictionary match
        for l in phnum:
            if l in list(LETTER_TO_NUMBER.keys()):
                phnum = phnum.replace(l,LETTER_TO_NUMBER[l])
        if phnum[0] == '1':
            phnum = phnum[1:]
        try:
            if len(phnum) != 10:
                raise ValueError
            elif phnum[0] == 0 or phnum[0] == 1 or re.match('11',phnum[1:2]):
                raise ValueError
            # Error check for exchange code conditions
            elif phnum[3] == 0 or phnum[3] == 1 or re.match('11',phnum[4:5]):
                raise ValueError
        except ValueError:
            phnum = "0000000000"
        self.area_code = phnum[0:3]
        self.exchange_code= phnum[3:6]
        self.line_number= phnum[6:10]
    
    def ___int__(self):
        """Create a string of the full phone number & return the integer version of it
        """
        inrep = str(self.area_code) + str(self.exchange_code) + str(self.line_number)
        return inrep
    
    def __repr__(self):
        """Create a formal representation of the full phone number
        """
        return f"Phone Number({(self.area_code + self.exchange_code + self.line_number)!r})"
    
    def __str__(self):
        """Create an informal representation of the full phone number
        """
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}"
    
    def __lt__(self, other):
        """Create one string of the phone number
        """
        num1 = self.area_code + self.exchange_code + self.line_number
        num2 = other.area_code + other.exchange_code + other.line_number
        # compare strings
        return True if num1 < num2 else False
            
            
def read_numbers(filename):
    """Reads phone numbers into list

    Args:
        filename (str): A string representing a file with phone numbers

    Returns:
        List[Tuple(Name,Phone Number)]: A list of all the phone numbers and organizations
    """
    with open(filename, 'r', encoding="utf-8") as op:
        alist = []
        for line in op:
            patt = re.compile(r"^(?P<org>.+)\t(?P<num>.+)")
            match = patt.search(line)
            org = match.group("org")
            pnum = PhoneNumber(match.group("num"))
            if pnum.area_code != "000":
                alist.append((org,pnum))
    alist.sort(key = lambda f: f[1])
    print(alist)
    return alist
    
    
def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
