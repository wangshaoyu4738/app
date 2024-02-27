import pytest


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

    # 标记某测试函数会失败
    @pytest.mark.xfail(condition=2 > 1, reason="预期失败")
    def test_a(self):
        print('wwwwwwwwwwwwwww')

    # 跳过测试函数
    @pytest.mark.skipif(condition=2>1, reason="跳过")
    def test_b(self):
        print('eeeeeeeeeeeeeeee')


if __name__ == '__main__':
    pytest.main(['-s', 'demo_02.py'])
