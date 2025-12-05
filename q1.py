def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    x_is_int = isinstance(x, int)
    y_is_int = isinstance(y, int)
    #x_is_float = isinstance(x, float)
    #y_is_float = isinstance(y, float)
    #eschewing string isnumeric logic as doesn't seem required for this task
    if x_is_int and y_is_int:
        print (f"x = {y}, y = {x}")
    else
        return -1




# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
error_check_1 = swap ("Apple", 10)
# - 9, 17
error_check_2 = swap (9,17)
