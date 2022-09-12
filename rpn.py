from argparse import ArgumentParser
import sys

def evaluate(postfixex):
    postfixex.strip()
    stringlist = []
    for char in postfixex:
        if char == '+' or '-' or '/' or '*':
            op2 = int(stringlist.pop())
            op1 = int(stringlist.pop())
            if char == '+':
                result_new = op1 + op2
                stringlist.append(result_new)
            elif char == '-':
                result_new = op1 - op2
                stringlist.append(result_new)
            elif char == '/':
                result_new = op1/op2
                stringlist.append(result_new)
            else:
                result_new = op1*op2
                stringlist.append(result_new)
        else:
            stringlist.append(char)
    
def main(filepath):
    

# Replace this comment with your implementations of the evaluate() and main()
# functions.


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
