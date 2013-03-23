"""
Example of looping multiple lists of different lengths concurrently
until all are exhausted.
"""

if __name__ == '__main__':
    l = range(10)
    m = ['a', 'b', 'c', 'd', 'e']
    n = ['one', 'two', 'three']

    for e in map(None, l, m, n):
        # None is mapped in place of exhausted lists
        print e[0]

        if e[1] != None:
            print e[1]
        if e[2] != None:
            print e[2]

