from  algo.validation import check_int

class Search:

    def __init__(self) -> None:
        pass

    def square_root(self, find_root, begin=0, end=None):
        # super(Search).__init__(find_root, begin=0, end=None)
    
        if check_int(find_root):
        
            arr = [x for x in range(0, find_root)] 

            if end is None:
                end = len(arr) - 1
            
            if begin <= end:
                mid = (begin + end) // 2
                
                if (mid * mid) == find_root:
                    print(f'\n√{find_root} → {mid}\n')
                    return mid
                elif (mid * mid) < find_root:
                    self.square_root(find_root, mid+1, end)
                else:
                    self.square_root(find_root, begin, mid-1)
            else:
                print(f'\n√{find_root} → No square root\n')

        # return None