"""
Advanced examples of how to use argparse.
"""
import argparse

def run():
    # instantiate the parser
    parser = argparse.ArgumentParser(description='Calculate X to the power of Y')

    # instantiate a group that allows to specify optional options that conflict
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    # add the positional arguments as well
    parser.add_argument('x', type=int, help='the base')
    parser.add_argument('y', type=int, help='the exponent')

    # actually parse the args from the user
    args = parser.parse_args()

    answer = args.x ** args.y

    # simply access the args like instance attributes
    if args.quiet:
        print answer
    elif args.verbose:
        print '{} to the power {} equals {}'.format(args.x, args.y, answer)
    else:
        print '{}^{} == {}'.format(args.x, args.y, answer)

if __name__ == '__main__':
    run()
