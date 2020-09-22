from pytest import fixture

pytest_plugins = 'pytester'

@fixture('session')
def a():
    return 'a'


@fixture('session')
def b(a):
    return a + ' b'
