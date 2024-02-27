import pytest


# 它用pytest.fixture标识，以装饰器形式定义在函数上面
@pytest.fixture()
def test_aa():
    print('------aaa---------')


# 函数要以test开头
# 作为参数应用:
def test_01(test_aa):
    print('aaaaaaaaaaaa')
    assert 1


def test_02():
    print('bbbbbbbbbbbb')
    assert 0

# 作为函数应用:
@pytest.mark.usefixtures('test_aa')
class Test_01():
    def setup_class(self):
        print('11111111111')

    def teardown_class(self):
        print('22222222222')

    def setup(self):
        print('qqqqqqqqqqq')

    def teardown(self):
        print('rrrrrrrrrrrrrr')

    @pytest.mark.usefixtures('test_aa')
    def test_a(self):
        print('wwwwwwwwwwwwwww')

    def test_b(self):
        print('eeeeeeeeeeeeeeee')


if __name__ == '__main__':
    pytest.main(['-s', 'demo_04.py'])
