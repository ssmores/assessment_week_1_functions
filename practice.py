"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

    >>> nums = [1, 2]
    >>> add_new_number(5, nums)
    >>> nums
    [1, 2, 5]

    
    """
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".
def hello_world():
    """Prints "Hello World".

    This function takes no arguments, and will print out "Hello World". 
    """
    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Prints a greeting to the user's name.

    This will take the user's name, and greets them with "Hi" and their name.
    """
    print "Hi " + name


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(int1, int2):
    """Multiplies two integers.

    Takes two integers, and multiplies them together.
    """
    print int1 * int2


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(string_to_repeat, integer_to_repeat_by):
    """Repeats a string by the number of an integer.

    This will print out a string the number of times specified by the integer.
    """
    print string_to_repeat * integer_to_repeat_by


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(sign_int):
    """Prints out if integer is greater than 0, less than 0, or 0.

    Prints out description of if the integer is greater than 0, less than 0, or is 0.
    """

    if type(sign_int) == int:
        if sign_int > 0:
            print "Higher than 0"
        elif sign_int < 0:
            print "Lower than 0"
        elif sign_int == 0:
            print "Zero"
    else:
        print "This is not an integer."


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(three_integer):
    """If integer is divisible by three, returns True, otherwise returns False.

    Takes an integer, and returns a value of True if it's divisible by three. 
    It returns False if it's not divisible by three.
    """
    return three_integer % 3 == 0


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(spaces_string):
    """Returns the number of spaces as available in the sentence.

    Takes a sentence string, and returns the nmber of spaces in the string.
    """

    count_of_spaces = 0
    for space in spaces_string:
        if space == " ":
            count_of_spaces +=1

    return count_of_spaces


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip_percent=15):
    """This will calculate the cost of a meal, provided the meal cost and tax.

    Takes the meal price, and adds the tip amount.  The tip is defaulted to 15%, 
    but can be provided as the parameter if it is not 15%.
    """

    total_cost = meal_price + (meal_price * tip_percent)
    return total_cost
    

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


