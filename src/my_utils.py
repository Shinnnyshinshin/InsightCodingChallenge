#!/usr/bin/env python
#import math

# this is for the strange way that python 3.7 does the rounding
def myround(numtoRound):
    if numtoRound - int(numtoRound) >= 0.5:
        return int(numtoRound) + 1
    else:
        return int(numtoRound)