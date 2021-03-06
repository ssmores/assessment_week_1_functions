"""Skills function assessment for Stefanie.

This is the fucntions skills assessment for Stefanie, for Summer 2016, Grace 
cohort for Hackbright.
"""


# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_total_item_cost(state_abbreviation, item_cost, tax_amount=0.05):
    """Calculate cost of an item, after taxes. Default tax is 5%, unless state is CA.

    Takes the tax amount (optional, but is defaulted to 5%), the state the
    purchase is made in, and the cost of the item.

    >>> calculate_total_item_cost('TX', 5)
    5.25

    >>> calculate_total_item_cost('CA', 5, 0.06)
    5.35
    """

    total_cost = 0

    if type(tax_amount) == int:
        tax_amount = float(tax_amount / 100)
    elif state_abbreviation.lower() == "ca":
        total_cost = float(item_cost) + float(item_cost * 0.07)
    else:
        total_cost = float(item_cost) + float(item_cost * tax_amount)

    return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):
    """Returns True if argument is "strawberry", "cherry", or "blackberry". 

    Takes a variable, evaluates if it's "strawberry", "cherry", or "blackberry",
    and returns a boolean value.

    >>> is_berry("blueberry")
    False

    >>> is_berry('strawberry')
    True
    """

    list_of_acceptable_fruit = ['strawberry', 'cherry', 'blackberry']

    return fruit_name in list_of_acceptable_fruit

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit_name):
    """Calculate shipping cost, based on status of is_berry function."

    If is_berry returns True, calculates costs as 0.
    If is_berry returns False, calculates costs as 5.

    >>> shipping_cost('strawberry')
    0

    >>> shipping_cost("apple")
    5
    """

    if is_berry(fruit_name) == True:
        return 0
    else:
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(hometown_name):
    """Evaluates if the argument is the same as my actual hometowm.

    Determines if the argument provided is the same as my hometown.

    >>> is_hometown('Austin')
    False

    >>> is_hometown("Piedmont")
    True
    """

    actual_hometown = 'piedmont'

    return hometown_name.lower() == actual_hometown
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """Takes first name and last name as arguments, and returns one string.

    Takes the arguments first_name and last_name, and returns them as one string.

    >>> full_name('bob', 'dole')
    'bob dole'
    """

    return first_name + " " + last_name

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(hometown_name, first_name, last_name):
    """Prints a messaged based on your hometown.

    Takes the is_hometown and full_name functions and creates a greeting.

    >>> hometown_greeting("Piedmont", 'stefanie', 'moy')
    Hi, stefanie moy, we're from the same place!
    """

    hometown_name.lower()

    if is_hometown(hometown_name) == True:
        print "Hi, " + full_name(first_name, last_name) + ", we're from the same place!"
    else:
        print "Hi, " + full_name(first_name, last_name) + ", where are you from?"


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.



# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print