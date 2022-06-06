from algo.search import Search

find = Search()

if __name__ == '__main__':
    
    user_in = print(input('Insert a integer number to ' 
                          'square root calculator: '))

    find.square_root(user_in)
    # find.square_root("gy")
    # find.square_root(11)
    # find.square_root(11g)