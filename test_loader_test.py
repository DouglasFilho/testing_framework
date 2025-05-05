from test_case import TestCase
from test_loader import TestLoader
from test_stub import TestStub
from test_suite import TestSuite
from test_result import TestResult

class TestLoaderTest(TestCase):
    def set_up(self):
        self.loader = TestLoader()
        self.result = TestResult()

    def test_loads_all_test_methods_from_class(self):
        suite = self.loader.load_tests_from_class(TestStub)
        suite.run(self.result)
        self.assert_equals("3 run, 1 failed, 1 error", self.result.summary())

    def test_loads_suite_instance(self):
        suite = self.loader.load_tests_from_class(TestStub)
        self.assert_true(isinstance(suite, TestSuite))

    def test_loads_test_case_instances(self):
        suite = self.loader.load_tests_from_class(TestStub)
        for test in suite.tests:
            self.assert_true(isinstance(test, TestStub))
