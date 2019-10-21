#!/usr/bin/env python
import math
def myround(numtoRound):
    """
    Over-write python's default rounding behavior. 
    For equally close multiples (ie 0.5) the function rounds up to the nearest integer.     
    Arguments:
        numtoRound {double} -- value to round. 
    Returns:
        [int] -- value rounded to nearest integer (with 0.5 rounded up)
    """
    if numtoRound - math.floor(numtoRound >= 0.5):
        return int(math.ceil(numtoRound))
    else:
        return int(math.floor(numtoRound))
