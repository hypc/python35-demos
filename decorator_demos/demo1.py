

def deco(func):
    def _deco(*args, **kwargs):
        print('deco start')
        returns = func(*args, **kwargs)
        print('deco end')
        return returns
    return _deco


def deco2(*args1, **kwargs1):
    def _deco(func):
        def __deco(*args, **kwargs):
            print('deco2 start')
            print('args: %s      kwargs: %s' % (args1, kwargs1))
            returns = func(*args, **kwargs)
            print('deco2 end')
            return returns
        return __deco
    return _deco


@deco
@deco2('deco2[0]', 'deco2[1]')
def func(a, b):
    print('a: %s, b: %s' % (a, b))


class A(object):

    @deco2('deco2[0]', 'deco2[1]')
    def func(self, a, b):
        print('a: %s, b: %s' % (a, b))


if __name__ == '__main__':
    func(1, 2)
    print('---------')
    A().func(1, 2)
