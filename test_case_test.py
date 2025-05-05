from test_case import TestCase
from test_result import TestResult
from test_stub import TestStub

class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        test = TestStub("test_success")
        test.run(self.result)
        self.assert_equals("1 run, 0 failed, 0 error", self.result.summary())

    def test_result_failure_run(self):
        test = TestStub("test_failure")
        test.run(self.result)
        self.assert_equals("1 run, 1 failed, 0 error", self.result.summary())

    def test_result_error_run(self):
        test = TestStub("test_error")
        test.run(self.result)
        self.assert_equals("1 run, 0 failed, 1 error", self.result.summary())

    def test_result_multiple_run(self):
        TestStub("test_success").run(self.result)
        TestStub("test_failure").run(self.result)
        TestStub("test_error").run(self.result)
        self.assert_equals("3 run, 1 failed, 1 error", self.result.summary())
