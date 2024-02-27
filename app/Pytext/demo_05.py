import pytest


# 作用于整个类, 表示每个类的所有测试方法只运行一次
@pytest.fixture(scope='class', autouse=True)
def test_aa():
    print('------aaa---------')


# 函数要以test开头
def test_01():
    print('aaaaaaaaaaaa')
    assert 1


def test_02():
    print('bbbbbbbbbbbb')
    assert 0


class Test_01():
    def setup_class(self):
        print('11111111111')

    def teardown_class(self):
        print('22222222222')

    def setup(self):
        print('qqqqqqqqqqq')

    def teardown(self):
        print('rrrrrrrrrrrrrr')

    def test_a(self):
        print('wwwwwwwwwwwwwww')

    def test_b(self):
        print('eeeeeeeeeeeeeeee')


if __name__ == '__main__':
    pytest.main(['-s', 'demo_05.py'])
