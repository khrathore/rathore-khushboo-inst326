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
        # Convert the phone number to a string if it's an integer
        if type(phnum) == int:
            phnum = str(phnum)
        # If the stype is not a string now, it is not valid
        try:
            if type(phnum) != str:
                raise TypeError
        except TypeError:
            print(f"I'm sorry, the number {phnum} is not valid")
        # Remove any characters that are not words or between 0-9
        phnum = re.sub(re.compile(r"[\W_]"),"",phnum)
        # Look through number and replace any letters with their dictionary match
        for l in phnum:
            patt = re.compile(r"[A-Z]")
            if not(re.match(patt, l)==None):
                l=LETTER_TO_NUMBER.get(l)
        # Conditional that removes a leading 1
        if phnum[0] == 1:
            phnum = phnum[1:]
        # Error check if the number is too long
        try:
            if len(phnum) != 10:
                raise ValueError
            # Error check for area code conditions
            elif phnum[0] == 0 or phnum[0] == 1 or re.match('11',phnum[1:2]):
                raise ValueError
            # Error check for exchange code conditions
            elif phnum[3] == 0 or phnum[3] == 1 or re.match('11',phnum[4:5]):
                raise ValueError
        except ValueError:
            print(f"I'm sorry, the number {phnum} is not valid")
        # Assign attributes
        self.area_code = phnum[0:2]
        self.exchange_code= phnum[3:5]
        self.line_number= phnum[6:9] #hehe nice
    
    def ___int__(self):
        # Create a string of the full phone number & return the integer version of it
        phnum = self.area_code + self.exchange_code + self.line_number
        return int(phnum)
    
    def __repr__(self):
        return f"Phone Number({(self.area_code + self.exchange_code + self.line_number)!r}"
    
    def __str__(self):
        return f"({self.area_code}) {self.exchange_code} {self.line_number}"
    
    def __lt__(self, other):
        # combine the full number into one string
        num1 = self.area_code + self.exchange_code + self.line_number
        num2 = other.area_code + other.exchange_code + other.line_number
        # compare strings
        return True if num1 < num2 else False
            
            
def read_numbers(filename):
    with open(filename, 'r', encoding="utf-8") as op:
        alist = []
        for line in op:
            patt = re.compile(r"^(?P<org>.+)\t(?P<num>.+)")
            match = patt.search(line)
            org = match.group("org")
            pnum = PhoneNumber(match.group("num"))
            alist.append((org,pnum))
    return alist.sort(key = lambda f: f[1])
    
    
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
