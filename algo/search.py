class Search:

    def __init__(self) -> None:
        pass

    def square_root(self, find_root, begin=0, end=None):

        arr = list (range(0, find_root))
        if end is None:
            end = len(arr) - 1
        if begin <= end:
            mid = (begin + end) // 2
            if (mid * mid) == find_root:
                print(f'\n√{find_root} → {mid}\n')
                return mid
            elif (mid * mid) < find_root:
                return self.square_root(find_root, mid+1, end)
            else:
                return self.square_root(find_root, begin, mid-1) 
        else:
            print(f'\n√{find_root} → No square root\n')
    # else:
    #     print('Not is a integer number')
