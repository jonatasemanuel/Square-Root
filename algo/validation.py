@staticmethod
def check_int(user_input):

    try:
        if isinstance(user_input, int):
           return True  

    except TypeError:
            if isinstance(user_input, float):
                print('\nPlease insert a integer number \n')
                return False
                
    except SyntaxError:
            print('Just number')
            return False