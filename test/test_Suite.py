import unittest
from test_Reactive import TestReactive
from test_Computed import TestComputed
from test_Watch import TestWatch
from test_WatchAttr import TestWatchAttr


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    suite.addTest(TestReactive('test_getter'))
    suite.addTest(TestReactive('test_setter'))

    suite.addTest(TestComputed('test_getter'))
    suite.addTest(TestComputed('test_setter'))

    suite.addTest(TestWatch('test_set_name_1'))
    suite.addTest(TestWatch('test_set_age_1'))
    suite.addTest(TestWatch('test_set_name_2'))
    suite.addTest(TestWatch('test_set_age_2'))

    suite.addTest(TestWatchAttr('test_set_name_1'))
    suite.addTest(TestWatchAttr('test_set_age_1'))
    suite.addTest(TestWatchAttr('test_set_name_2'))
    suite.addTest(TestWatchAttr('test_set_age_2'))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    print(result)

my_suite()