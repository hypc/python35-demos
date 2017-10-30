from enum import Enum


class A(Enum):
    a = 1
    b = 2
    c = 3

if __name__ == '__main__':
    print('A:')
    for _ in A:
        print('  %s=%s' % (_.name, _.value))
