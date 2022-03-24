# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 14:30
# @Copyright：北京码同学
import pytest

@pytest.mark.usefixtures('qianzhi_and_houzhi')
class Test111:
    @pytest.mark.usefixtures('qianzhi_and_houzhi')
    def test_111(self):
        print('这是一条测试用例')

    def test_222(self,qianzhi_and_houzhi):
        print('这是第二条测试用例')

    def test_333(self,return_data):
        # 在测试用例内部使用return_data这个fixture的返回值
        print(return_data)
        print('用例执行完成')


if __name__ == '__main__':
    pytest.assume(1==2)