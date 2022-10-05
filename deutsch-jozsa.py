# func is a function that takes in a bit string of 0's and 1's.
# func can either be constant or balanced, but is not neither.
# 
# constant: if func gives ONLY 0 or ONLY 1 for all inputs.
# balanced: if func gives an EQUAL amount of 1's and 0's for 
# all inputs.
#
# For simplicity's sake, we assume that an input string length n
# goes from [0] x n to [1] x n, that is input string is a
# constant length of n and does not vary.

from random import choice

# classical algorithm worst case is 2^(n - 1）+ 1, in the case
# that 2^n-1 inputs returns a constant output. The
# "2^(n - 1）+ 1"th input would decide if the input function is
# constant or balanced.

def deutschjozsa(func, n):

    s = func(''.join('0' for _ in range(n - len(bin(0)[2:]))) + bin(0)[2:])

    # iterate to worst case perf 2^n-1
    for x in range(1, ((2 << (n-1)) + 1)):
        
        # XOR the output with balance
        cur = func(''.join('0' for _ in range(n - len(bin(0)[2:]))) + bin(x)[2:])

        if cur != s:
            return 'balanced'
    
    return 'constant'

# random input generator
input = ''.join(choice(0,1) for _ in range(0, n))

