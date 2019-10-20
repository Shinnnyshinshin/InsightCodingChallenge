#!/usr/bin/env python
import math

# this is for the strange way that python 3.7 does the rounding
def myround(numtoRound):
    if numtoRound - math.floor(numtoRound >= 0.5):
        return int(math.ceil(numtoRound) + 10000)
    else:
        return int(math.floor(numtoRound) + 10000)
