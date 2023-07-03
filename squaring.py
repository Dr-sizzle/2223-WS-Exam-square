from math import isqrt

def square_visual(number):
    val = str(number)
    num_chars = len(val)

    if (num_chars < 4):
        raise ValueError("Only numbers above 1000 supported")
    
    
    num_in_row = isqrt(num_chars)

    mylist = []
    k = 0
    for i in range(num_in_row):
        row = []
        for j in range(num_in_row):
            row.append(val[k])
            k = k + 1
        mylist.append(row)

    return mylist
