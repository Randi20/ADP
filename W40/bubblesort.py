from issorted import issorted

def bubblesort(lst):
    """ Computes a bubble-sort

    >>> bubblesort([5, 2, 3])
    [2, 3, 5]
    >>> bubblesort([15, 10, 9])
    [9, 10, 15]
    >>> bubblesort([])
    []
    >>> bubblesort([1])
    [1]
    """
    n = len(lst)
    
    lst = list(lst)
    
    if len(lst) <= 1:
        return lst
    
    changes = True
    
    while changes:
        changes = False
        
        for i in range(n-1):
            for j in range(0, n-i-1):
            
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    change = True
    return lst
        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("Den er færdig")
