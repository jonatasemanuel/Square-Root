from algo.search import Search
from algo.validation import check_int


find = Search()


if __name__ == '__main__':
    try:
        user_in = int(input('Insert a number to square root calculator: '))

        if check_int(user_in):
            find.square_root(user_in)

    except (ValueError, SyntaxError):
        print('Not is a integer number !')
        print('Please insert a integer number')
        