import unittest
from ddt import ddt, file_data
import sys
import os.path
from BeautifulReport import BeautifulReport

sys.path.append(os.getcwd())
from keywords_driver.dml_keyword import DmlKeywords
from logs.log import Logger
from decimal import Decimal


@ddt
class DmlCases(unittest.TestCase):
    """[mysql数据库] DML测试用例代码部分"""

    @classmethod
    def setUpClass(cls) -> None:
        """类的初始化"""
        cls.if_ = DmlKeywords()
        cls.log = Logger(logger='test')

    @classmethod
    def tearDownClass(cls) -> None:
        """类的释放"""
        pass

    def setUp(self) -> None:
        """主要实现测试前的初始化工作"""
        print('Each test case will be executed once before execution')

    def tearDown(self) -> None:
        """主要实现测试完成后的垃圾回收等工作"""
        print('Each test case will be executed once after execution')

    def assignment(self, kwargs):
        """封装字典对象赋值行为"""
        for key, value in kwargs.items():
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self, key)
        return kwargs

    @file_data('../cases_data/function.yaml')
    def test_1_function(self, **kwargs):
        """测试用例2：测试[mysql数据库]常用聚合函数的功能"""
        try:
            dict_ = self.assignment(kwargs)
            sql = 'SELECT ' + dict_['func_type'] + '(' + dict_['column'] + ')' + ' FROM ' + dict_['table_name'] + ';'
            return_data = self.if_.function(sql=sql, func_type=dict_['func_type'])
            self.log.info('return_data: {}'.format(return_data))
            self.assertEqual(first=Decimal(dict_['value']), second=return_data, msg='查询结果不匹配')
        except Exception as e:
            self.log.error('run error info: {}'.format(e))

    @file_data('../cases_data/select.yaml')
    def test_2_select(self, **kwargs):
        """测试用例2：测试[mysql数据库]select查询语句是否能有效执行"""
        try:
            dict_ = self.assignment(kwargs)
            return_data = self.if_.select(sql=dict_['sql'])
            self.log.info('return_data: {}'.format(return_data))
            self.log.info('dict_: {}'.format(dict_))
        except Exception as e:
            self.log.error('run error info: {}'.format(e))
        else:
            self.assertEqual(first=int(dict_['result_len']), second=return_data, msg='查询结果-不符合预期')

    @file_data('../cases_data/select.yaml')
    def test_3_expalin(self, **kwargs):
        """测试用例3：测试[mysql数据库]是否满足它常用的单表访问方式 """
        try:
            dict_ = self.assignment(kwargs)
            sql = 'explain ' + dict_['sql']
            return_dict = self.if_.explain(sql=sql)
            self.log.debug('sql: {}'.format(sql))
            self.log.info('return_data: {}'.format(return_dict))
        except Exception as e:
            self.log.error('run error info: {}'.format(e))
        else:
            self.assertEqual(first=dict_['type'], second=return_dict['type'], msg='查询访问方式-不符合预期')
            if len(dict_) == 4:
                self.assertEqual(first=dict_['extra'], second=return_dict['extra'], msg='index merge访问方式-不符合预期')


if __name__ == '__main__':
    unittest.main()

