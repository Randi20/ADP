def merge(xs, ys):
    """ Merges two sorted lists

    >>> merge([], [])
    []
    >>> merge([], [1,2])
    [1, 2]
    >>> merge([1,2], [])
    [1, 2]
    >>> merge([1,3], [2,4])
    [1, 2, 3, 4]
    """
    # recursiv
    if not xs:
        return ys
    if not ys:
        return xs
    x, *xs_ = xs
    y, *ys_ = ys
    if x < y: return [x] + merge(xs_, ys)
    else: return [y] + merge(xs, ys_)
    
    # iterative
    
    i = 0
    j = 0
    while True.
        if j > len(ys) or xs[i] < ys[j]:
        
            merged.append(xs[i])
            i += 1
        elif j < len(ys):
            merged.append(ys[j])
            j += 1
        else:
            break


if __name__ == "__main__":
    import doctest
    doctest.testmod()
