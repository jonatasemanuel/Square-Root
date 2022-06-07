@staticmethod
def check_int(user_input):
    """Check if user input is a integer number.

    Args:
        user_input (input)): Data to check

    Returns:
        int: integer number typed
    """
    if isinstance(user_input, int):
        return user_input
    return False    