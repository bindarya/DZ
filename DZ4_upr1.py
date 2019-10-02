import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type = int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace.name)
    n = int(namespace.name)
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    print( a )

    