from test_suite import TestSuite

class TestLoader:
    def load_tests_from_class(self, test_class):
        suite = TestSuite()
        for method_name in dir(test_class):
            if method_name.startswith("test_"):
                suite.add_test(test_class(method_name))
        return suite
 