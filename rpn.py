from argparse import ArgumentParser
import sys


def evaluate(expr):
    """Evaluates a postfix expression.
    
    Args:
        expr (str): a postfix expression to be evaluated.
    
    Returns:
        float: the result of the expression.
    """
    stack = []
    for token in expr.split():
        if token in ["+", "-", "*", "/"]:
            num2 = stack.pop()
            num1 = stack.pop()
            value = (num1 + num2 if token == "+" else
                     num1 - num2 if token == "-" else
                     num1 * num2 if token == "*" else
                     num1 / num2)
            stack.append(value)
        else:
            stack.append(float(token))
    return stack.pop()


def main(filepath):
    """Read postfix expressions from a file and print their results.
    
    Args:
        filepath (str): path to a file containing one postfix expression per
            line.
    
    Side effects:
        Print to stdout.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(f"{line} = {evaluate(line)}")


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
