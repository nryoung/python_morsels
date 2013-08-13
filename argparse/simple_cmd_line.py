"""
Simple example of how to use the argparse library.
"""
import argparse

def run():
    # instantiate our argument parser
    parser = argparse.ArgumentParser()

    # add an optional and positional arguments to our instantiated parser
    parser.add_argument('square', type=int,
               help='display a square of a given number')
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='increase output verbosity')

    # actually parse the arguments feed in from the user
    args = parser.parse_args()

    # simply access the arguments we want like instance attributes
    answer = args.square ** 2

    # here again we access the arguments like instance attributes
    if args.verbosity >= 2:
        print 'The square of {} equals {}'.format(args.square, answer)
    elif args.verbosity >= 1:
        print '{}^2 == {}'.format(args.square, answer)
    else:
        print answer

if __name__ == '__main__':
    run()
