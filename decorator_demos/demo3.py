

class Form(object):
    pass


def check_form(form):
    def _deco(func):
        def __deco(clazz, request, *args, **kwargs):
            if request == 'request':
                returns = func(clazz, request, *args, **kwargs)
                return returns

            return '422'
        return __deco
    return _deco


class View(object):

    @check_form(Form)
    def get(self, request):
        return request


if __name__ == '__main__':
    print(View().get('request'))
    print(View().get('1'))
