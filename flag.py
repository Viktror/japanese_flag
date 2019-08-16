import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', default=1, type=int)
    return parser


def circle(spc, strin, ltrs):
    line = '#'

    for i in range(0, spc - 1):
        line = '%s ' % line

    for i in range(0, strin):
        line = '%s*' % line

    for i in range(0, ltrs):
        line = '%so' % line

    print(line + line[::-1], end='\n')


def counter(c, n):

    while c > 0:
        c -= 1
        print('#', '#', sep=' ' * (n * 3), end='\n')


def flag(N):

    print('#' * ((N * 3) + 2), end='\n')
    count = N / 2

    counter(count, N)

    numspace = int((N * 3) / 2)
    numstars = 1
    numleaters = 0

    circle(numspace, numstars, numleaters)

    while numspace > N + 1:
        numspace -= 1
        numleaters += 1
        circle(numspace, numstars, numleaters)

    circle(numspace, numstars, numleaters)

    while numleaters > 0:
        numspace += 1
        numleaters -= 1
        circle(numspace, numstars, numleaters)

    counter(count, N)
    print('#' * ((N * 3) + 2), end='\n')


if __name__ == '__main__':
    parser = createParser()
    N = parser.parse_args(sys.argv[1:])
    if N.N % 2 != 0:
        raise argparse.ArgumentError(parser.add_argument('N', default=1, type=int), 'parameter is not a valid even integer number')
    flag(N.N)
