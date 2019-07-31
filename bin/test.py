# coding=utf-8
import os
import sys
import unittest

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path)

from test_case.test_case_1 import MyTestCase
from common.HTMLTestRunner import HTMLTestRunner


def main():
    # 执行测试用例方法一:
    # unittest.main()

    # 执行测试用例方法二:
    report_file_page = path + r'\report\ExampleReport.html'
    suite = unittest.TestSuite()
    # runner = unittest.TextTestRunner()
    suite.addTests([MyTestCase('test_case_1'), MyTestCase('test_case_2')])
    with open(report_file_page, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title=u'腾讯视频爬虫', description=u'爬虫组件单元测试')
        runner.run(suite)

    # 执行测试用例方法三:
    # test_dir = path + '/test_case'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover)


if __name__ == '__main__':
    main()
