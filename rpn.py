from argparse import ArgumentParser
import sys

def evaluate(postfixex):
    """Evaluates a given postfix expression, expects a string as the input.

    Args:
        postfixex (string): a string that contains a postfix expression

    Returns:
        float: The value of the post-fix expression evaluation
    """
    
    postfixex = postfixex.strip("\n")
    if len(postfixex) == 1:
        return postfixex
    stringlist = []
    for char in postfixex:
        if char == "+" or char == "-" or char == "/" or char == "*":
            op2 = float(stringlist.pop())
            op1 = float(stringlist.pop())
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
        elif char == ' ':
            pass
        else:
            stringlist.append(int(char))
    return result_new    
    

def main(filepath):
    """The function that read and prints the post-fix file and their solutions

    Args:
        filepath (string): A string that shows where the file that is being read lives.
        
    Returns:
        output: prints the postfix expression provided and the resulting value
    """
    
    with open(filepath, "r+", encoding="utf-8") as problems:
        for line in problems:
            line = line.strip("\n")
            sol = evaluate(line)
            print(f"{line} = {sol}")

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
