def binary_search(names, name):
    """binary search on a sorted list"""
    length = len(names)
    middle = length // 2
    while names[middle] != name: 
        if name < names[middle]:
            middle //=  2
        else:
            middle += (length - middle) // 2 
    return middle 
