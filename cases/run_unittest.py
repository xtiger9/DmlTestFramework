import unittest
import os.path
from BeautifulReport import BeautifulReport

"""
运行测试用例同时生成两种测试报告
"""
if __name__ == '__main__':
    # 测试用例所在目录 and 测试报告保存目录
    if os.getcwd().__contains__('cases'):
        case_dirs = "../cases/"
        report_dir = "../report/"
    else:
        case_dirs = os.getcwd() + "/cases/"
        report_dir = os.getcwd() + "/report/"

    """生成unittest自带的测试报告"""
    discover = unittest.defaultTestLoader.discover(case_dirs, pattern='test_*.py')
    text_report_path = report_dir + "text_dml_report.txt"
    with open(text_report_path, "a", encoding='utf-8') as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(discover)

    """生成BeautifulReport测试报告"""
    discover = unittest.defaultTestLoader.discover(case_dirs, pattern='test_*.py')
    runner = BeautifulReport(discover)
    runner.report(
        description="描述信息",
        filename="beautiful_dml_report",
        report_dir=report_dir
    )
