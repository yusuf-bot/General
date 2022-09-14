import random
import time
def binary_search(l,target,low,high):
    if low==None:
        low=0
    if high==None:
        high=len(l)-1

    midpoint=(high-low)//2
    if target==midpoint:
        return midpoint
    elif target<midpoint:
        return binary_search(l, target, None, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, None)


