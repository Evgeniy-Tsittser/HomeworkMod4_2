
'''
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
            Ничего не выводит на печать
'''

'''
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

test_function()
                    Также ничего не выводит на печать
'''


def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()


