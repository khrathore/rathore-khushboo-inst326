"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys

def get_min_payment(principal, annrate, mortyrs = 30, payr = 12):
    """ This function determines the minimum payment (as an integer) per month that can be made to the mortgage in 
    order to ensure that it is paid off within a specified thime. The function has two option arguments that represent
    standard mortgage length and payment intervals.

    Args:
        principal (integer): The initial amount of the mortgage
        annrate (float): The annual interest rate of the mortgage
        mortyrs (int, optional): The number of years that the mortgage goes for. Defaults to 30.
        payr (int, optional): The number of payments per year for the mortgage. Defaults to 12.

    Returns:
        int: The minimum payment that can be made to each installment the mortgage in order to pay it off on time
    """
    min_mort = ((principal * (annrate/payr)) * ((1 + annrate/payr) ** (mortyrs * payr))) / (((1 + annrate/payr) ** (mortyrs * payr)) - 1)
    wholemin = math.ceil(min_mort)
    return wholemin

def interest_due(balance, annrate, payr = 12):
    """ This function determines the interest that is due on the current mortgage balance and returns it as a float.

    Args:
        balance (int): The current balance of the mortgage
        annrate (float): The provided annual interest rate of the mortgage
        payr (int, optional): The number of payments per year for the mortgage. Defaults to 12.

    Returns:
        float: The interest due on the current balance of the mortgage
    """
    interest = balance * (annrate/payr)
    return interest

def remaining_payments(balance, annrate, targpay, payr = 12):
    """ This function determines the amount of payments that will be required to pay off a full mortgage under terms outlines

    Args:
        balance (int): The current balance of the mortgage
        annrate (float): The provided annual interest rate of the mortgage
        targpay (float): The amount that the payer wants to pay for the mortgage each installment. Will be set to the minimum
        payment if not outlined
        payr (int, optional): The number of payments per year for the mortgage. Defaults to 12.

    Returns:
        int: The amount of installments required to pay off the full mortgage
    """
    installments = 0
    while (balance > 0):
        interest = interest_due(balance, annrate, payr)
        payleft = targpay - interest
        balance = balance - payleft
        installments = installments + 1
    return installments

def main(principal, annrate, mortyrs = 30, payr = 12, targpay = None):
    """_summary_

    Args:
        principal (integer): The initial amount of the mortgage
        annrate (float): The annual interest rate of the mortgage
        mortyrs (int, optional): The number of years that the mortgage goes for. Defaults to 30.
        payr (int, optional): The number of payments per year for the mortgage. Defaults to 12.
        targpay (float): The amount that the payer wants to pay for the mortgage each installment. Defaults to NONE
        
    Side Effects:
        Prints out the minimum mortgage payment
        Print out a phrase if the target payment that has been input is lower than the minimum payment.
        When the program finishes running, print out the amount of payments and what the payment will 
        be to pay off the mortgage within the given time.
    """
    min_pay = get_min_payment(principal, annrate, mortyrs, payr)
    print(f"The minimum payment for your mortgage is {min_pay}")
    if targpay == None:
            targpay = min_pay
    if targpay < min_pay:
        print(f"I'm sorry, your target monthly payment of {targpay} is lower than your minimum possible monthly payment of {min_pay}. Please try again.")      
        sys.exit
    else:
        paymentsneeded = remaining_payments(principal, annrate, targpay, payr)
        print(f"If you make payments of {targpay}, you will pay off the mortgage in {paymentsneeded} payments.")    

def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
