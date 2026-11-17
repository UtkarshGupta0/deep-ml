def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if(len(a[0]) != len(b)):
        return -1
    b_cols = list(zip(*b))
    return [[sum((x*y) for x , y in zip(row,col)) for col in b_cols] for row in a]