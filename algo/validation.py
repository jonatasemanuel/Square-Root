@staticmethod
def check_int(user_input):

    try:
        if isinstance(user_input, int):
           return True  

    except TypeError or SyntaxError:
            if isinstance(user_input, float):
                print('\nPlease insert a integer number \n')
                return False
                