from algo.search import Search
from algo.validation import check_int


find = Search()


if __name__ == '__main__':

    while True:
        try:
            user_in = int(input('\n\033[33;1mInsert a number to '
                                'square root calculator:\033[0;0m '))

            if check_int(user_in):
                find.square_root(user_in)

        except (ValueError, SyntaxError):
            print('\033[31;1mNot is a integer number !\033[0m\n')
        else:
            cont = str(input('\033[36;1mWould you like a calculation '
                             'again ? \n[ y / n]:\033[0;0m ').lower())
            if cont not in "y yes":
                print('\n\033[31;1mExiting...\033[0m')
                break
        
            